from Question import *
from Answer import *

class AnswerCollection:
    def __init__(self, questionId, question: Question):
        self.questionId = questionId
        self.question = question
        self.answerCollection = []

    def add(self, answer: Answer):
        self.answerCollection.append(answer)

    def getCollection(self):
        return self.answerCollection

    def isTrueAnswered(self):
        trueAnswer = 0
        self.question.pickQuestionAt(self.questionId)

        for answer in self.answerCollection:
            if self.isRadio(answer):
                return self.question.checkIfAnswerIsTrue(answer.getValue())
            else:
                if self.isCheckedAnswer(answer):
                    answerIsTrue = self.question.checkIfAnswerIsTrue(answer.getAnswer())
                    if True == answerIsTrue:
                        trueAnswer +=1
                    else:
                        return False

        return trueAnswer == len(self.question.getTrueAnswers())

    def getAnswerPoint(self):
        return self.question.getQuestionPoint()

    def isRadio(self,answer):
        return isinstance(answer.getValue(), str)

    def isCheckedAnswer(self, answer):
        return  bool(answer.getValue())
