from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

# tutorial video: https://www.youtube.com/watch?v=ZmteLworB4E&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq&index=5


class ScatterTextWidget(BoxLayout):
    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        label = self.ids['my_label']
        label.color = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
