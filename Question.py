import json
import random
import copy

class Question:
    def __init__(self,database):
        self.__data = json.load(database)
        self.__questions = copy.deepcopy(self.__data)
        self.__question = None
        self.__points = 0

    def drawQuestion(self, fromDb = False):
        if fromDb:
            self.__question = random.choice(self.__data["questions"])
        else:
            if len(self.__questions["questions"]) > 0:
                idx = random.randrange(len(self.__questions["questions"]))
                self.__question = self.__questions["questions"][idx]
                self.__points += self.__question['points']
                del self.__questions["questions"][idx]
            else:
                raise IndexError("There is no more questions to pick!")

    def getAllQuestions(self):
        questions = []
        for i in self.__data["questions"]:
            questions.append(i["question"])
        return questions

    def getRemainingQuestions(self):
        questions = []
        for i in self.__questions["questions"]:
            questions.append(i["question"])
        return questions

    def getCount(self):
        return len(self.__data["questions"])

    def getRemainingCount(self):
        return len(self.__questions["questions"])

    def pickQuestionAt(self, idx):
        self.__question = self.__data["questions"][idx]

    def getQuestion(self):
        return self.__question["question"]

    def getCurrentIndex(self):
        return self.__data["questions"].index(self.__question)

    def getAllAnswers(self):
        answers = []
        for i in self.__question["answers"]:
            answers.append(i["text"])
        return answers

    def getTrueAnswers(self):
        answers = []
        for i in self.__question["answers"]:
            if i["isTrue"]:
                answers.append(i["text"])
        return answers

    def getTrueAnswersFor(self,idx):
        answers = []
        for i in self.__data["questions"][idx]["answers"]:
            if i["isTrue"]:
                answers.append(i["text"])
        return answers

    def getAllAnswersFor(self,idx):
        answers = []
        for i in self.__data["questions"][idx]["answers"]:
            answers.append(i["text"])
        return answers
        

    def checkIfAnswerIsTrue(self,answer):
        for i in self.__question["answers"]:
            if(i["text"] == answer):
                return i["isTrue"]
        return False

    def checkIfAnswerIdIsTrue(self,answerId):
        try:
            if int(answerId) >= len(self.__question["answers"]):
                return False
        except ValueError:
            return False

        return self.__question["answers"][int(answerId)]["isTrue"]

    def checkIfAnswerIsTrueFor(self,answer,idx):
        for i in self.__data["questions"][idx]["answers"]:
            if(i["text"] == answer):
                return i["isTrue"]
        return False

    def checkIfAnswerIdIsTrueFor(self,answerId,idx):
        try:
            if int(answerId) >= len(self.__data["questions"][idx]["answers"]):
                return False
        except ValueError:
            return False

        return self.__question["answers"][int(answerId)]["isTrue"]

    def isMultiAnswer(self):
        hasCorrect = False;
        for answer in self.__question["answers"]:
            if not hasCorrect and answer['isTrue']:
                hasCorrect = True
            elif hasCorrect and answer['isTrue']:
                return True
        return False

    def isMultiAnswerFor(self,idx):
        hasCorrect = False;
        for answer in self.__data["questions"][idx]["answers"]:
            if not hasCorrect and answer['isTrue']:
                hasCorrect = True
            elif hasCorrect and answer['isTrue']:
                return True
        return False
        
    def getAllAvailablePoints(self):
        return self.__points

    def getQuestionPoint(self):
        return self.__question['points']

    def getQuestionPointFor(self,idx):
        return self.__data["questions"][idx]['points']
