import json
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTime, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon
from QSS_Stylesheet import *
import webbrowser
import languages 

class AboutWindow(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        if parent:
            self.setStyleSheet(parent.styleSheet())
            self.language = self.parent().language

        self.set_language()
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 1000, 400)
        self.setWindowIcon(QIcon("images/about_logo.png"))
        self.about_screen()

    def set_language(self):
        self.title = languages.text[self.language]["about"]

        self.welcome_text = languages.text[self.language]["about_welcome"].format(self.parent().title)
        self.about_info_text = languages.text[self.language]["about_info"]
        self.tutorial_text = languages.text[self.language]["app_tutorial"]

        self.about_creator_btn = languages.button[self.language]["about_creator"]


    def about_screen(self):
        self.welcome = QLabel(self.welcome_text)

        self.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 36px; font-family: {FONT};")

        self.about = QLabel(self.about_info_text)

        self.about.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.author_image = QLabel()
        pixmap = QPixmap("images/author.png")
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.author_image.setPixmap(pixmap)

        self.about_creator = QPushButton(self.about_creator_btn)
        if self.parent():
            self.about_creator.setStyleSheet(self.parent().start_button.styleSheet())
        self.about_creator.clicked.connect(lambda: webbrowser.open("https://github.com/asahinakenneth-afk/pyqt5"))

        self.tutorial = QLabel(self.tutorial_text)

        self.tutorial.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 26px; font-family: {FONT};")

        self.version = QLabel("Version 1.2")
        self.version.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 22px; font-family: {FONT};")

        self.main_layout = QVBoxLayout()
        self.head_layout = QHBoxLayout()
        self.body_layout = QHBoxLayout()
        self.creator_layout = QVBoxLayout()

        self.head_layout.addWidget(self.welcome, alignment=Qt.AlignCenter)

        self.creator_layout.addWidget(self.author_image, alignment=Qt.AlignCenter)
        self.creator_layout.addWidget(self.about_creator, alignment=Qt.AlignCenter)

        self.body_layout.addWidget(self.about, alignment=Qt.AlignLeft)
        self.body_layout.addSpacing(15)
        self.body_layout.addLayout(self.creator_layout)

        self.main_layout.addLayout(self.head_layout)
        self.main_layout.addLayout(self.body_layout)
        self.main_layout.addWidget(self.tutorial, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.version, alignment=Qt.AlignBottom)

        self.setLayout(self.main_layout)

class ConfigWindow(QDialog):
    time_changed = pyqtSignal(QTime)
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        if parent:
            self.setStyleSheet(parent.styleSheet())
            self.language = self.parent().language
            self.is_spanish = (self.parent().language == "es")

        self.current_time = self.parent().default_time

        self.set_language()
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowIcon(QIcon("images/config_logo.png"))
        self.config_screen()
        self.event_handler()

    def set_language(self):
        self.title = languages.text[self.language]["config"]
        self.welcome_text = languages.text[self.language]["config_welcome"]
        self.timers_config_text = languages.text[self.language]["timers_config"]

        self.config_timer_btn = languages.button[self.language]["config_time"] 
        self.full_screen_btn = languages.button[self.language]["full_screen"]   
        self.window_mode_btn = languages.button[self.language]["window_screen"]   
        self.return_btn = languages.button[self.language]["return"]   
        self.save_btn = languages.button[self.language]["save"]

    def config_screen(self):
        self.full_screen = False

        self.welcome = QLabel(self.welcome_text)
        self.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.current_time_label = QLabel(self.parent().default_time.toString("mm:ss"), self)
        self.current_time_label.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.config_timers = QPushButton(self.config_timer_btn)
        self.spanish_mode = QPushButton("Español")
        self.english_mode = QPushButton("English")
        self.set_full_screen = QPushButton(self.full_screen_btn)
        self.set_window_mode = QPushButton(self.window_mode_btn)
        self.return_button = QPushButton(self.return_btn)
        self.save_button = QPushButton(self.save_btn)

        self.add_1_min = QPushButton("+1")
        self.add_5_min = QPushButton("+5")
        self.subs_1_min = QPushButton("-1")
        self.subs_5_min = QPushButton("-5")

        self.config_timers.setFixedSize(300, 75)
        self.spanish_mode.setFixedSize(300, 75)
        self.english_mode.setFixedSize(300, 75)
        self.set_window_mode.setFixedSize(300, 75)
        self.set_full_screen.setFixedSize(300, 75)
        self.return_button.setFixedSize(300, 75)
        self.save_button.setFixedSize(300, 75)

        self.add_1_min.setFixedSize(75, 75)
        self.add_5_min.setFixedSize(75, 75)
        self.subs_1_min.setFixedSize(75, 75)
        self.subs_5_min.setFixedSize(75, 75)

        if self.parent():
            self.config_timers.setStyleSheet(self.parent().start_button.styleSheet())
            self.spanish_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.english_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.set_window_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.set_full_screen.setStyleSheet(self.parent().start_button.styleSheet())
            self.return_button.setStyleSheet(self.parent().start_button.styleSheet())
            self.save_button.setStyleSheet(self.parent().start_button.styleSheet())

            self.add_1_min.setStyleSheet(self.parent().start_button.styleSheet())
            self.add_5_min.setStyleSheet(self.parent().start_button.styleSheet())
            self.subs_1_min.setStyleSheet(self.parent().start_button.styleSheet())
            self.subs_5_min.setStyleSheet(self.parent().start_button.styleSheet())

        self.main_layout = QVBoxLayout()

        self.container = QWidget(self)
        self.timers_layout = QHBoxLayout(self.container)

        self.timers_layout.addWidget(self.subs_5_min, alignment=Qt.AlignCenter)
        self.timers_layout.addWidget(self.subs_1_min, alignment=Qt.AlignCenter)
        self.timers_layout.addWidget(self.current_time_label, alignment=Qt.AlignCenter)
        self.timers_layout.addWidget(self.add_1_min, alignment=Qt.AlignCenter)
        self.timers_layout.addWidget(self.add_5_min, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.container)
        self.main_layout.addWidget(self.return_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.config_timers, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.spanish_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.english_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.set_window_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.set_full_screen, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.save_button, alignment=Qt.AlignCenter)

        self.container.hide()
        self.set_window_mode.hide()

        if self.is_spanish:
            self.spanish_mode.hide()
            self.english_mode.show()
        else:    
            self.english_mode.hide()
            self.spanish_mode.show()
        self.return_button.hide()

        self.setLayout(self.main_layout)

    def config_timers_screen(self):
        self.welcome.setText(self.timers_config_text)

        self.config_timers.hide()
        self.english_mode.hide()
        self.spanish_mode.hide()
        self.set_window_mode.hide()
        self.set_full_screen.hide()
        self.spanish_mode.hide()

        self.container.show()
        self.return_button.show()

    def modify_time(self, mins):
        new_time = self.current_time.addSecs(mins * 60)

        if new_time <= QTime(0, 0, 0):
            return
        if new_time >= QTime(1, 0, 0):
            return
        
        self.current_time = new_time

        self.current_time_label.setText(self.current_time.toString("mm:ss"))

        self.time_changed.emit(self.current_time)

    def return_config_screen(self):
        self.welcome.setText(self.welcome_text)

        self.return_button.hide()
        self.container.hide()

        if self.full_screen:
            self.set_window_mode.show()

        else:
            self.set_full_screen.show()

        if self.is_spanish:
            self.english_mode.show()

        else: 
            self.spanish_mode.show()
        self.config_timers.show()

    def set_spanish(self):
        self.is_spanish = True
        self.language = "es"
        self.spanish_mode.hide()
        self.english_mode.show()

        QMessageBox.information(self, "Aviso", languages.text["es"]["restart"])

    def set_english(self):
        self.is_spanish = False
        self.language = "en"
        self.english_mode.hide()
        self.spanish_mode.show()

        QMessageBox.information(self, "Warning", languages.text["en"]["restart"])

    def full_screen_mode(self):
        self.parent().showFullScreen()
        self.set_full_screen.hide()
        self.set_window_mode.show()
        self.full_screen = True

    def window_screen_mode(self):
        self.parent().showNormal()
        self.set_window_mode.hide()
        self.set_full_screen.show()
        self.full_screen = False

    def save_settings(self):
        config_data = {
        "language": self.language,         
        "default_timer": self.current_time_label.text(),  

        "default_time": {
            "minutes": self.current_time.minute(),
            "seconds": self.current_time.second()
            }
        }
        
        try:
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4, ensure_ascii=False)
            
        except Exception as e:
                print(f"Error al guardar la configuración: {e}")
        self.accept()

    def event_handler(self):
        self.save_button.clicked.connect(self.save_settings)
        self.config_timers.clicked.connect(self.config_timers_screen)
        self.spanish_mode.clicked.connect(self.set_spanish)
        self.english_mode.clicked.connect(self.set_english)
        self.set_full_screen.clicked.connect(self.full_screen_mode)
        self.set_window_mode.clicked.connect(self.window_screen_mode)
        self.return_button.clicked.connect(self.return_config_screen)
        self.add_1_min.clicked.connect(lambda: self.modify_time(1))
        self.add_5_min.clicked.connect(lambda: self.modify_time(5))
        self.subs_1_min.clicked.connect(lambda: self.modify_time(-1))
        self.subs_5_min.clicked.connect(lambda: self.modify_time(-5))

