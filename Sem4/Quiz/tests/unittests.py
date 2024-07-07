import unittest
from unittest.mock import patch
from models.question import Question, QuestionChooser
from models.apihandler import APIHandler
from models.database import Database
from models.user import * 

from datetime import timedelta
import time

class TestQuestion(unittest.TestCase):
    def test_getConfirmityInPercent(self):
        '''
        TestID: 1
        Test: 2 mal die gleiche Anfrage stellen, Ergenisse max +-5
        '''
        question:Question = Question(
            title="Title",
            questionText="Wie lautet der 1. Artikel des Grundgesetzes?",
            perfectAnswer="Die Würde des Menschen ist unantastbar"
        )
        apiHandler = APIHandler()
        userAnswer = "Die Würde des Menschen ist unantastbar"

        result1 = question.getQuestionAnswerConformityInPercent(apiHandler, userAnswer)
        result2 = question.getQuestionAnswerConformityInPercent(apiHandler, userAnswer)
        print(f"Res1: {result1}\n Res2: {result2}")

        self.assertTrue(-5 <= int(result1) - int(result2) <= 5)

    def test_setPerfectAnswer(self):
        '''
        TestID: 5
        Test: Prüft, ob Antworten generiert werden können
        und testet ob die Antwort das richtige Ergebnis beinhaltet
        '''
        question = Question(
            title="Golfbälle",
            questionText="Wie viele Einkerbungen hat ein Golfball?"
        )
        apiHandler = APIHandler()

        question.setPerfectAnswer(apiHandler)
        # ist 336 in der perfekten Antwort
        self.assertIn("336", question.getPerfectAnswer())

    def test_getRandomQuestion(self):
        '''
        TestID: 9
        Test: Zeit bis eine Frage geladen wurde  
        '''
        questionChooser = QuestionChooser()
        db = Database()
   
        
        with patch('time.time', return_value=0):
            start_time = time.time()
            allQuestions = db.getAllDataFromOneTable("questions")
            questionChooser.getRandomQuestion(allQuestionsAsJson=allQuestions.json())
            end_time = time.time()

        # Fragen innerhalb von 1,5 Sekunden geladen 
        self.assertLess(end_time - start_time, 1.5)

    def test_setPerfectAnswer_time(self):
        '''
        TestID: 10
        Test: Zeit bis eine perfekte Antwort generiert wurde
        '''
        question = Question(
            title="Golfbälle",
            questionText="Wie viele Einkerbungen hat ein Golfball?"
        )
        apiHandler = APIHandler()
        userAnswer = "336"
        
        with patch('time.time', return_value=0):
            start_time = time.time()
            question.setPerfectAnswer(apiHandler)
            end_time = time.time()
        # Antworte sollte in unter 3 Sekunden generiert sein
        self.assertLess(end_time - start_time, 3)

    def test_getConfirmityInPercent_time(self):
        '''
        TestID: 11
        Test: Zeit bis die Übereinstimmung von Antwort
        und perfekten Antwort generiert ist
        '''
        question = Question(
            title="Title",
            questionText="Wie lautet der 1. Artikel des Grundgesetzes?",
            perfectAnswer="Die Würde des Menschen ist unantastbar"
        )
        apiHandler = APIHandler()
        userAnswer = "Die Würde des Menschen ist unantastbar"
        
        with patch('time.time', return_value=0):
            start_time = time.time()
            question.getQuestionAnswerConformityInPercent(apiHandler, userAnswer)
            end_time = time.time()
        # Konformität innerhalb von 2 Sekunden
        self.assertLess(end_time - start_time, 2)
    
    def test_makeRequestBody(self):
        '''
        TestID: 4
        Test: Prüft die Richtigkeit des RequestBody
        '''
        question = Question(title="test", questionText="testText", perfectAnswer="perfektTest")
        expected_output = {"title": "test" , "questionText" : "testText", "perfectAnswer" : "perfektTest"}
        
        self.assertEqual(question.makeRequestBody(), expected_output)


class TestUserRegister(unittest.TestCase):
    def test_isUsernameAvailable(self):
        '''
        TestID: 2
        Test: Prüft username Validierung
        '''
        # vergebener Name
        user_register = UserRegister(username= "vergebenerUsername", password="pw")
        self.assertFalse(user_register.isUsernameAvailable())

        # freier Name
        user_register.username = "freierUsername"
        self.assertTrue(user_register.isUsernameAvailable())

    def test_makeRequestBody(self):
        '''
        TestID: 3
        Test: Prüft die Richtigkeit des RequestBody
        '''
        db = Database()
        user_register = UserRegister(username="test", password="pw")
        expected_output = {"username": "test", "totalPoints": 0, "password": "pw"}
        
        self.assertEqual(user_register.makeRequestBody(), expected_output)
        if user_register.registerSuc:
            db.setDataToDB(user_register)


class TestUser(unittest.TestCase):
    def test_updateTotalPointsInDB(self):
        '''
        TestID: 8
        Test: Addieren von Punkten in der DB
        '''
        user = User(username="test", password="pw")
        questionPoints = 10
        db = Database()
        
        user.updateTotalPointsInDB(questionPoints, db)
        
        self.assertEqual(user.get_total_points(), 20)
        # zurücksetzen der Punkte 
        db.del_one_entry(tableName="users", attributeKey="username", attributeValue="test")




