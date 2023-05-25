from kivy.utils import get_color_from_hex

def get_color(r, g, b, a):
    return r/255, g/255, b/255

MAIN_COLOR = get_color_from_hex('#26471c')
#MAIN_RGBA = 38/255, 71/255, 28/255, 1
MAIN_RGBA = get_color(60,107,65,255)
SUBMAIN_RGBA = get_color(159,217,203,255)
CONTRAST_RGBA = get_color(250,160,149,255)
#LIGHT_RGBA = get_color(255,221,227,255)
LIGHT_RGBA = get_color(255,255,255,255)
