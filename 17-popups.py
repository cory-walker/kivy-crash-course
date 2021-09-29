from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class Rarity_popup(Popup):
    pass


class Scrn1(Screen):
    pass


class Mgr(ScreenManager):
    rarity_selection = "?"

    def __init__(self, **kwargs):
        super(Mgr, self).__init__(**kwargs)


# popup = Popup(title='test popup', content=Label(
#    text='Hello world'), size_hint=(None, None), size=(400, 400))


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import Factory kivy.factory.Factory
Mgr:
    transition: FadeTransition()
    id: manager
    Scrn1:

<Rarity_popup>:
    title: "Rarities"
    id: rar_pop
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: "common"
            on_release: root.rarity_selection="common"; rar_pop.dismiss(); ThisApp.set_rarity("common")
        Button:
            text: "uncommon"
            on_release: root.rarity_selection="uncommon"; rar_pop.dismiss()
        Button:
            text: "rare"
            on_release: root.rarity_selection="rare"; rar_pop.dismiss()
        Button:
            text: "very rare"
            on_release: root.rarity_selection="very rare"; rar_pop.dismiss()
        Button:
            text: "legendary"
            on_release: root.rarity_selection="legendary"; rar_pop.dismiss()

<Scrn1>:
    Button:
        id: rarity_btn
        text: 'Rarity: ?'
        on_release: Factory.Rarity_popup().open()

'''
                                  )


class ThisApp(App):
    rarity_selection = "?"

    def build(self):
        return root_widget

    def set_rarity(self, rarity, *args):
        self.rarity_selection = rarity


ThisApp().run()
