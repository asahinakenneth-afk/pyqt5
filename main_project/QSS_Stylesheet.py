from pyautogui import size 

WIDTH, HEIGHT = size()

if WIDTH >= 1920 and HEIGHT >= 1080:
    COUNTER_HEIGHT = 512
else:
    COUNTER_HEIGHT = 384

WIDTH, HEIGHT = int(WIDTH*0.9), int(HEIGHT*0.9)

WINDOW_LIGHT = (255, 189, 203)
WINDOW_DARK = (54, 11, 27)
TEMPORIZER_LIGHT = (255, 157, 143)
TEMPORIZER_DARK = (41, 5, 6)
TEXT_COLOR_LIGHT = (36, 10, 16)
TEXT_COLOR_DARK = (209, 148, 165)

REST_LIGHT = (157, 205, 237)
REST_DARK = (3, 23, 28)

BUTTON_LIGHT = (255, 143, 168)
BUTTON_DARK = (102, 0, 34)
BUTTON_HOVER_LIGHT = (255, 120, 110)
BUTTON_HOVER_DARK = (138, 3, 25)

BUTTON_REST_LIGHT = (157, 205, 237)
BUTTON_REST_DARK = (5, 61, 77)
BUTTON_REST_HOVER_LIGHT = (56, 167, 217)
BUTTON_REST_HOVER_DARK = (0, 11, 20)


FONT = "rainyhearts"
FONT_JP = "PixelMplus10-Regular"

SET_LABEL_STYLE_LIGHT = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: 64px; font-family: {FONT};"""
SET_LABEL_STYLE_DARK = f"""color: rgb{TEXT_COLOR_DARK}; font-size: 64px; font-family: {FONT};"""
SET_LABEL_STYLE_JP = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: 64 px; font-family:{FONT_JP}"""

SET_COUNTER_STYLE_LIGHT = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: 24px; font-family: {FONT};"""
SET_COUNTER_STYLE_DARK = f"""color: rgb{TEXT_COLOR_DARK}; font-size: 24px; font-family: {FONT};"""
SET_COUNTER_STYLE_JP = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: 24 px; font-family:{FONT_JP}"""

SET_TIMER_STYLE_LIGHT = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: {COUNTER_HEIGHT}px; font-family: {FONT};"""
SET_TIMER_STYLE_DARK = f"""color: rgb{TEXT_COLOR_DARK}; font-size: {COUNTER_HEIGHT}px; font-family: {FONT};"""
SET_TIMER_STYLE_JP = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: {COUNTER_HEIGHT}px; font-family:{FONT_JP}"""

BUTTON_STYLE_LIGHT = f"""
    QPushButton {{
        background-color: rgb{BUTTON_LIGHT};
        color: rgb{TEXT_COLOR_LIGHT};
        font-family: '{FONT}';
        font-size: 32px;
        font-weight: bold;
        border-style: solid;
        border: 4px solid #000000;
        border-top: 4px solid #ffffff;
        border-left: 4px solid #ffffff;
        border-bottom: 4px solid #FF7898;
        border-right: 4px solid #FF7898;
    }}
    QPushButton:hover {{
        background-color: rgb{BUTTON_HOVER_LIGHT};
    }}
    QPushButton:pressed {{
        border-top: 4px solid #FF7898;
        border-left: 4px solid #FF7898;
        border-bottom: 4px solid #ffffff;
        border-right: 4px solid #ffffff;
    }}
"""

BUTTON_STYLE_DARK = f"""
    QPushButton {{
        background-color: rgb{BUTTON_DARK};
        color:  rgb{TEXT_COLOR_DARK};
        font-family: '{FONT}';
        font-size: 32px;
        font-weight: bold;
        border-style: solid;
        border: 4px solid #000000;
        border-top: 4px solid #BA7070;
        border-left: 4px solid #BA7070;
        border-bottom: 4px solid #8B0000;
        border-right: 4px solid #8B0000;
    }}
    QPushButton:hover {{
        background-color: rgb{BUTTON_HOVER_DARK};
    }}
    QPushButton:pressed {{
        border-top: 4px solid #8B0000;
        border-left: 4px solid #8B0000;
        border-bottom: 4px solid #BA7070;
        border-right: 4px solid #BA7070;
    }}
"""

BUTTON_REST_STYLE_LIGHT = f"""
    QPushButton {{
        background-color: rgb{BUTTON_REST_LIGHT};
        color: rgb{TEXT_COLOR_LIGHT};
        font-family: '{FONT}';
        font-size: 32px;
        font-weight: bold;
        border-style: solid;
        border: 4px solid #000000;
        border-top: 4px solid #ffffff;
        border-left: 4px solid #ffffff;
        border-bottom: 4px solid #6DB5E8;
        border-right: 4px solid #6DB5E8;
    }}
    QPushButton:hover {{
        background-color: rgb{BUTTON_REST_HOVER_LIGHT};
    }}
    QPushButton:pressed {{
        border-top: 4px solid #6DB5E8;
        border-left: 4px solid #6DB5E8;
        border-bottom: 4px solid #ffffff;
        border-right: 4px solid #ffffff;
    }}
"""

BUTTON_REST_STYLE_DARK = f"""
    QPushButton {{
        background-color: rgb{BUTTON_REST_DARK};
        color: rgb{TEXT_COLOR_DARK};
        font-family: '{FONT}';
        font-size: 32px;
        font-weight: bold;
        border-style: solid;
        border: 4px solid #000000;
        border-top: 4px solid #909B9E;
        border-left: 4px solid #909B9E;
        border-bottom: 4px solid #002833;
        border-right: 4px solid #002833;
    }}
    QPushButton:hover {{
        background-color: rgb{BUTTON_REST_HOVER_DARK};
    }}
    QPushButton:pressed {{
        border-top: 4px solid #002833;
        border-left: 4px solid #002833;
        border-bottom: 4px solid #909B9E;
        border-right: 4px solid #909B9E;
    }}
"""