from apihandler import APIHandler
import re
class Question:
   
    def __init__(self, title, questionText):
        self.title = title
        self.questionText = questionText
        
        
        
    def getPerfectAnswer(self):
        return self.__perfectAnswer
    
    def setPerfectAnswer(self, apiHandler):
        self.__perfectAnswer = apiHandler.generatePerfectAnswer(self.questionText)

    def getQuestionAnswerConformityInPercent(self, apiHandler, userAnswer):
        while (True):
            conformity = apiHandler.getQuestionAnswerConformityInPercent(self, userAnswer)
            conformity = re.sub(r"\D", "", conformity)
            if len(conformity) <= 2 and conformity.isdigit():
                break
        return conformity 

        
        