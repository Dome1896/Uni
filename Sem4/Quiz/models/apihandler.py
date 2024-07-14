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
            #{"role": "system", "content": "Just Answer with a Number between 0 and 100"},
            #{"role": "user", "content": f"PerfectAnswer: {question.getPerfectAnswer()} \n Users Answer: {userAnswer} \n How closely does the User Answer match the Perfect Answer in percentage?"}

            {"role": "system", "content": "You are a scoring system that evaluates how closely a user's answer matches a perfect answer. Respond with a number between 0 and 100 that represents the percentage match."},
            {"role": "user", "content": f"Perfect Answer: {question.getPerfectAnswer()} \n User's Answer: {userAnswer} \n On a scale from 0 to 100, how closely does the User's Answer match the Perfect Answer in percentage? Provide a number only."}     
                    ]
            )
        
        conformity = completion.choices[0].message.content
        return conformity
    

    def __getApiKey(self):
        cfp = ConfigParser()
        try:
            cfp.read("config.ini")
            __apikey = cfp.get("API", "apikey")
            return __apikey
        except:
            print("config.ini is missing or wrong")
            
    
        
