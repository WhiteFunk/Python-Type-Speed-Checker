from tkinter import *
import ctypes
import random
import tkinter
from tkinter import font
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title('Type Speed Checker')

root.geometry('700x700')

font1 = font.Font(family= "Clarendon Blk BT", size=30)
# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", font1)
root.option_add("*Button.Font", font1)

def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            labelRight.configure(text=labelRight.cget('text')[1:])
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'After the Second World War, Germany was occupied by Allied forces, including England and Russia. Russia wasn\'t happy about some of the things that the Western Allies were doing in Germany, so they surrounded Berlin and stopped supplies reaching the city. The RAF was part of a team who airlifted supplies to the people in the city. They brought in food, medical supplies and many other items to keep Berlin running. During the year it was in action, the Western Allied air craft ran over 200,000 flights and delivered up 8,893 tonnes of essentials each day.',
        'On the 3 September 1939, England and France declared waron Germany. This was the beginning of the Second World War,a war no one thought would happen after the horror of the FirstWorld War. With this new war came new threats from above and new technology was needed. Enter the Spitfire and the Hurricane... both would be vital in protecting England from air attack.The Spitfire was produced in larger numbers than any otheraircraft before or since. The Hurricane was an equallyimpressive fighter and played a major part in achieving the victory of 1945.',
        'Prince Harry and Meghan Markle have chosen white garden roses, peonies and foxgloves for their wedding day. The royal couple plan to get married on Saturday 19 May at St George\'s Chapel in Windsor. Florist Philippa Craddock will create the floral displays for the special day, Kensington Palace said. Meghan Markle has said on social media in the past that peonies make her "endlessly happy".'
    ]
    text = random.choice(possibleTexts).lower()
    splitPoint = 0
    
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='green' )
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global labelRight
    labelRight = Label(root, text=text[splitPoint:],fg='grey')
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='green')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='red')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False
    
    amountWords = len(labelLeft.cget('text').split(' '))
    
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    ResultLabel.destroy()
    ResultButton.destroy()

    resetWritingLabels()

def addSecond():
    
    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    if writeAble:
        root.after(1000, addSecond)

resetWritingLabels()

root.mainloop()