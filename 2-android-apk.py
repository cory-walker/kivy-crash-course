"""
Kivy contact and support:
    http://kivy.org/docs/contact.html
    #Kivy on irc.freenode.net

Kivy android build doc:
    http://kivy.org/docs/guide/packaging-andriod.html

Python-for-android
    https://github.com/kivy/python-for-android
    http://python-for-android.readthedoc.ord/en/latest
    http://kivy.org/docs/guide/packaging-android.html

Buidozer:
    $ sudo pip install buildozer
    https://github.com/kivy/buildozer
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!", font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f


if __name__ == "__main__":
    TutorialApp().run()
