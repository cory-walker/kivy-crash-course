from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar

from settingsJson import settings_json

# Tutorial: https://www.youtube.com/watch?v=oQdGWeN51EE

Builder.load_string('''
<interface>
    orientation: 'vertical'
    Button:
        text: 'open the settings'
        font_size: 100
        on_release: app.open_settings()
''')


class Interface(BoxLayout):
    pass


class SettingsApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.config.items('example')
        setting = self.config.get('example', 'boolexample')
        self.use_kivy_settings = False
        return Interface()

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True, 'numericexample': 10, 'optionsexample': 'option2', 'stringexample': 'some_string', 'pathexample': '/some/path'
        })

    def build_settings(self, settings):
        settings.add_json_panel('Panel Name', self.config, data=settings_json)

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)


SettingsApp().run()
