from apihandler import APIHandler
from question import Question, QuestionChooser
from database import Database
from user import User, UserRegister

apiHandler = APIHandler()
db = Database()

# register
if (input("l for login OR r for register: ") == "r"):
    while True:
        username = input("username: ")
        newUser = UserRegister(username)
        if newUser.registerSuc:
            db.setDataToDB(newUser)
            print("User angelegt")
            break
        print("Name ist already used")


# login

loginUsername= input("loging username: ")
user = User(loginUsername)

# apiHandler = APIHandler()
# print(apiHandler.generatePerfectAnswer("Warum schwimmen Schiffe?"))
# test = Question(title="Akkulaufzeit", questionText="Wie lange hält ein Akku mit 4500 mAh?", perfectAnswer="ca. 9 Stunden")
# db.setDataToDB(test)
# game loop auf den

# erhalten aller fragen
allQuestions = db.getAllDataFromOneTable("questions").json()
# es wird eine zufällige Frage ausgewählt
chosenQuestion = QuestionChooser.getRandomQuestion(allQuestions)
# das Objekt zu der Frage wird erstellt 
question = Question(chosenQuestion["title"], chosenQuestion["questionText"], chosenQuestion["perfectAnswer"])
print(question.toString())
# der Nutzer gibt die Antwort ein
userAnswer = input("Antwort eingeben: ")
# die Antwort wird mit der Perfekten Antwort verglichen
percentage = question.getQuestionAnswerConformityInPercent(apiHandler, userAnswer)
# der User erhält seine Punkte
user.updateTotalPointsInDB(questionPoints=percentage, database=db)      

# question = Question("Schwimmfähigkeit von Schiffen", "Warum Schwimmen schiffe?")
# question.setPerfectAnswer(apiHandler)

# print(question.getPerfectAnswer())
# print(f"{question.title}\nWas ist die Antwort auf die Frage: {question.questionText}")
# userAnswer = input(f"{question.title}\nWas ist die Antwort auf die Frage: {question.questionText}")
# print (f"Deine Anwort ist zu {question.getQuestionAnswerConformityInPercent(apiHandler, userAnswer)}% richtig")

