class Answer:
    def __init__(self, answer, variable):
        self.answer = answer
        self.variable = variable

    def getAnswer(self):
        return self.answer

    def getValue(self):
        return self.variable.get()

    def getVariable(self):
        return self.variable
