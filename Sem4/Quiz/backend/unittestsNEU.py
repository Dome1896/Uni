import unittest
from unittest.mock import patch
from question import Question
from apihandler import APIHandler
from database import Database
from user import * 

class TestQuestion(unittest.TestCase):
    def test_getConfirmityInPercent(self):
        question = Question(
            title="Title",
            questionText="Wie lautet der 1. Artikel des Grundgesetzes?",
            perfectAnswer="Die Würde des Menschen ist unantastbar"
        )
        apiHandler = MockApiHandler()
        userAnswer = "Die Würde des Menschen ist unantastbar"

        result1 = question.getConfirmityInPercent(apiHandler, userAnswer)
        result2 = question.getConfirmityInPercent(apiHandler, userAnswer)

        self.assertTrue(-5 <= result1 - result2 <= 5)

    def test_setPerfectAnswer(self):
        question = Question(
            title="Golfbälle",
            questionText="Wie viele Einkerbungen hat ein Golfball?"
        )
        apiHandler = MockApiHandler()
        userAnswer = "336"

        question.setPerfectAnswer(apiHandler, userAnswer)

        self.assertIn("336", question.perfectAnswer)

    def test_getRandomQuestion(self):
        questionChooser = QuestionChooser()
        allQuestions = getAllQuestionsAsJson()
        
        with patch('time.time', return_value=0):
            start_time = time.time()
            questionChooser.getRandomQuestion(allQuestions)
            end_time = time.time()
        
        self.assertLess(end_time - start_time, 1.5)

    def test_setPerfectAnswer_time(self):
        question = Question(
            title="Golfbälle",
            questionText="Wie viele Einkerbungen hat ein Golfball?"
        )
        apiHandler = MockApiHandler()
        userAnswer = "336"
        
        with patch('time.time', return_value=0):
            start_time = time.time()
            question.setPerfectAnswer(apiHandler, userAnswer)
            end_time = time.time()
        
        self.assertLess(end_time - start_time, 3)

    def test_getConfirmityInPercent_time(self):
        question = Question(
            title="Title",
            questionText="Wie lautet der 1. Artikel des Grundgesetzes?",
            perfectAnswer="Die Würde des Menschen ist unantastbar"
        )
        apiHandler = MockApiHandler()
        userAnswer = "Die Würde des Menschen ist unantastbar"
        
        with patch('time.time', return_value=0):
            start_time = time.time()
            question.getConfirmityInPercent(apiHandler, userAnswer)
            end_time = time.time()
        
        self.assertLess(end_time - start_time, 2)

class TestUserRegister(unittest.TestCase):
    def test_isUsernameAvailable(self):
        user_register = UserRegister()
        user_register.username = "vergebenerUsername"
        
        self.assertFalse(user_register.__isUsernameAvailable())
        
        user_register.username = "freierUsername"
        
        self.assertTrue(user_register.__isUsernameAvailable())

    def test_makeRequestBody(self):
        user_register = UserRegister(username="test")
        expected_output = {"username": "test", "totalPoints": 0}
        
        self.assertEqual(user_register.makeRequestBody(), expected_output)

class TestUser(unittest.TestCase):
    def test_setDataToDB(self):
        user = User(username="test", password="test")
        db = Database()
        self.assertTrue(db.setDataToDB(user))

    def test_updateTotalPointsInDB(self):
        user = User(username="test")
        questionPoints = 10
        database = MockDatabase()
        
        user.updateTotalPointsInDB(questionPoints, database)
        
        self.assertEqual(user.totalPoints, 20)

# Mock classes and functions
class MockApiHandler:
    def get_answer(self, questionText):
        return "Die Würde des Menschen ist unantastbar"

class MockDatabase:
    def __init__(self):
        self.totalPoints = 0

    def update_points(self, points):
        self.totalPoints += points

def getAllQuestionsAsJson():
    return []

if __name__ == '__main__':
    unittest.main()
