from AnswerCollection import *
from PointManager import *
from Question import *
from tkinter import *
from Answer import *

quest = Question(open('./db.json'))

window = Tk()
window.title("Quiz")
window.geometry("500x800")
window.wm_resizable(0, 0)


def finish():
    label = Label(navbar, text=str(summarize()['points']) + "/" + str(summarize()['availablePoints']), fg="black", bg="#fff", width=12)
    label.config(font=("Arial", 12))
    label.pack(anchor=CENTER)
    label.place(y=60)



navbar = Frame(window, bg="#d3d3d3", width=100)
navbar.pack(fill=Y, side=LEFT)

points = Label(navbar, text='Liczba \n punktów:', fg="black", bg="#d3d3d3", width=12)
points.config(font=("Arial", 12))
points.pack(anchor=E)
points.place(y=10)

# startButton = Button(navbar, text="Start", width=12)
# startButton.pack()
# startButton.place(x=4, y=120)

endButton = Button(navbar, text="Zakończ quiz", width=12, command=finish)
endButton.pack()
endButton.place(x=4, y=150)

exitButton = Button(navbar, text="Wyjdź", width=12, command=window.destroy)
exitButton.pack()
exitButton.place(x=4, y=180)

labelFrame = LabelFrame(window, width=100, height=100)
labelFrame.pack(side="left", fill=BOTH)
canvas = Canvas(labelFrame, relief=SUNKEN)
canvas.configure(scrollregion=(0, 0, 300, 2000))

scrollbar = Scrollbar(labelFrame)
scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill=Y)
canvas.pack(side="left", fill=BOTH)

frame = Frame(canvas)
frame.pack(side="top", fill=BOTH)
canvas.create_window(0, 0, window=frame, anchor="nw")

answersCollections = []

column = 1
row = 0
w = 0
for i in range(2):
    question = Frame(frame, bg="#fff")

    row += 3
    quest.drawQuestion()
    label = Label(question, text=str(i + 1) + ". " + quest.getQuestion(), fg="black", bg="#fff")
    label.config(font=("Arial", 12))
    label.pack(anchor=W, pady=5, padx=15)

    answerCollection = AnswerCollection(quest.getCurrentIndex(), quest)
    answersCollections.append(answerCollection)
    stringVar = None
    row += 3

    for answer in quest.getAllAnswersFor(quest.getCurrentIndex()):
        row += 1
        w += 1

        if True == quest.isMultiAnswer():
            answerObject = Answer(answer, IntVar())
            checkButton = Checkbutton(question, text=answer, variable=answerObject.getVariable(), bg="#fff")
            checkButton.pack(anchor=W, padx=30)
        else:
            if stringVar == None:
                stringVar = StringVar()
            answerObject = Answer(answer, stringVar)
            radioButton = Radiobutton(question, text=answer, variable=answerObject.getVariable(), value=answer,
                                      bg="#fff")
            radioButton.pack(anchor=W, padx=30)

        answerCollection.add(answerObject)
    question.pack(fill=BOTH, padx=70, pady=10)


def summarize():
    summarize = PointManager.summarize(answersCollections, quest)
    # print(summarize)
    return summarize


window.mainloop()
