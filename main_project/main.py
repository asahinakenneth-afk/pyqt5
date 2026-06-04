import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtCore import Qt, QTimer, QTime
from pyautogui import size
from QSS_Stylesheet import *
from popups import *

def run():
    app = QApplication([])
    window = MainWindow()
    app.exec_()

## Gracias Gemini por resolverme la duda
myappid = 'pomodoro.pixelart.1.0' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
WIDTH, HEIGHT = size()

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        QFontDatabase.addApplicationFont("rainyhearts.ttf")
        self.config_window()
        self.set_mainscreen()
        self.set_light_mode()
        self.event_handler()
        self.show()

    def config_window(self):
        self.setWindowTitle(TITLE)
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
        self.setWindowIcon(QIcon("logo.png"))

    def set_mainscreen(self):
        self.default_time = "25:00"
        self.default_rest_time = "05:00"
        self.usage_count = 0
        self.is_rest_screen = False
        ## ESTABLECER DISENO DE LA VENTANA
        self.label = QLabel(f"Welcome to {TITLE}!")
        self.counter = QLabel(f"You've concentrated {self.usage_count} times!")
        self.timer = QLabel(self.default_time, self)

        self.label.setStyleSheet(SET_LABEL_STYLE)
        self.counter.setStyleSheet(SET_COUNTER_STYLE)
        self.timer.setStyleSheet(SET_TIMER_STYLE)

        self.config_button = QPushButton("⚙️")
        self.about_button = QPushButton("❓")

        self.start_button = QPushButton("Start temporizer")
        self.stop_button = QPushButton("Stop Temporizer")
        self.return_button = QPushButton("Return to main screen")
        self.mode_button = QPushButton("🌙 Mode")

        self.config_button.setFixedSize(75, 75)
        self.about_button.setFixedSize(75, 75)

        self.start_button.setFixedSize(300, 75)
        self.stop_button.setFixedSize(300, 75)
        self.return_button.setFixedSize(300, 75)

        self.main_Layout = QVBoxLayout()
        self.up_button_Layout = QHBoxLayout()
        self.down_button_Layout = QHBoxLayout()

        self.up_button_Layout.addWidget(self.config_button, alignment=Qt.AlignLeft)
        self.up_button_Layout.addWidget(self.counter, alignment=Qt.AlignCenter)
        self.up_button_Layout.addWidget(self.about_button, alignment=Qt.AlignRight)

        self.down_button_Layout.addWidget(self.start_button)
        self.down_button_Layout.addWidget(self.stop_button)
        self.down_button_Layout.addWidget(self.return_button)

        self.main_Layout.addLayout(self.up_button_Layout)
        self.main_Layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.main_Layout.addWidget(self.timer, alignment=Qt.AlignCenter)

        self.main_Layout.addLayout(self.down_button_Layout)
        self.main_Layout.addWidget(self.mode_button, alignment=Qt.AlignBottom)

        self.stop_button.hide()
        self.counter.hide()
        self.timer.hide()
        self.return_button.hide()

        self.timer_engine = QTimer(self) ## Cuenta el tiempo, valga la redundancia
        self.timer_engine.timeout.connect(self.update_timer) ## La conecta a la funcion que actualiza el tiempo

        self.setLayout(self.main_Layout)

    def open_about_screen(self):
        self.about_window = AboutWindow(self) ## Si no le pones el puto self se abre y se cierra al instante foking python
        self.about_window.show()

    def open_config_screen(self):
    ## self.config_window = ConfigWindow()
    ## self.config_window.exec_() ## Modo modal porque me da yuyu que la persona juguetee con la aplicación mientras se configura JAJJAJ
        pass

    def pomodoro_screen(self):
        self.is_rest_screen = False
        if self.is_light_mode:
            self.set_light_mode()
        else:
            self.set_dark_mode()
        self.label.setText("Temporizer started")
        self.timer.setText(self.default_time)

        self.start_button.hide()

        self.timer.show()
        self.counter.hide()
        self.stop_button.show()
        self.return_button.show()

    def rest_screen(self):
        self.is_rest_screen = True
        self.usage_count += 1
        self.counter.setText(f"You've concentrated {self.usage_count} times!")
        if self.is_light_mode:
            self.set_light_mode()
        else:   
            self.set_dark_mode()
        self.label.setText("Its rest time!")
        self.timer.setText(self.default_rest_time)
        self.stop_button.hide()
        self.counter.show()
        self.rest_temporizer()
        self.update_timer()

    def return_main_screen(self):
        self.is_rest_screen = False
        if self.is_light_mode:
            self.set_light_mode()
        else:   
            self.set_dark_mode()
        self.label.setText(f"Welcome to {TITLE}!")
        self.counter.hide()
        self.return_button.hide()
        self.stop_button.hide()
        self.start_button.show()
        self.timer.hide()
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
        self.pomodoro_screen()
        self.time_left = QTime(0, 0, 25) ## 25 "minutitos"
        self.timer_engine.start(1200) # que tan lento baja el contador de tiempo

    def stop_temporizer(self):
        self.label.setText("Temporizer stopped")
        self.timer_engine.stop()

        self.stop_button.hide()
        self.start_button.show()
        
    def rest_temporizer(self):
        if self.usage_count % 4 == 0 and self.usage_count != 0: ## Cada 4 pomodoros, un descanso largo
            self.time_left = QTime(0, 0, 15) ## 15 minutitos de descanso largo
        else:
            self.time_left = QTime(0, 0, 5) ## 5 minutitos de descanso
        self.timer_engine.start(1800)

    def set_light_mode(self):
        if self.is_rest_screen:
            self.setStyleSheet(f"background-color: rgb{REST_LIGHT};")
            self.config_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.about_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.start_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.stop_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.mode_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
            self.return_button.setStyleSheet(BUTTON_REST_STYLE_LIGHT)
        else:
            self.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
            self.config_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.about_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.start_button.setStyleSheet(BUTTON_STYLE_LIGHT)
            self.stop_button.setStyleSheet(BUTTON_STYLE_LIGHT)
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
            self.about_window.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 24px; font-family: {FONT};")


    def set_dark_mode(self):
        if self.is_rest_screen:
            self.setStyleSheet(f"background-color: rgb{REST_DARK};")

            self.config_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.about_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.start_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.stop_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.mode_button.setStyleSheet(BUTTON_REST_STYLE_DARK)
            self.return_button.setStyleSheet(BUTTON_REST_STYLE_DARK)

        else:   
            self.setStyleSheet(f"background-color: rgb{WINDOW_DARK};")
            self.config_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.about_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.start_button.setStyleSheet(BUTTON_STYLE_DARK)
            self.stop_button.setStyleSheet(BUTTON_STYLE_DARK)
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
            self.about_window.welcome.setStyleSheet(f"color: rgb(168, 15, 54); font-size: 24px; font-family: {FONT};")

    def alternate_mode(self):
        if self.is_light_mode:
            self.set_dark_mode()
            self.mode_button.setText("🌞 Mode")
        else:
            self.set_light_mode()
            self.mode_button.setText("🌙 Mode")

    def event_handler(self):
        self.about_button.clicked.connect(self.open_about_screen)
        self.config_button.clicked.connect(self.open_config_screen)
        self.start_button.clicked.connect(self.start_temporizer)
        self.stop_button.clicked.connect(self.stop_temporizer)
        self.mode_button.clicked.connect(self.alternate_mode)
        self.return_button.clicked.connect(self.return_main_screen)

run()