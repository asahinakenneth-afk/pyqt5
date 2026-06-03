WINDOW_LIGHT = (255, 199, 222)
WINDOW_DARK = (54, 11, 27)
TEMPORIZER_LIGHT = (255, 157, 143)
TEMPORIZER_DARK = (41, 5, 6)
TEXT_COLOR = (255, 255, 255)
REST_LIGHT = (157, 205, 237)
REST_DARK = (3, 23, 28)
BUTTON_LIGHT = (255, 143, 168)
BUTTON_DARK = (102, 0, 34) 
BUTTON_HOVER_LIGHT = (255, 120, 110)
BUTTON_HOVER_DARK = (138, 3, 25)
FONT = "Consolas"
FONT_SIZE = 32
SET_LABEL_STYLE = f"""color: rgb{TEXT_COLOR}; font-size: {FONT_SIZE}px; font-family: {FONT};"""

SET_TIMER_STYLE = f"""color: rgb{TEXT_COLOR}; font-size: 346px; font-family: {FONT};"""

BUTTON_STYLE_LIGHT = f"""
    QPushButton {{
        background-color: rgb{BUTTON_LIGHT};
        color: #FFFFFF;
        font-family: '{FONT}';
        font-size: 24px;
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
        color: #FFFFFF;
        font-family: '{FONT}';
        font-size: 24px;
        font-weight: bold;
        border-style: solid;
        border: 4px solid #000000;
        border-top: 4px solid #ffffff;
        border-left: 4px solid #ffffff;
        border-bottom: 4px solid #8B0000;
        border-right: 4px solid #8B0000;
    }}
    QPushButton:hover {{
        background-color: rgb{BUTTON_HOVER_DARK};
    }}
    QPushButton:pressed {{
        border-top: 4px solid #8B0000;
        border-left: 4px solid #8B0000;
        border-bottom: 4px solid #ffffff;
        border-right: 4px solid #ffffff;
    }}
"""