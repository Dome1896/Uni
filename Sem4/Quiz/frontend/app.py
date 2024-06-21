# Importiert die Hauptklasse der Kivy-App
from kivy.app import App

# Importiert String- und Objekt-Eigenschaften aus Kivy
from kivy.properties import StringProperty, ObjectProperty

# Importiert verschiedene Layouts und Widgets aus Kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.controller import Controller

class LoginWindow(Screen):
    pass

class QuizWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class AddQuestionsWindow(Screen):
    pass

class FragenApp(App):
    def build(self):
        kv = Builder.load_file("my.kv")
        self.icon = "sb.jpg"
        return kv

if __name__ == "__main__":
    FragenApp().run()
