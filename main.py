import time
from tkinter import *
import pyautogui
from PIL import Image,ImageTk

#Boxen
root = Tk()

root.title("Adriano_Banano")
root.geometry("366x200")
root.config(bg="gray")

#Bilde





Rute1 = LabelFrame(root, text="Bruker 1 (Tre Sekunder)", padx=35,pady=10, bg="gray", fg="blue")
Rute1.place(x=10,y=10)


Rute2 = LabelFrame(root, text="Bruker 2 (Alt Tab)", padx=35,pady=10, bg="gray", fg="blue")
Rute2.place(x=10,y=100)

#Skrift1
skrivP1 = Label(Rute1, text="Passord: ", bg="gray")
skrivP1.grid(row=1, column=0)

skrivB1 = Label(Rute1, text="Brukernavn: ", bg="gray")
skrivB1.grid(row=0,column=0)




#input1
passord1 = Entry(Rute1)
passord1.grid(row=1,column=1)

Brukernavn1 = Entry (Rute1)
Brukernavn1.grid(row=0, column=1)


#enterboox1
enter1 = IntVar()

e1 =Checkbutton(Rute1, text="ENTER", variable=enter1, bg="gray")
e1.grid(row=0, column=2)
name = enter1



#skriv 1
def myClick():
    if enter1.get() == 1:
        time.sleep(3)
        pyautogui.write(Brukernavn1.get())
        pyautogui.press("enter")
        pyautogui.write(passord1.get())
        pyautogui.press("enter")
    else:
        time.sleep(3)
        pyautogui.write(Brukernavn1.get())
        pyautogui.press("tab")
        pyautogui.write(passord1.get())
        pyautogui.press("enter")
myButton1 = Button(Rute1, text="Skriv1", command=myClick, fg="green", padx=20)
myButton1.grid(row=1,column=2)


#Skrift2
skrivP2 = Label(Rute2, text="Passord: ", bg="gray")
skrivP2.grid(row=1, column=0)

skrivB2 = Label(Rute2, text="Brukernavn: ", bg="gray")
skrivB2.grid(row=0,column=0)



#input2
passord2 = Entry(Rute2)
passord2.grid(row=1, column=2)

Brukernavn2 = Entry(Rute2)
Brukernavn2.grid(row=0, column=2)

#enterboox
enter2 = IntVar()

e2 =Checkbutton(Rute2, text="ENTER", variable=enter2,bg="gray")
e2.grid(row=0, column=3)
name = enter2



#skriv 2
def myClick():
    if enter2.get() == 1:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")
        pyautogui.write(Brukernavn2.get())
        pyautogui.press("enter")
        pyautogui.write(passord2.get())
        pyautogui.press("enter")
    else:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")
        pyautogui.write(Brukernavn2.get())
        pyautogui.press("tab")
        pyautogui.write(passord2.get())
        pyautogui.press("enter")
myButton2 = Button(Rute2, text="Skriv2", command=myClick, fg="green", padx=20,)
myButton2.grid(row=1, column=3)

root.mainloop()