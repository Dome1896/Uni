from apihandler import APIHandler
from question import Question, QuestionChooser
from database import Database
from user import User, UserRegister

apiHandler = APIHandler()
db = Database()

# register

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

# game loop auf den

# erhalten aller fragen
answers = db.getAllDataFromOneTable("questions")
# es wird eine zufällige Frage ausgewählt
chosenQuestion = QuestionChooser.getRandomQuestion(answers)
# das Objekt zu der Frage wird erstellt 
question = Question(chosenQuestion["title"], chosenQuestion["questionText"], chosenQuestion["perfectAnswer"])
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

