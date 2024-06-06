from apihandler import APIHandler
from question import Question
from user import *
class Unittest:

    def __init__(self):
        self.apiHandler = APIHandler()
        self.db = Database()
        

    def runAllTest(self):
        testID1 = self.__getConfirmityInPercent_Test_100()
        return testID1

    def __getConfirmityInPercent_Test_100(self):
        question = Question(title="Title", questionText="Wie lautet des 1.Artikel des Grundgesetztes?", perfectAnswer="Die würde des Menschen ist unantastbar")
        percentage = question.getQuestionAnswerConformityInPercent(apiHandler=self.apiHandler, userAnswer="Die würde des Menschen ist unantastbar")
        if percentage == "100":
            return True
        return False, percentage
