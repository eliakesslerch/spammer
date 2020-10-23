from tkinter import *
from tkinter import messagebox
import keyboard
import webbrowser
import time
master = Tk()
master.title("Spammer2.0 v1.1")
menu = Menu(master)
datei_menu = Menu(menu, tearoff=0)
help_menu = Menu(menu, tearoff=0)
def site():
    webbrowser.open('https://github.com/eliakesslerch/spammer')
def help():
	m_text = "\
1. In Textfeld Nachricht eingeben \n\
2. Anzahl auswählen\n\
3. Delay zwischen Nachrichten eingeben \n\
4. In Chat-Textfeld klicken\n\
5. Wartezeit eintippen\n\
6. Spammen!\n\
"
	messagebox.showinfo(message=m_text, title = "Hilfe")
def spam():
 count = 0
 waittime = int((wait.get()))
 number = int((countfield.get())) 
 time.sleep(waittime)
 while count < int(number):
     textcontent = ((text.get()))
     keyboard.write(textcontent)
     keyboard.press_and_release("enter")
     count = count + 1
Button(master, text='Spam!', command=spam).grid(row=8, column=1, sticky=W, pady=4)
text = Entry(master)
Label(master, text="Text: ").grid(row=0)
text.grid(row=0, column=1)
wait = Entry(master)
Label(master, text="Wartezeit: ").grid(row=3, column=0)
wait.grid(row=3, column=1)
wait.insert(0, "3")
countfield = Entry(master)
Label(master, text="Anzahl: ").grid(row=4, column=0)
countfield.grid(row=4, column=1)
countfield.insert(0, "20")
datei_menu.add_command(label="Spam", command=spam)
datei_menu.add_command(label="Website", command=site)
help_menu.add_command(label="Hilfe", command=help)
menu.add_cascade(label="Datei", menu=datei_menu)
menu.add_cascade(label="Hilfe", menu=help_menu)
master.config(menu=menu)
master.mainloop()