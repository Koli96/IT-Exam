# -*- coding: utf-8 -*-

from AnswerCollection import *
from PointManager import *
from Question import *
from tkinter import *
from Answer import *
import codecs

window = Tk()
window.title("Quiz")
window.geometry("520x900")


def finish():
    for widget in frame.winfo_children():
        widget.destroy()
    points = Label(navbar, text='Liczba \n punktów:', fg="black", bg="#d3d3d3", width=12)
    points.config(font=("Arial", 12))
    points.pack(anchor=E)
    points.place(y=10)

    label = Label(navbar, text=str(summarize()['points']) + "/" + str(summarize()['availablePoints']), fg="black",
                  bg="#E91E63", width=12)
    label.config(font=("Arial", 12))
    label.pack(anchor=CENTER)
    label.place(y=60)

    if summarize()['points'] / summarize()['availablePoints'] > 0.5:
        label.configure(bg='#8BC34A')


def buildView():
    global quest
    global answersCollections
    answersCollections = []
    quest = Question(codecs.open('./db.json', 'r', 'utf-8'))
    createQuestionsView(answersCollections, quest, navbar)



navbar = Frame(window, bg="#d3d3d3", width=100)
navbar.pack(fill=Y, side=LEFT)

startButton = Button(navbar, text="Start", width=12, command=buildView)
startButton.pack()
startButton.place(x=4, y=120)

endButton = Button(navbar, text="Zakończ", width=12, command=finish)
endButton.pack()
endButton.place(x=4, y=150)

exitButton = Button(navbar, text="Wyjdź", width=12, command=window.destroy)
exitButton.pack()
exitButton.place(x=4, y=180)

labelFrame = LabelFrame(window)
labelFrame.pack(side="left", fill=BOTH)
canvas = Canvas(labelFrame)
canvas.configure(scrollregion=(0, 0, 900, 2500))

scrollbar = Scrollbar(labelFrame)
scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill=Y)
canvas.pack(side="left", fill=Y)

frame = Frame(canvas)
frame.pack(side="top", fill=BOTH)
canvas.create_window(0, 0, window=frame, anchor="nw", width=800)


test = Frame(labelFrame, width=15)
test.pack(fill=Y, side=RIGHT)


def createQuestionsView(answersCollections, quest, navbar):
    for widget in frame.winfo_children():
        widget.destroy()

    for widget in navbar.winfo_children():
        if str(widget).find('label') != -1:
            widget.destroy()



    for i in range(10):
        question = Frame(frame, bg="#fff")
        quest.drawQuestion()

        label = Label(question, text=str(i + 1) + ". " + quest.getQuestion(), fg="black", bg="#fff")
        label.configure(wraplength=350, justify=LEFT)
        label.config(font=("Arial", 12))
        label.pack(anchor=W, pady=5, padx=15)

        answerCollection = AnswerCollection(quest.getCurrentIndex(), quest)
        answersCollections.append(answerCollection)
        stringVar = None

        for answer in quest.getAllAnswersFor(quest.getCurrentIndex()):
            if True == quest.isMultiAnswer():
                answerObject = Answer(answer, IntVar())
                checkButton = Checkbutton(question, text=answer, variable=answerObject.getVariable(), bg="#fff")
                checkButton.pack(anchor=W, padx=30)
                checkButton.configure(wraplength=300, justify=LEFT)
            else:
                if stringVar == None:
                    stringVar = StringVar()
                    stringVar.set("1")
                answerObject = Answer(answer, stringVar)
                radioButton = Radiobutton(question, text=answer, variable=answerObject.getVariable(), value=answer,
                                          bg="#fff")
                radioButton.pack(anchor=W, padx=30)
                radioButton.configure(wraplength=300, justify=LEFT)

            answerCollection.add(answerObject)
        question.pack(fill=BOTH, padx=8, pady=10)


def summarize():
    summarize = PointManager.summarize(answersCollections, quest)

    return summarize


window.mainloop()
