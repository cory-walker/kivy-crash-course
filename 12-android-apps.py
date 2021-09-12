from kivy.app import App
#from jnius import autoclass
#from plyer.notification import notify

import plyer

# tutorial video: https://www.youtube.com/watch?v=8Jwp1PTvECI&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq&index=12

''' Used for pyjnius
PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity

Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
'''

class AndroidApp(App):
    def build(self):
        #vibrator.vibrate(10000)
        plyer.notification.notify('Some title','some message')    

AndroidApp().run()
