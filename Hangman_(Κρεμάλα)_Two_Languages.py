import os
import csv
import msvcrt as m
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.scrolledtext import *
import random
from tkinter import messagebox

def main2(x):
    Frame2.grid_forget()
    global Frame3
    global language
    language=x
    Frame3=LabelFrame(root, bd=0, bg="#ffd480" )
    Frame3.grid(row=5, column=0, columnspan=51)     
    global tries
    tries=7
    global hits
    hits=0
    global choice
    choice=[]
    global usedLetter
    usedLetter=[]
    global button1
    global button2
    global button3
    global text1
    global text2
    global text3
    root.bind('<F11>', lambda event: game(7)) #restart game.
    root.bind('<Escape>', lambda event: root.destroy()) #exit game.
    if x=='GR':
        text1="Παίκτης εναντίον υπολογιστή"
        text2="Παίκτης εναντίον παίκτη"
        text3="Έξοδος από το παιχνίδι"
    elif x=='ENG':
        text1="Player   vs.   Computer"
        text2="Player   vs.   Player"
        text3="Exit Game"        
    button1=Button(Frame3, text=text1, padx=53, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(1))
    button1.grid(row=5, column=6, padx=80, pady=170)
    button2=Button(Frame3, text=text2, padx=70, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(2))
    button2.grid(row=5, column=9, padx=80, pady=170)
    button3=Button(Frame3, text=text3, padx=67, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(3))
    button3.grid(row=5, column=12, padx=80, sticky=E, pady=170)
    if x=='ENG':
        button1.config(padx=79)
        button2.config(padx=91)
        button3.config(padx=120)    

def main():
    global root
    root=Tk()
    root.config(background="#ffd480")  
    root.title("Serafina Panagiotaki - Παιχνίδι \"ΚΡΕΜΑΛΑ\" v. 2.1 - powered by Python v. 3.10.5") 
    root.state('zoomed')
    photo = PhotoImage(file = "hangman7.png") #window icon
    root.iconphoto(False, photo)
    root.option_add("*Button.Background", "#00334d") #attribute για όλα τα Buttons    
    root.option_add("*Button.Background", "#00334d") #attribute για όλα τα Buttons
    root.option_add("*Button.Foreground", "white")  #attribute για όλα τα Buttons
    root.option_add("*Button.cursor", "hand2")  #attribute για όλα τα Buttons, cursor="hand2" --> cursor: pointer
    pictures=['hangman0.jpg', 'hangman1.jpg', 'hangman2.jpg', 'hangman3.jpg', 'hangman4.jpg', 'hangman5.jpg', 'hangman6.jpg', 'hangman7.jpg']
    global Frame0
    Frame0=LabelFrame(root, bd=0, bg="#ffd480")
    Frame0.grid(row=0, column=0, columnspan=52)
    global Frame2
    Frame2=LabelFrame(root, bd=0, bg="#ffd480" )
    Frame2.grid(row=5, column=0, columnspan=52)   
    title0=Label(Frame0, text="Κρεμάλα (Hangman)", font="Arial, 60", fg="#00334d", bg="#ffd480") 
    title0.grid(row=0, column=0, columnspan=52, padx = 420, sticky = E + W)
    global title1
    title1=Label(Frame0, text="Βρες την κρυμμένη λέξη... και κέρδισε!", font="Arial, 20", fg="#004466", bg="#ffd480")
    title1.grid(row=3, column=0, columnspan=52, sticky=W+E, pady=0)
    image3 = Image.open("greek_flag.jpg")
    photo3 = ImageTk.PhotoImage(image3)    
    langGr=Button(Frame2, image = photo3, command=lambda: main2('GR'), borderwidth=0)
    langGr.grid(row=10, column=25, padx=100)
    langGr.image = photo3
    global Frame4
    Frame4=LabelFrame(Frame2, bd=0)
    Frame4.grid(row=5, column=0, columnspan=52, pady=80)
    grVersion=Label(Frame2, text="Ελληνικές λέξεις", fg="#00334d", bg="#ffd480", font=('Arial', 14))
    grVersion.grid(row=9, column=25, padx=60, sticky=S)
    image4 = Image.open("english_flag.jpg")
    photo4 = ImageTk.PhotoImage(image4)         
    langEng=Button(Frame2, image = photo4, command=lambda: main2('ENG'), borderwidth=0)
    langEng.grid(row=10, column=26)    
    langEng.image = photo4
    engVersion=Label(Frame2, text="English version", fg="#00334d", bg="#ffd480", font=('Arial', 14))
    engVersion.grid(row=9, column=26, padx=100, sticky=S)    
    root.mainloop()

def field():
    global length
    length=len(words[x][0])    
    for i in range(length):         
        global gramma
        gramma=Label(Frame1, text=guess[i], fg="#00334d", bg="#ffd480", font=("Arial", 22), padx=15)
        gramma.grid(row=15, column=1+i, pady=15)    
    for i in range(len(alphabet)):
        line=16+round(i/(len(alphabet)-1))
        global changeLine
        if language=='GR':
            changeLine=12
        elif language=='ENG':
            changeLine=13
        if i<changeLine:
            j=i
        else:
            j=i-changeLine
        global letter
        letter=Button(Frame1, text=alphabet[i], padx=25, pady=20, fg="#ffd480", bg="#00334d", bd=10, relief=RAISED, command=lambda i=i: check(alphabet[i]))
        letter.grid(row=line, column=j, padx=9, pady=10)        

def check(o):
    global message
    global count
    global hits
    global tries
    global choice
    global notification
    global gramma
    for i in range(length):
        gramma=Label(Frame1, text=guess[i], fg="#00334d", bg="#ffd480", font=("Arial", 20), padx=15)#, pady=15
        gramma.grid(row=15, column=1+i, pady=0)    
    if tries<7: #πατέντα, αν tries<7 σημαίνει πως ήδη έχει δοθεί από τον χρήστη γράμμα που δεν ανήκει στην λέξη και έχει εμφανιστεί από προηγουμένως μήνυμα (που εδώ το σβήνω).
        global notification1
        notification1.config(text="")
    count=0
    for j in range(length):
        if o==words[x][0][j]: #υπάρχει το γράμμα στην κρυμμένη λέξη.                        
            count=count+1;            
            if o not in choice: #σημαίνει πως δεν έχει ζητηθεί το συγκεκριμένο γράμμα άλλη φορά, επομένως το τοποθετούμε στην κρυμμένη λέξη.
                guess[j]=o;
                if language=='GR':
                    text1="Λέξη:"
                elif language=='ENG':
                    text1="Hidden word:"
                global leksi
                leksi=Label(Frame1, text=text1, fg="#00334d", bg="#ffd480", font=("Arial", 15), padx=10)
                leksi.grid(row=15, column=0, sticky=E, pady=0)
                for i in range(length):
                    gramma=Label(Frame1, text=guess[i], fg="#00334d", bg="#ffd480", font=("Arial", 20), padx=15)#, pady=15
                    gramma.grid(row=15, column=1+i, pady=0)                 
                hits=hits+1;
        else: #δεν υπάρχει το γράμμα στην κρυμμένη λέξη.
            if o in choice: #σημαίνει πως έχει ήδη ζητηθεί το συγκεκριμένο γράμμα και δεν υπάρχει στην λέξη, για αυτό και αυξάνει στην συνέχεια ο counter, ώστε όταν γίνει ο δικός του
                count=count+1; #έλεγχος λίγο πιο κάτω και βρεθεί μη μηδενικός, να μη χρεωθεί ως αποτυχία εκ νέου.               
                break
    if o not in choice:
        choice.append(o);
    if count==0:
        tries=tries-1;
        image0 = Image.open(pictures[7-tries])#αρχικά--> "hangman0.jpg", με κάθε αστοχία του παίκτη μειώνεται κατά ένα η μεταβλητή tries και αυξάνει το index της λίστας
        photo0 = ImageTk.PhotoImage(image0)    #pictures[], οπότε θα αλλάζει κάθε φορά η εικόνα μετά από αποτυχία.
        label0 = Label(Frame1, image = photo0, bd=0)
        label0.image1 = photo0
        label0.grid(row=5, column=3, columnspan=52)
    if tries==0:
        if language=='GR':
            messageFinal="Έχασες!!! Η κρυμμένη λέξη ήταν:\n\n"+words[x][0]
        elif language=='ENG':
            messageFinal="Ooops, you lost!!! The hidden word was:\n\n"+words[x][0]
        messagebox.showinfo('', messageFinal)       
    if hits==length:
        if language=='GR':
            messageFinal="Συγχαρητήρια!!! Τη βρήκες!!!"
        elif language=='ENG':
            messageFinal="Congratulations!!! You found it!!!"
        messagebox.showinfo('', messageFinal)
    elif tries>1:
        if language=='GR':
            message=str(tries)+" προσπάθειες απομένουν..."
        elif language=='ENG':
            message=str(tries)+" tries left..."            
    elif tries==1:
        if language=='GR':
            message="Μία προσπάθεια απομένει..."
        elif language=='ENG':
            message="One try left..."            
    global usedLetter
    if len(usedLetter)>0: #Αν έχει δοθεί νωρίτερα γράμμα από τον χρήστη, καθαρίζει το περιεχόμενο των γραμμάτων που εκτυπώνονται στην οθόνη για να προστεθεί η νέα επιλογή παρακάτω.    
        global notification2
        notification2.config(text="")
    epilogi=o
    if epilogi not in usedLetter:
        usedLetter.append(epilogi)
        usedLetter.sort()
        global usedLettersString          
        usedLettersString=""
        for epilogi in usedLetter:
            usedLettersString=usedLettersString+epilogi
            if epilogi<usedLetter[-1]:
                usedLettersString=usedLettersString+', '
    if language=='GR':
        text1="Γράμματα που χρησιμοποιήθηκαν:\n"
    elif language=='ENG':
        text1="Player\'s choices:\n"
    notification1=Label(Frame1, text=message, fg="#00334d", bg="#ffd480", font=("Arial", 15))
    notification1.grid(row=5, column=11, columnspan=52, sticky=W+E)
    notification2=Label(Frame1, text=text1+usedLettersString, fg="#00334d", bg="#ffd480", font=("Arial", 15))
    notification2.grid(row=6, column=11, columnspan=52, sticky=W+E)   
    count=0
    
def game(m): 
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    if m in [1, 2]:
        global Frame1   
        Frame1=LabelFrame(root, bd=0, bg="#ffd480",)
        Frame1.grid(row=5, column=0, columnspan=52, pady=15)
        global alphabet
        if language=='GR':
            alphabet=['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
            text1="Νέο παιχνίδι"
            text2="Έξοδος από το παιχνίδι"
        elif language=='ENG':
            alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            text1="New Game"
            text2="Exit Game"
        global back
        global exitButton
        back=Button(Frame1, text=text1, padx=107, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(4))
        back.grid(row=3, column=0, columnspan=52, sticky=W)
        exitButton=Button(Frame1, text=text2, padx=109, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(6))
        exitButton.grid(row=3, column=11, columnspan=5)
        if language=='GR':
            exitButton.config(padx=67)
    if m==1: #Παίκτης εναντίον υπολογιστή]
        global pictures
        pictures=['hangman0.jpg', 'hangman1.jpg', 'hangman2.jpg', 'hangman3.jpg', 'hangman4.jpg', 'hangman5.jpg', 'hangman6.jpg', 'hangman7.jpg']
        image0 = Image.open(pictures[0])
        photo0 = ImageTk.PhotoImage(image0)    
        label0 = Label(Frame1, image = photo0, bd=0)
        label0.image1 = photo0
        label0.grid(row=5, column=3, columnspan=52, pady=0)        
        global words
        words=[]
        if language=='GR':
            with open("greek.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter=',')
                for row in ro:
                    words.append(row)
        elif language=='ENG':
            with open("english.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter=',')
                for row in ro:
                    words.append(row)
        global choice
        choice=[]
        global x
        x=random.randrange(0, len(words))
        global length
        length=len(words[x][0])
        global guess
        guess=[]
        for i in range(length):
            guess.append("___")
        if language=='GR':
            text1="Λέξη:"
        elif language=='ENG':
            text1="Hidden word:"
        leksi=Label(Frame1, text=text1, fg="#00334d", bg="#ffd480", font=("Arial", 15), padx=10)
        leksi.grid(row=15, column=0, sticky=E)
        for i in range(length):
            gramma=Label(Frame1, text=guess[i], fg="#00334d", bg="#ffd480", font=("Arial", 22), padx=15)#, pady=15
            gramma.grid(row=15, column=1+i, pady=10)
        for i in range(len(alphabet)):
            line=16+round(i/(len(alphabet)-1))
            global changeLine
            if language=='GR':
                changeLine=12
            elif language=='ENG':
                changeLine=13
            if i<changeLine:
                j=i
            else:
                j=i-changeLine
            global letter
            letter=Button(Frame1, text=alphabet[i], padx=25, pady=20, fg="#ffd480", bg="#00334d", bd=10, relief=RAISED, command=lambda i=i: check(alphabet[i]))
            letter.grid(row=line, column=j, padx=9, pady=10)        
    elif m==2: #Παίκτης εναντίον παίκτη
        global playerWord
        global player
        global playerWord
        if language=='GR':
            text1="Κρυμμένη λέξη:"
            text2="Υποβολή"
        elif language=='ENG':
            text1="Hidden word:"
            text2="Submit"
        player=Label(Frame1, text=text1, fg="#00334d", bg="#ffd480", font=("Arial", 15))
        player.grid(row=10, column=1, padx=20, pady=150)
        playerWord=Entry(Frame1, width=50, fg="#ffd480", bg="#00334d", font=("Arial", 15))
        playerWord.config(show="*")
        playerWord.grid(row=10, column=2, pady=150)
        global submit
        submit=Button(Frame1, text=text2, padx=100, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(5))
        submit.grid(row=10, column=3, padx=20)
        if language=='ENG':
            submit.config(padx=120)
    elif m==3: #Έξοδος από το παιχνίδι στην αρχή.
        Frame3.grid_forget()
        if language=='GR':
            text1="Ευχαριστούμε πολύ που χρησιμοποιήσατε αυτή την εφαρμογή!"
            text2="Κλείσιμο παραθύρου"
            text3="Επανεκκίνηση"
        elif language=='ENG':
            text1="Thank you for using this application!"
            text2="Close window"
            text3="Restart Game"
        hello1=Label(Frame0, font=("Arial", 15), text=text1, fg="#00334d", bg="#ffd480")
        hello1.grid(row=10, column=0, columnspan=52, pady=0, sticky=S)
        hello2=Label(Frame0, font=("Arial", 12), text="Programmed, designed and developed by Shery Panagiotaki, @copyright 2022", fg="#00334d", bg="#ffd480")
        hello2.grid(row=11, column=0, columnspan=52, pady=10, sticky=N)        
        image4 = Image.open("shery_pic_2.jpg")#ή "shery_pic_3.jpg"
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(Frame0, image = photo4, bd=0)
        label4.image = photo4
        label4.grid(row=9, column=0, columnspan=52, pady=30)
        restartButton=Button(Frame0, text=text3, padx=100, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: game(7))
        restartButton.grid(row=16, column=25, pady=20, padx=65)
        exitButton=Button(Frame0, text=text2, padx=76, pady=20, bd=10, font=("Arial", 12), relief=RAISED, command=lambda: root.destroy())
        exitButton.grid(row=16, column=26, pady=20, padx=65)
        if language=='ENG':
            exitButton.config(padx=100)
        #root.bind('<F11>', lambda event: game(7))
    elif m==4: #Επιστροφή στο κεντρικό μενού.
        root.destroy()
        main()
    elif m==5: #Έναρξη παιχνιδιού player vs. player μετά από την είσοδο της κρυμμένης λέξης.
        global entry
        global newWord
        entry=[]
        words=[]
        newWord=playerWord.get()
        newWord.strip()
        newWord=newWord.upper()
        entry.append(newWord)
        words.append(entry)
        x=0                
        pictures=['hangman0.jpg', 'hangman1.jpg', 'hangman2.jpg', 'hangman3.jpg', 'hangman4.jpg', 'hangman5.jpg', 'hangman6.jpg', 'hangman7.jpg']
        image0 = Image.open(pictures[0])#"hangman0.jpg"
        photo0 = ImageTk.PhotoImage(image0)    
        label0 = Label(Frame1, image = photo0, bd=0)
        label0.image1 = photo0
        label0.grid(row=5, column=3,columnspan=52, pady=0)
        temp=[]
        if language=='GR':
            with open("greek.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter=',')
                for row in ro:
                    temp.append(row)
        elif language=='ENG':
            with open("english.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter=',')
                for row in ro:
                    temp.append(row)            
            final=""
            final2=[]
            for character in newWord:
                if not (character==','): #απάλειψη του ','.
                    final=final+character #concatenate, η λέξη γίνεται string και καταχωρείται αμέσως μετά στη Βάση Δεδομένων για μελλοντική χρήση (computer vs. player).
            final2.append(final) #append σε λίστα
            if not final2 in temp: #έλεγχος αν η λέξη που έδωσε ο χρήστης υπάρχει ήδη στη Βάση Δεδομένων του προγράμματος.
                temp.append(final2) #append σε λίστα (η temp[] είναι λίστα που περιλαμβάνει λίστες).
                if language=='GR':
                    with open("greek.csv", "w", encoding="utf-8", newline="") as file:
                        wo=csv.writer(file)
                        for row in temp:
                            wo.writerow(row)
                elif language=='ENG':
                    with open("english.csv", "w", encoding="utf-8", newline="") as file:
                        wo=csv.writer(file)
                        for row in temp:
                            wo.writerow(row)                    
        submit.grid_forget()
        player.grid_forget()
        playerWord.grid_forget()
        length=len(words[x][0])
        guess=[]
    elif m==6: #Έξοδος από το παιχνίδι μετά την είσοδο του χρήστη.
        Frame1.grid_forget()
        Frame3.grid(row=5, column=0)
        Frame3.grid(row=5, column=0)       
        game(3)
    elif m==7: #επανέναρξη του παιχνιδιού (το έχω συνδέσει και με το <F11>.
        root.destroy()
        main()

main()
