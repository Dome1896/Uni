from apihandler import APIHandler
from question import Question

apiHandler = APIHandler()


question = Question("Schwimmfähigkeit von Schiffen", "Warum Schwimmen schiffe?")
question.setPerfectAnswer(apiHandler)

print(question.getPerfectAnswer())
print(f"{question.title}\nWas ist die Antwort auf die Frage: {question.questionText}")
userAnswer = input(f"{question.title}\nWas ist die Antwort auf die Frage: {question.questionText}")
print (f"Deine Anwort ist zu {question.getQuestionAnswerConformityInPercent(apiHandler, userAnswer)}% richtig")

