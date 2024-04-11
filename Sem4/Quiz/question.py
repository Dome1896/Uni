from apihandler import APIHandler
class Question:
    def __init__(self, title, questionText):
        self.title = title
        self.questionText = questionText
        
        
    def getPerfectAnswer(self):
        return self.__perfectAnswer
    
    def setPerfectAnswer(self, apiHandler):
        self.__perfectAnswer = apiHandler.generatePerfectAnswer(self.questionText)
        