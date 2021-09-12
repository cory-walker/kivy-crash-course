from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty

# tutorial video: https://www.youtube.com/watch?v=WdcUg_rX2fM&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq&index=9

Builder.load_string('''
<ScrollableLabel>:
    text: str('some really really long string ' * 100)
    Label:
        text: root.text
        font_size: 10
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


if __name__ == "__main__":
    runTouchApp(ScrollableLabel())
