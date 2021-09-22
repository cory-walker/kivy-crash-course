from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


class ScrnMgr(ScreenManager):
    pass


class MenuBar(BoxLayout):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScrnMgr:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: '1st screen'
<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: '2nd screen'

<MenuBar>:
    orientation: 'horizontal'
    size_hint_y: None
    size_y: 15
    Button:
        text: 'Main'
        on_release: app.root.current = 'first'
    Button:
        text: 'second'
        on_release: app.root.current = 'second'
''')


class LayoutExperimentApp(App):
    def build(self):
        return root_widget


LayoutExperimentApp().run()
