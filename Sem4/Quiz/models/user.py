from models.database import Database
class User:
    def __init__(self, username, password):
        db = Database()
        self.username = username
        self.password = password
        self.tableName = "users"
        self.__totalPoints = db.getDataFromTableWithFilter(self.tableName, "username", self.username)[0]["totalPoints"]
        

    def get_total_points(self):
        return self.__totalPointsS

    def updateTotalPointsInDB(self, questionPoints, database : Database):
        self.__totalPoints += questionPoints 
        database.updateOneValue(self.tableName, "username", self.username, "totalPoints", self.__totalPoints)

    
class UserRegister:
    def __init__(self, username, password):
       
        self.username = username
        self.password = password
        if self.isUsernameAvailable():
            self.__totalPoints = 0
            self.registerSuc = True
        else: self.registerSuc = False
        self.tableName = "users"
             


    # Wenn der Username bereits in der Datenbank gefunden werden kann, dann return False 
    def isUsernameAvailable(self):
        db = Database()
        response  = db.getDataFromTableWithFilter("users", "username", self.username)
        if len(response) != 0:
            # name ist schon vergeben
            return False
        # name ist noch offen
        return True 
    def makeRequestBody(self):
        return {"username": self.username , "totalPoints" : self.__totalPoints, "password": self.password}    