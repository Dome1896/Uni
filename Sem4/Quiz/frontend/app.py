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
from controller.controller import Controller

class LoginWindow(Screen):
    def login(self):
        if not Controller.user_login(self.ids.username.text, self.ids.password.text):
            self.ids.slogan_msg.text = "Login nicht möglich"

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        #self.ids.welcome_msg.text = f"Hallo {Controller.user.username}, du hast aktuell {Controller.user.get_total_points()}"

    def get_all_question(self):
        Controller.get_all_questions()

class AddQuestionsWindow(Screen):
    def generate_answer(self, instance):
        # Generieren der Antwort
        title = self.ids.frageTitel_input.text
        question_input = self.ids.frage_input.text
        perfect_answer = Controller.create_question(title=title, questionText=question_input)
        self.ids.antwort_input.text = perfect_answer
        # Anpassen des Buttons
        self.ids.generate_or_save_question.bind(on_release=self.save_data)
        self.ids.generate_or_save_question.text = "Frage speichern"

    def save_data(self, instance):
        # Speichern der Frage
        Controller.save_question(title= self.ids.frageTitel_input.text, questionText=self.ids.frage_input.text, answer=self.ids.antwort_input.text)
        self.ids.frageTitel_input.text = ""
        self.ids.frage_input.text = ""
        self.ids.antwort_input.text = ""  
        # Anpassen des Buttons
        self.ids.generate_or_save_question.text = "Antwort generieren"
        self.ids.generate_or_save_question.bind(on_release=self.generate_answer)

class QuizWindow(Screen):
    def next_question(self, instance):
        Controller.next_question()
        self.ids.frageTitel_label.text = Controller.question.title
        self.ids.frage_label.text = Controller.question.questionText
        self.ids.next_question.bind(on_release=self.reveal_answer)

    def reveal_answer(self, instance):
       self.ids.perfect_answer_label.text = Controller.question.getPerfectAnswer()
       self.ids.points_label.text = "Punkte: " + Controller.get_points(user_answer=self.ids.Quiz_antwort_input.text)
       self.ids.next_question.bind(on_release=self.next_question)

class PopupRegister(Popup):
    def reg_user(self):
        if Controller.user_reg(self.ids.username.text, self.ids.password.text):
            self.ids.message.text = "Registrierung erfolgreich.\nAutomatischer Login"
            Controller.user_login(self.ids.username.text, self.ids.password.text)
            app = App.get_running_app()
            app.root.current = "main"
            app.root.transition.direction = "left"
            self.dismiss()
        else:
            self.ids.message.text = "Username bereits vergeben"

class FragenApp(App):
    def build(self):
        kv = Builder.load_file("frontend/my.kv")
        self.icon = "sb.jpg"
        return kv

    def show_register_popup(self):
        popup = PopupRegister()
        popup.open()

if __name__ == "__main__":
    FragenApp().run()