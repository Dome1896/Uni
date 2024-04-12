from database import Database
class User:
    def __init__(self, username):
        db = Database()
        self.username = username
        self.tableName = "users"
        self.__totalPoints = db.getDataFromTableWithFilter(self.tableName, "username", self.username)[0]["totalPoints"]
        

    def updateTotalPointsInDB(self, questionPoints, database):
        self.__totalPoints += questionPoints 
        database.updateOneValue(self.tableName, "username", self.username, "totalPoints", self.__totalPoints)

    
class UserRegister:
    def __init__(self, username):
       
        self.username = username
        if self.__isUsernameAvailable():
            self.__totalPoints = 0
            self.registerSuc = True
        else: self.registerSuc = False
        self.tableName = "users"
             


    # Wenn der Username bereits in der Datenbank gefunden werden kann, dann return False 
    def __isUsernameAvailable(self):
        db = Database()
        response  = db.getDataFromTableWithFilter("users", "username", self.username)
        if len(response) != 0:
            # name ist schon vergeben
            return False
        # name ist noch offen
        return True 
    def makeRequestBody(self):
        return {"username": self.username , "totalPoints" : self.__totalPoints}    