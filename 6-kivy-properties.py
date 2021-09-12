from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty

import random

# tutorial video: https://www.youtube.com/watch?v=OkW-1uzP5Og&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq&index=6


class ScatterTextWidget(BoxLayout):

    text_colour = ListProperty([1, 0, 0, 1])

    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        self.text_colour = colour

        ''' # changing colour by ID method
        label = self.ids['my_label']
        label.color = colour

        label1 = self.ids.label1
        label2 = self.ids['label2']

        label1.color = colour
        label2.color = colour
        '''

    def on_text_colour(self, *args):
        pass


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
