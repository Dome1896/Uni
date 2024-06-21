from backend.question import *
from backend.apihandler import APIHandler
from backend.user import *
from backend.database import *


class Controller:
    db = Database()
    apiHandler = APIHandler()
    
    #----------- Start LOGIN --------------
    @classmethod
    def user_login(cls, username, password):
        cls.user: User
        pass

    @classmethod
    def user_reg(cls, username, password):
        pass
    #----------- End LOGIN --------------

    #----------- Start MENU -------------
    @classmethod
    def get_all_questions(cls):
        cls.all_questions = cls.db.getAllDataFromOneTable("questions")
    #----------- End MENU -------------
    
    #----------- Start Quiz -------------
    @classmethod
    def next_question(cls):
        chosenQuestion =  QuestionChooser.getRandomQuestion(cls.all_questions)
        cls.question = Question(chosenQuestion["title"], chosenQuestion["questionText"], chosenQuestion["perfectAnswer"])
    
    @classmethod
    def get_points(cls, user_answer):
        points = cls.question.getQuestionAnswerConformityInPercent(cls.apiHandler,user_answer)
        cls.user.updateTotalPointsInDB(points, cls.db)
        return points
    #----------- End QUIZ ---------------

    #----------- Start CREATE QUESTION -------------
    @classmethod
    def create_question(cls, title, questionText):
        question = Question(title=title, questionText=questionText)
        perfect_answer = question.getPerfectAnswer(cls.apiHandler)
        cls.db.setDataToDB(question)
        return perfect_answer
    #----------- End CREATE QUESTION ---------------