import sys
import ctypes
import json
import languages
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtCore import Qt, QTimer, QTime
from QSS_Stylesheet import *
from popups import *
from time import sleep

def run():
    app = QApplication([])
    window = MainWindow()
    app.exec_()

## Gracias Gemini por resolverme la duda (sólo quería íconos bonitos...)
myappid = 'pomodoro.1.0' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        QFontDatabase.addApplicationFont("fonts/rainyhearts.ttf")
        QFontDatabase.addApplicationFont("fonts/PixelMplus10-Regular.ttf")
        
        self.language = "en"
        self.default_timer = "25:00"
        self.default_time = QTime(0, 25, 0)
        self.usage_count = 0
 
        self.config = "config.json"
        ## Okay juro que lo único que pedí a la IA fue lo de abrir el archivo json, el try/error es mío
        try: 
            with open("config.json", "r", encoding="utf-8") as archivo:
                data = json.load(archivo)

                self.language = data["language"]
                self.default_timer = data["default_timer"]
                time_data = data.get("default_time", {"minutes": 25, "seconds": 0})
                self.default_time = QTime(0, time_data["minutes"], time_data["seconds"])
        except FileNotFoundError:
            pass

        self.set_language()
        self.config_window()
        self.set_mainscreen()
        self.event_handler()
        self.set_light_mode()
        self.show()

    def config_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
        self.setWindowIcon(QIcon("images/logo.png"))

    def set_language(self):
        self.title = languages.text[self.language]["title"]

        ##TEXT
        self.welcome_app_text = languages.text[self.language]["start_welcome"].format(self.title)
        self.counter_text = languages.text[self.language]["counter"].format(self.usage_count)

        self.temp_start_text = languages.text[self.language]["temp_start"]
        self.tempt_stop_text = languages.text[self.language]["temp_stop"]
        self.rest_text = languages.text[self.language]["rest"]

        ##BUTTONS
        self.start_temp_btn = languages.button[self.language]["start"]
        self.continue_temp_btn = languages.button[self.language]["continue"]
        self.stop_temp_btn = languages.button[self.language]["stop"]
        self.return_btn = languages.button[self.language]["return"]
        self.mode_light_btn = languages.button[self.language]["mode_light"]
        self.mode_dark_btn = languages.button[self.language]["mode_dark"]

    def set_mainscreen(self):
        self.is_rest_screen = False
        ## ESTABLECER DISENO DE LA VENTANA

        self.label = QLabel(self.welcome_app_text)
        self.counter = QLabel(self.counter_text)
        self.timer = QLabel(self.default_timer, self)

        self.label.setStyleSheet(SET_LABEL_STYLE)
        self.counter.setStyleSheet(SET_COUNTER_STYLE)
        self.timer.setStyleSheet(SET_TIMER_STYLE)

        self.config_button = QPushButton("⚙️")
        self.about_button = QPushButton("❓")

        self.start_button = QPushButton(self.start_temp_btn)
        self.re_start_button = QPushButton(self.continue_temp_btn)
        self.stop_button = QPushButton(self.stop_temp_btn)
        self.return_button = QPushButton(self.return_btn)
        self.mode_button = QPushButton(self.mode_dark_btn)

        self.config_button.setFixedSize(75, 75)
        self.about_button.setFixedSize(75, 75)

        self.start_button.setFixedSize(360, 90)
        self.re_start_button.setFixedSize(360, 90)
        self.stop_button.setFixedSize(360, 90)
        self.return_button.setFixedSize(360, 90)

        self.main_Layout = QVBoxLayout()
        self.up_button_Layout = QHBoxLayout()
        self.down_button_Layout = QHBoxLayout()

        self.up_button_Layout.addWidget(self.config_button, alignment=Qt.AlignLeft)
        self.up_button_Layout.addWidget(self.counter, alignment=Qt.AlignRight)
        self.up_button_Layout.addWidget(self.about_button, alignment=Qt.AlignRight)

        self.down_button_Layout.addWidget(self.start_button)
        self.down_button_Layout.addWidget(self.re_start_button)
        self.down_button_Layout.addWidget(self.stop_button)
        self.down_button_Layout.addWidget(self.return_button)

        self.main_Layout.addLayout(self.up_button_Layout)
        self.main_Layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.main_Layout.addWidget(self.timer, alignment=Qt.AlignCenter)

        self.main_Layout.addLayout(self.down_button_Layout)
        self.main_Layout.addWidget(self.mode_button, alignment=Qt.AlignBottom)

        self.stop_button.hide()
        self.re_start_button.hide()
        self.counter.hide()
        self.timer.hide()
        self.return_button.hide()

        self.timer_engine = QTimer(self) ## Cuenta el tiempo, valga la redundancia

        self.setLayout(self.main_Layout)

    def open_about_screen(self):
        self.about_window = AboutWindow(self) ## Si no le pones el puto self se abre y se cierra al instante foking python
        self.wait_time(0.5)
        self.about_window.show()

    def open_config_screen(self):
        self.config_window = ConfigWindow(self)
        self.config_window.time_changed.connect(self.update_timer_live)
        self.config_window.exec_() ## Modo modal porque me da yuyu que la persona juguetee con la aplicación mientras se configura JAJJAJ

    def pomodoro_screen(self):
        self.wait_time(0.5)
        self.is_rest_screen = False
        if self.is_light_mode:
            self.set_light_mode()
        else:
            self.set_dark_mode()
        self.label.setText(self.temp_start_text)

        self.start_button.hide()
        self.counter.hide()
        self.re_start_button.hide()
        self.config_button.hide()

        self.timer.show()
        self.stop_button.show()
        self.return_button.show()

    def rest_screen(self):
        self.wait_time(0.5)
        self.is_rest_screen = True
        self.usage_count += 1
        self.counter.setText(self.counter_text)
        if self.is_light_mode:
            self.set_light_mode()
        else:   
            self.set_dark_mode()

        self.label.setText(self.rest_text)
        self.timer.setText("05:00")
        self.stop_button.hide()
        self.counter.show()
        self.re_start_button.hide()

        self.rest_temporizer()
        self.update_timer()

    def return_main_screen(self):
        self.wait_time(0.5)
        self.is_rest_screen = False
        if self.is_light_mode:
            self.set_light_mode()
        else:   
            self.set_dark_mode()
        self.label.setText(self.welcome_app_text)

        self.counter.hide()
        self.return_button.hide()
        self.stop_button.hide()
        self.re_start_button.hide()
        self.timer.hide()

        self.start_button.show()
        self.config_button.show()

        self.timer_engine.stop()

    def update_timer(self):
        # Sirve para todos los contadores

        ## Basicamente le resta los segundos al contador
        self.time_left = self.time_left.addSecs(-1)
        ## Si no pones esto no se actualiza JAJA
        self.timer.setText(self.time_left.toString("mm:ss")) ##solo minutos y segunditos

        if self.time_left == QTime(0, 0, 0):
            self.timer_engine.stop()

            if not self.is_rest_screen:
                self.rest_screen()
            else:
                self.start_temporizer()
                self.is_rest_screen = False

    def start_temporizer(self):
        self.time_left = self.default_time ## 25 "minutitos"
        self.pomodoro_screen()
        self.timer_engine.start(1200) # que tan lento baja el contador de tiempo

    def continue_temporizer(self):
        self.timer_engine.start(1200)
        self.stop_button.show()
        self.re_start_button.hide()

    def stop_temporizer(self):
        self.label.setText(self.stop_temp_btn)
        self.timer_engine.stop()

        self.stop_button.hide()
        self.re_start_button.show()
        
    def rest_temporizer(self):
        if self.usage_count % 4 == 0 and self.usage_count != 0: ## Cada 4 pomodoros, un descanso largo
            self.time_left = QTime(0, 15, 0) ## 15 minutitos de descanso largo
        else:
            self.time_left = QTime(0, 5, 0) ## 5 minutitos de descanso
        self.timer_engine.start(2000)

    def update_timer_live(self, new_time):
        self.default_time = new_time
        self.time_left = new_time
        self.timer.setText(self.time_left.toString("mm:ss"))

    def set_light_mode(self):
        self.wait_time(0.2)
        if self.is_rest_screen:
            self.setStyleSheet(f"background-color: rgb{REST_LIGHT};")
            self.config_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.about_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.start_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.stop_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.re_start_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.mode_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.return_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
        else:
            self.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
            self.config_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.about_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.start_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.stop_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.re_start_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.mode_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.return_button.setStyleSheet(BUTTON_STYLE_LIGHT)
        self.is_light_mode = True

        if hasattr(self, 'about_window') and self.about_window.isVisible():
            if self.is_rest_screen:
                self.about_window.setStyleSheet(f"background-color: rgb{REST_LIGHT};")
                self.about_window.about_creator.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            else:
                self.about_window.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
                self.about_window.about_creator.setStyleSheet(BUTTON_STYLE_LIGHT)

    def set_dark_mode(self):
        self.wait_time(0.2)
        if self.is_rest_screen:
            self.setStyleSheet(f"background-color: rgb{REST_DARK};")

            self.config_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.about_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.start_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.stop_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.re_start_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.mode_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.return_button.setStyleSheet(BUTTON_REST_STYLE_DARK)

        else:   
            self.setStyleSheet(f"background-color: rgb{WINDOW_DARK};")
            self.config_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.about_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.start_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.stop_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.re_start_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.mode_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.return_button.setStyleSheet(BUTTON_STYLE_DARK)
        self.is_light_mode = False

        if hasattr(self, 'about_window') and self.about_window.isVisible():
            if self.is_rest_screen:
                self.about_window.setStyleSheet(f"background-color: rgb{REST_DARK};")
                self.about_window.about_creator.setStyleSheet(BUTTON_REST_STYLE_DARK)
            else:
                self.about_window.setStyleSheet(f"background-color: rgb{WINDOW_DARK};")
                self.about_window.about_creator.setStyleSheet(BUTTON_STYLE_DARK)

    def alternate_mode(self):
        if self.is_light_mode:
            self.set_dark_mode()
            self.mode_button.setText(self.mode_light_btn)
        else:
            self.set_light_mode()
            self.mode_button.setText(self.mode_dark_btn)

    def wait_time(self, seconds):
        global sleep
        sleep(seconds)

    def event_handler(self):
        self.timer_engine.timeout.connect(self.update_timer) ## La conecta a la funcion que actualiza el tiempo
        self.about_button.clicked.connect(self.open_about_screen)
        self.config_button.clicked.connect(self.open_config_screen)
        self.start_button.clicked.connect(self.start_temporizer)
        self.re_start_button.clicked.connect(self.continue_temporizer)
        self.stop_button.clicked.connect(self.stop_temporizer)
        self.mode_button.clicked.connect(self.alternate_mode)
        self.return_button.clicked.connect(self.return_main_screen)

run()