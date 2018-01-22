from Question import *

class PointManager:
    @staticmethod
    def summarize(answersCollection, questions: Question):
        points = 0
        for answerCollection in answersCollection:
            if True == answerCollection.isTrueAnswered():
                points += answerCollection.getAnswerPoint()

        return {"points": points, "availablePoints": questions.getAllAvailablePoints()}
