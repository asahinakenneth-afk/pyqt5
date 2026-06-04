from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from QSS_Stylesheet import *
import webbrowser

class AboutWindow(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        if parent:
            self.setStyleSheet(parent.styleSheet())

        self.setWindowTitle("About")
        self.setGeometry(0, 0, 1000, 400)
        self.setWindowIcon(QIcon("about_logo.png"))
        self.about_screen()

    def about_screen(self):
        self.welcome = QLabel(f"Welcome to the 'about' screen of {TITLE}!")

        self.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 36px; font-family: {FONT};")

        self.about = QLabel(f"""
            The pomodoro technique is a time management method developed by Francesco Cirillo in the late 1980s.
    The technique uses a timer to break down work into intervals, usually 25 minutes in length, separated by short breaks!
  The method is designed to improve focus and productivity, I hope it helps you to concentrate and manage your time better.""")

        self.about.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.image = QLabel()
        pixmap = QPixmap("autor.png")
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image.setPixmap(pixmap)

        self.about_creator = QPushButton("Created with love by me! ❤️")
        if self.parent():
            self.about_creator.setStyleSheet(self.parent().start_button.styleSheet())
        self.about_creator.clicked.connect(lambda: webbrowser.open("https://github.com/asahinakenneth-afk/pyqt5"))

        self.tutorial = QLabel(f"""
                                    The usage of this app is very simple:\n
1. Just click on the "Start Temporizer" button to start the pomodoro timer. 
2. When the timer reaches 0, it will automatically switch to the rest screen.
3. You can switch to light or dark mode with the button below the start button, 
4. You can return to the main screen with the "Return to main screen" button!
5. If you want to change the default time or rest time, just click on the "⚙️" button...
6. Then enter the desired time in the format "MM:SS" (minutes:seconds) and click on "Save".
7. If you want to full-size this app, also click on the "⚙️" button and then click on the "full-size mode" button!""")

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

        self.setWindowTitle("Configuration")
        self.setGeometry(0, 0, 300, 300)
        self.setWindowIcon(QIcon("config_logo.png"))
        self.config_screen()
        self.event_handler()

    def config_screen(self):
        self.welcome = QLabel("Configuration Screen")
        self.welcome.setStyleSheet(f"color: rgb{TEXT_COLOR}; font-size: 30px; font-family: {FONT};")

        self.config_timers = QPushButton("Config time")
        self.spanish_mode = QPushButton("🇲🇽")
        self.set_full_screen = QPushButton("Full-Screen mode")
        self.set_window_mode = QPushButton("Window mode")
        self.return_button = QPushButton("Return")

        self.config_timers.setFixedSize(300, 75)
        self.spanish_mode.setFixedSize(300, 75)
        self.set_window_mode.setFixedSize(300, 75)
        self.set_full_screen.setFixedSize(300, 75)

        if self.parent():
            self.config_timers.setStyleSheet(self.parent().start_button.styleSheet())
            self.spanish_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.set_window_mode.setStyleSheet(self.parent().start_button.styleSheet())
            self.set_full_screen.setStyleSheet(self.parent().start_button.styleSheet())
            self.return_button.setStyleSheet(self.parent().start_button.styleSheet())


        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.return_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.config_timers, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.spanish_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.set_window_mode, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.set_full_screen, alignment=Qt.AlignCenter)

        self.set_window_mode.hide()
        self.return_button.hide()

        self.setLayout(self.main_layout)

    def config_timers_screen(self):
        self.welcome.setText("Timers configuration")

        self.set_window_mode.hide()
        self.set_full_screen.hide()
        self.spanish_mode.hide()

        self.return_button.show()

    def return_config_screen(self):
        self.welcome.setText("Configuration Screen")

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

    def event_handler(self):
        self.config_timers.clicked.connect(self.config_timers_screen)
        self.set_full_screen.clicked.connect(self.full_screen_mode)
        self.set_window_mode.clicked.connect(self.window_screen_mode)


