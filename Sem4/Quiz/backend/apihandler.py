from configparser import ConfigParser
from openai import OpenAI
class APIHandler:
    def __init__(self):
        self.client = OpenAI(api_key=self.__getApiKey())
    
    def generatePerfectAnswer(self, questionText):
        # ChatGPT Api Anfrage
        # schauen, wie man genau mit chatGPT anfragen behandelt
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "Just give and answer to the following question"},
            {"role": "user", "content": questionText}
                    ]
            )
        
        perfectAnswer = completion.choices[0].message.content
        return perfectAnswer
    
    def getQuestionAnswerConformityInPercent(self, question, userAnswer):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "Just Answer with a Number between 0 and 100"},
            {"role": "user", "content": f"PerfectAnswer: {question.getPerfectAnswer()} \n Users Answer: {userAnswer} \n For how much percentage does the User Answer fits the Perfect Answer"
             
             }
                    ]
            )
        
        conformity = completion.choices[0].message.content
        return conformity
    

    def __getApiKey(self):
        cfp = ConfigParser()
        try:
            cfp.read("backend/config.ini")
            __apikey = cfp.get("API", "apikey")
            return __apikey
        except:
            print("config.ini is missing or wrong")
            
    
        
