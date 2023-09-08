from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
import pickle
import json
import os

from keras.models import load_model

from AI import get

Window.size = (300,500) 

intents = json.loads(open(os.getcwd()+"\\intents.json").read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            root.manager.current = 'profile'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome'
        halign: 'center'
"""

class MainScreen(Screen):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)
        print(self.name)

class MenuScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name="home"))
sm.add_widget(MenuScreen(name="menu"))

class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_file("app.kv")
        return screen
    
    def navigation_draw(self):
        print("Pressed")
    
    def get_search(self, obj, label):
        if obj.__contains__("search"):
            I = get.Information.search(str(obj).replace("search",""))
            label.text = str(I)
        else:
            ints = get.Information.predict(obj)
            res = get.Information.get_response(ints, intents)
            label.text = res   
App().run()