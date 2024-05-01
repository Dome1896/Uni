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

# if user says yes, gets the code to create a new question
if (input("Möchtest du eine Frage anlegen? (y/n): ") == "y"):
    title = input("Fragentitel eingeben: ")
    questionText = input("Gebe deine Frage ein: ")
    newQuestion = Question(title=title, questionText=questionText)
    newQuestion.setPerfectAnswer(apiHandler=apiHandler)
    db.setDataToDB(newQuestion)

    
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
print(percentage)
# der User erhält seine Punkte
user.updateTotalPointsInDB(questionPoints=int(percentage), database=db)      
