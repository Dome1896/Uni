import re
import random
from backend.apihandler import APIHandler
class Question:
    
    def __init__(self, title, questionText, perfectAnswer = ""):
        self.title = title
        self.questionText = questionText
        self.__perfectAnswer = perfectAnswer
        self.tableName = "questions"    
        
        
    def getPerfectAnswer(self):
        return self.__perfectAnswer
    
    def setPerfectAnswer(self, apiHandler : APIHandler):
        self.__perfectAnswer = apiHandler.generatePerfectAnswer(self.questionText)

    def getQuestionAnswerConformityInPercent(self, apiHandler : APIHandler, userAnswer):
        while (True):
            conformity = apiHandler.getQuestionAnswerConformityInPercent(self, userAnswer)
            conformity = re.sub(r"\D", "", conformity)
            if len(conformity) <= 3 and conformity.isdigit():
                break
        return conformity
    
    def makeRequestBody(self):
        return {"title": self.title , "questionText" : self.questionText, "perfectAnswer" : self.__perfectAnswer}
    
    def toString(self):
        return f"Title: {self.title} \nQuestion: {self.questionText}"
     
class QuestionChooser:
    @classmethod
    def getRandomQuestion(allQuestionsAsJson):
        randomQuestionID = random.randint(0, len(allQuestionsAsJson)-1)
        return allQuestionsAsJson[randomQuestionID]
        
        
        