from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.properties import ListProperty

# Tutorial: https://www.youtube.com/watch?v=xx-NLOg6x8o


class ColourScreen(BoxLayout):
    colour = ListProperty([1., 0., 0., 1.)

root_widget= Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    FirstScreen:
    SecondScreen:
    ColourScreen:

<FirstScreen>:
    orientation: 'vertical'
    Label:
        text: 'first screen'
        font_size: 30
    Image:
        source: 'colours.png'
        allow_strech: True
        keep_ratio: False
    BoxLayout:
        Button:
            text: 'goto second screen'
            font_size: 30
        Button:
            text: 'get random colour screen'
            font_size: 30
<SecondScreen>:
    orientation: 'vertical'
    Label:
        text: 'second screen'
        font_size: 30
    Image:
        source: 'colours.png'
        allow_strech: True
        keep_ratio: False
    BoxLayout:
        Button:
            text: 'goto second screen'
            font_size: 30
        Button:
            text: 'get random colour screen'
            font_size: 30
<ColourScreen>:
    orientation: 'vertical'
    Label:
        text: 'first screen'
        font_size: 30
    Image:
        source: 'colours.png'
        allow_strech: True
        keep_ratio: False
    BoxLayout:
        Button:
            text: 'goto second screen'
            font_size: 30
        Button:
            text: 'get random colour screen'
            font_size: 30
''')
