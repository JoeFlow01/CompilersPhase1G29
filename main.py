from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from automata.fa.dfa import DFA
numbers = "0123456789"
operators = "+-*/"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def evenchecker(number):
    if number%2 ==0:
        return True
    else:
        return False

def IdentifierChecker(word):
    if word[0] not in letters:
        return False
    for i in word:
        if((i not in letters) and (i not in numbers)):
            return False
    return True

def operatorchecker(word):
    if len(word) > 1:
        return False
    if word[0] not in operators:
        return False
    return True

def numchecker(word):
    if (word.count(".") > 1):
        return False
    if((word[0]==".") or (word[len(word)-1]==".")):
        return False
    for i in word:
        if((i not in numbers) and i!="."):
            return False
    return True

def expressionchecker(sentence):
    splited_sentence=sentence.split()
    if  evenchecker(len(splited_sentence)):
        return "Not accepted"
    for i in range(0, len(splited_sentence), 2):
        if((numchecker(splited_sentence[i])!=True) and(IdentifierChecker(splited_sentence[i])!=True)):
            return "Not accepted"
    for i in range(1, len(splited_sentence), 2):
        if(operatorchecker(splited_sentence[i])!=True):
            return "Not accepted"
    return "Accepted"

def tokenlister(sentence):
    #if expressionchecker(sentence)=="Not accepted":
     #   return "Not a valid expression"
    mylist=[]
    splited_sentence = sentence.split()
    for i in splited_sentence:
        if(IdentifierChecker(i)):
            mylist.append("ID")
        elif(numchecker(i)):
            mylist.append("Number")
        elif(operatorchecker(i)):
            mylist.append("Operator")
        else:
            mylist.append("Unknown_token")
    return mylist

def tokenlister2(sentence):
    return sentence.split()

main = Tk()
main.title("Design of Compilers Project")
main.minsize(500, 500)
main.geometry("701x438")
bgimg=Image.open("bck.png")
bckend=ImageTk.PhotoImage(bgimg)
lbl=Label(main,image=bckend)
lbl.place(x=0,y=0)
number1Label = Label(text="Enter the Arithmetic Expression")
number1Label.pack(pady=(100,10))

number1Entry = Entry()
number1Entry.pack(pady=10)
def sen():
    num1=number1Entry.get()
    firstlabel = Label(text=" ".join(expressionchecker(num1)))
    firstlabel.pack(pady=10)
    resultLabel = Label(text=" ".join(tokenlister(num1)))
    resultLabel.pack(ipady=10)
    resultLabel2 = Label(text=" ".join(tokenlister2(num1)))
    resultLabel2.pack(pady=10)
    dfa = DFA(
        states={'q1', 'q2', 'q3', 'q4', 'Dead'},
        input_symbols={"ID", "Number", "Operator", "Unknown_token"},
        transitions={
            'q1': {"ID": 'q2', "Number": 'q2', "Operator": 'Dead', "Unknown_token": 'Dead'},
            'q2': {"ID": 'Dead', "Number": 'Dead', "Operator": 'q3',  "Unknown_token": 'Dead'},
            'q3': {"ID": 'q4', "Number": 'q4', "Operator": 'Dead', "Unknown_token": 'Dead'},
            'q4': {"ID": 'Dead', "Number": 'Dead', "Operator": 'q3', "Unknown_token": 'Dead'},
            'Dead': {"ID": 'Dead', "Number": 'Dead', "Operator": 'Dead', "Unknown_token": 'Dead'},
        },
        initial_state='q1',
        final_states={'q4', 'Dead'}
    )
    state_sequence=""
    for i in dfa.read_input_stepwise(tokenlister(number1Entry.get())):
        state_sequence=state_sequence+i+" "
    label=Label(text=state_sequence)
    label.pack()

but=Button(text="Check",command=sen)
but.pack(pady=5)


def openNewWindow():
    newWindow = Toplevel(main)
    newWindow.title("DFA")
    newWindow.geometry("1600x1600")
    Label(newWindow).pack()
    frame = Frame(newWindow, width=200, height=200)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("DFA.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()
    newWindow.mainloop()

btn = Button(main, text="Show DFA", command=openNewWindow)
btn.pack(pady=15)
label = Label(main)
label.pack(pady=5)

main.mainloop()












