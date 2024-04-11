from apihandler import APIHandler
from question import Question

apiHandler = APIHandler("gptURL")


question = Question("Schwimmfähigkeit von Schiffen", "Warum Schwimmen schiffe?")
question.setPerfectAnswer(apiHandler)


print(question.getPerfectAnswer())