from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Hello world!!'
    Button:
        text: 'Click here to dismiss'
        on_press: pop.chosen_rarity="common";pop.set_and_dismiss()
''')

rarity = "?"


class SimplePopup(Popup):
    chosen_rarity = StringProperty("?")

    def __init__(self, **kwargs):
        super(SimplePopup, self).__init__(**kwargs)

    def set_and_dismiss(self, *args):
        global rarity
        rarity = self.chosen_rarity
        print(rarity)
        self.dismiss()


class SimpleButton(Button):
    text = "Fire Popup !"

    def fire_popup(self):
        pops = SimplePopup()
        pops.open()


class SampleApp(App):
    def build(self):
        return SimpleButton()


SampleApp().run()
