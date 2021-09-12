
from kivy.app import App

from jnius import autoclass

# tutorial video: https://www.youtube.com/watch?v=8Jwp1PTvECI&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq&index=12

PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity

Contect = autoclass('android.content.Contect')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)


class AndroidApp(App):
    def build(self):
        vibrator.vibrate(10000)


AndroidApp().run()
