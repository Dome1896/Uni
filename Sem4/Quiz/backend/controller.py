from backend.question import *
from backend.apihandler import APIHandler
from backend.user import *
from backend.database import *

import time


class Controller:
    db = Database()
    apiHandler = APIHandler()
    
    #----------- Start LOGIN --------------
    @classmethod
    def user_login(cls, username, password):
        try:
            cls.user = User(username=username, password=password)
        except Exception:
            return False
        else:
            return True
    #----------- End LOGIN --------------

    #----------- Start User Register -------
    @classmethod
    def user_reg(cls, username, password):
        user = UserRegister (username, password)
        if user.registerSuc:
            cls.db.setDataToDB(user)
            return True
        else:
            return False
    @classmethod
    def wait_3_seconds(cls, window):
        time.sleep(3)
        window.dismiss()
    
    #----------- End User Register --------

    #----------- Start MENU -------------
    @classmethod
    def get_all_questions(cls):
        cls.all_questions = cls.db.getAllDataFromOneTable("questions")
    #----------- End MENU -------------
    
    #----------- Start Quiz -------------
    @classmethod
    def next_question(cls):
        chosenQuestion =  QuestionChooser.getRandomQuestion(cls.all_questions.json())
        cls.question = Question(chosenQuestion["title"], chosenQuestion["questionText"], chosenQuestion["perfectAnswer"])
    
    @classmethod
    def get_points(cls, user_answer):
        points = cls.question.getQuestionAnswerConformityInPercent(cls.apiHandler,user_answer)
        cls.user.updateTotalPointsInDB(int(points), cls.db)
        return points
    #----------- End QUIZ ---------------

    #----------- Start CREATE QUESTION -------------
    @classmethod
    def create_question(cls, title, questionText):
        question = Question(title=title, questionText=questionText)
        question.setPerfectAnswer(cls.apiHandler)
        # Frage im zwischenspeicher Speichern
        cls.cache_question = question
        return question.getPerfectAnswer()
    
    @classmethod
    def save_question(cls, title, questionText, answer):
        # prüfen, ob es Änderungen an den Werten gab
        if title != cls.cache_question.title: 
            cls.cache_question.title = title
        if questionText != cls.cache_question.questionText: 
            cls.cache_question.questionText = questionText
        if answer != cls.cache_question.getPerfectAnswer(): 
            cls.cache_question.__perfectAnswer = answer
        # speichern der Frage und zurücksetzen der Frage
        cls.db.setDataToDB(cls.cache_question)
        cls.cache_question = None
    #----------- End CREATE QUESTION ---------------