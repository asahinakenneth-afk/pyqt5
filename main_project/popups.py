from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from QSS_Stylesheet import *
import webbrowser
import languages 

class AboutWindow(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        if parent:
            self.setStyleSheet(parent.styleSheet())

        self.set_language()
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 1000, 400)
        self.setWindowIcon(QIcon("about_logo.png"))
        self.about_screen()

    def set_language(self):
        self.title = languages.text[self.parent().language]["about"]

        self.welcome_text = languages.text[self.parent().language]["about_welcome"].format(self.parent().title)
        self.about_info_text = languages.text[self.parent().language]["about_info"]
        self.tutorial_text = languages.text[self.parent().language]["app_tutorial"]

        self.about_creator_btn = languages.button[self.parent().language]["about_creator"]


    def about_screen(self):
        self.welcome = QLabel(self.welcome_text)

        self.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 36px; font-family: {FONT};")

        self.about = QLabel(self.about_info_text)

        self.about.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.image = QLabel()
        pixmap = QPixmap("autor.png")
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image.setPixmap(pixmap)

        self.about_creator = QPushButton(self.about_creator_btn)
        if self.parent():
            self.about_creator.setStyleSheet(self.parent().start_button.styleSheet())
        self.about_creator.clicked.connect(lambda: webbrowser.open("https://github.com/asahinakenneth-afk/pyqt5"))

        self.tutorial = QLabel(self.tutorial_text)

        self.tutorial.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 26px; font-family: {FONT};")

        self.version = QLabel("Version 1.0")
        self.version.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 22px; font-family: {FONT};")

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.about, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.tutorial, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.image, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.about_creator, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.version, alignment=Qt.AlignBottom)

        self.setLayout(self.main_layout)

class ConfigWindow(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        if parent:
            self.setStyleSheet(parent.styleSheet())

        self.set_language()
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowIcon(QIcon("images/config_logo.png"))
        self.config_screen()
        self.event_handler()

    def set_language(self):
        self.title = languages.text[self.parent().language]["config"]
        self.welcome_text = languages.text[self.parent().language]["config_welcome"]
        self.timers_config_text = languages.text[self.parent().language]["timers_config"]

        self.config_timer_btn = languages.button[self.parent().language]["config_time"] 
        self.full_screen_btn = languages.button[self.parent().language]["full_screen"]   
        self.window_mode_btn = languages.button[self.parent().language]["window_screen"]   
        self.return_btn = languages.button[self.parent().language]["full_screen"]   
        self.save_btn = languages.button[self.parent().language]["save"]

    def config_screen(self):
        self.welcome = QLabel(self.welcome_text)
        self.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.config_timers = QPushButton(self.config_timer_btn)
        self.spanish_mode = QPushButton("Español")
        self.english_mode = QPushButton("English")
        self.set_full_screen = QPushButton(self.full_screen_btn)
        self.set_window_mode = QPushButton(self.window_mode_btn)
        self.return_button = QPushButton(self.return_btn)
        self.save_button = QPushButton(self.save_btn)

        self.config_timers.setFixedSize(300, 75)
        self.spanish_mode.setFixedSize(300, 75)
        self.english_mode.setFixedSize(300, 75)
        self.set_window_mode.setFixedSize(300, 75)
        self.set_full_screen.setFixedSize(300, 75)
        self.return_button.setFixedSize(300, 75)
        self.save_button.setFixedSize(300, 75)

        if self.parent():
            self.config_timers.setStyleSheet(self.parent().start_button.styleSheet())
            self.spanish_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.english_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.set_window_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.set_full_screen.setStyleSheet(self.parent().start_button.styleSheet())
            self.return_button.setStyleSheet(self.parent().start_button.styleSheet())
            self.save_button.setStyleSheet(self.parent().start_button.styleSheet())

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.return_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.config_timers, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.spanish_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.english_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.set_window_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.set_full_screen, alignment=Qt.AlignCenter)

        self.set_window_mode.hide()
        self.english_mode.hide()
        self.return_button.hide()

        self.setLayout(self.main_layout)

    def config_timers_screen(self):
        self.welcome.setText(self.timers_config_text)

        self.set_window_mode.hide()
        self.set_full_screen.hide()
        self.spanish_mode.hide()

        self.return_button.show()

    def return_config_screen(self):
        self.welcome.setText(self.welcome_text)

        self.return_button.hide()

        self.set_window_mode.show()
        self.set_full_screen.show()
        self.spanish_mode.show()

    def full_screen_mode(self):
        self.parent().showFullScreen()
        self.set_full_screen.hide()
        self.set_window_mode.show()

    def window_screen_mode(self):
        self.parent().showNormal()
        self.set_window_mode.hide()
        self.set_full_screen.show()

    def save_changes(self):
        pass

    def event_handler(self):
        self.config_timers.clicked.connect(self.config_timers_screen)
        self.set_full_screen.clicked.connect(self.full_screen_mode)
        self.set_window_mode.clicked.connect(self.window_screen_mode)


