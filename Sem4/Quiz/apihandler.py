from configparser import ConfigParser
import requests
class APIHandler:
    def __init__(self, url):
        self.__getApiKey()
        self.__url = url
    
    def generatePerfectAnswer(self, questionText):
        # ChatGPT Api Anfrage
        # schauen, wie man genau mit chatGPT anfragen behandelt
        #response = requests.get(self.url, header={'Authorization': f'apikey {self.__apikey}'})
        #perfectAnswer = response.choices[0].message.content
        return "sad"
    

    

    def __getApiKey(self):
        cfp = ConfigParser()
        try:
            cfp.read("config.ini")
            self.__apikey = cfp.get("API", "apikey")
        
        except:
            print("config.ini is missing")
            
    
        
