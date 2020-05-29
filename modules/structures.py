import os
import shutil

def simple_app_mvc(app_path, name):
    # name patternize
    models = app_path + '\\models'
    views = app_path + '\\views'
    controllers = app_path + '\\controllers'
    main_app = app_path + '\\main.py'
    route_app = app_path + '\\routes.py'
    # paths creating
    os.mkdir(app_path)

    with open(main_app, 'w') as f:
        f.write(f"""\
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return Button(text = "{name}")

MainApp().run()
""")

def show_case_mvc(app_path):
    ...
