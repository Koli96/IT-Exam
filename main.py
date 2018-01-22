from AnswerCollection import *
from PointManager import *
from Question import *
from tkinter import *
from Answer import *


quest = Question(open('./db.json'))

window=Tk()
window.title("Quiz")
window.geometry("600x360")

answersCollections=[]

column = 1
row = 0
w = 0
for i in range(2):
    row +=3
    quest.drawQuestion()
    Label(text=quest.getQuestion()).grid(row=row,column=column,sticky=W)


    answerCollection = AnswerCollection(quest.getCurrentIndex(), quest)
    answersCollections.append(answerCollection)
    stringVar = None
    row +=3
    for answer in quest.getAllAnswersFor(quest.getCurrentIndex()):
       row +=1
       w +=1

       if True == quest.isMultiAnswer():
            answerObject = Answer(answer,IntVar())
            Checkbutton(window, text=answer, variable=answerObject.getVariable()).grid(row=row, sticky=W)
       else:
            if stringVar == None:
                stringVar = StringVar()
            answerObject = Answer(answer,stringVar)
            Radiobutton(window, text=answer, variable=answerObject.getVariable(), value=answer).grid(row=row, sticky=W)

       answerCollection.add(answerObject)


def summarize():
    summarize = PointManager.summarize(answersCollections, quest)
    print(summarize)

Button(window, text='Finish', command=summarize).grid(row=100, sticky=W, pady=4)

window.mainloop()
