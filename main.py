from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cipher import *
from emailSender import *

global email
email = ""

def mainMenu():
    #creating the menu frame
    menuFrame = Frame()

    #creating main title
    mainTitle = Label(menuFrame, text="Welcome to the Bean and Brew app", font=("Montserrat", 15))
    mainTitle.pack(pady=20)

    mainSubtitle = Label(menuFrame, text="Enjoy your stay on our app")
    mainSubtitle.pack(pady=10)

    menuGridFrame = Frame()
    
    bookTableButton = Button(menuGridFrame, text="Book a Table", command=lambda: tableBooking(menuFrame, menuGridFrame), width=20)
    bookTableButton.grid(row = 0, column = 0, padx=20, pady=20)

    preOrderButton = Button(menuGridFrame, text="Pre Order Coffee", width=20)
    preOrderButton.grid(row = 0, column = 1, padx=20, pady=20)

    bookBakingButton = Button(menuGridFrame, text="Book Baking Lessons", width=20)
    bookBakingButton.grid(row = 1, column = 0, padx=20, pady=20)

    POGoodsButton = Button(menuGridFrame, text="Pre Order Baked Goods", width=20)
    POGoodsButton.grid(row = 1, column = 1, padx=20, pady=20)

    customiseButton = Button(menuGridFrame, text="Customise Hamper", width=20)
    customiseButton.grid(row = 2, column = 0, padx=20, pady=20)

    postingButton = Button(menuGridFrame, text="Posts", width=20, command=lambda: rateMyCake(menuFrame, menuGridFrame))
    postingButton.grid(row = 2, column = 1, padx=20, pady=20)

    exitButton = Button(menuGridFrame, text="Exit", command=exit, width=20)
    exitButton.grid(row = 3, column = 0, columnspan = 2, padx=20, pady=20)
    
    #packing the entire frame
    menuFrame.pack()
    menuGridFrame.pack()
    
#==================== Social media ===========================#
def rateMyCake(frame1, frame2):
    frame1.destroy()
    frame2.destroy()

    def _on_mousewheel(event):
        mainCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    mainFrame = Frame()
    mainFrame.pack(fill=BOTH, expand=1)

    mainCanvas = Canvas(mainFrame)
    mainCanvas.pack(side=LEFT, fill=BOTH, expand=1)
    mainCanvas.bind_all("<MouseWheel>", _on_mousewheel)

    scrollbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=mainCanvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    mainCanvas.configure(yscrollcommand=scrollbar.set)
    mainCanvas.bind("<Configure>", lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox("all")))

    secondFrame = Frame(mainCanvas)

    mainCanvas.create_window((0,0), window=secondFrame, anchor="nw")
    totalCakes = 0
    run = True
    
    while run:
        for i in range(10):
            cakeName = Label(secondFrame, text=f"Cake {totalCakes + i}")
            cakeName.pack(padx=20, pady=10)

        totalCakes +=  10
        waitVar = IntVar()
        moreCakesButton = Button(secondFrame, text="View more cakes", command=lambda: waitVar.set(1))
        moreCakesButton.pack(padx=20, pady=20)
        secondFrame.pack()
        moreCakesButton.wait_variable(waitVar)
        print("RUNNING")

#================= Table Booking System ======================#   
def tableBooking(frame1, frame2):
    frame1.destroy()
    frame2.destroy()
    
    tableTitleFrame = Frame()
    tableFrame = Frame()

    mainTitle = Label(tableTitleFrame, text="Bean and Brew", font=("Montserrat", 15))
    mainTitle.pack(pady=20)

    mainSubtitle = Label(tableTitleFrame, text="Book a table at one of resturants. First pick the location of the branch you would like to book at", wraplength=500, justify="center")
    mainSubtitle.pack(pady=10)

    harrogateButton = Button(tableFrame, text="Harrogate", command= lambda: tableBookingSelection(tableTitleFrame, tableFrame, "Harrogate"))
    harrogateButton.grid(row=0, column=0, padx=20, pady=20)

    LeedsButton = Button(tableFrame, text="Leeds", command= lambda: tableBookingSelection(tableTitleFrame, tableFrame, "Leeds"))
    LeedsButton.grid(row=0, column=1, padx=20, pady=20)

    knaresButton = Button(tableFrame, text="Knaresborough", command= lambda: tableBookingSelection(tableTitleFrame, tableFrame, "Knaresborough"))
    knaresButton.grid(row=0, column=2, padx=20, pady=20)

    tableTitleFrame.pack()
    tableFrame.pack()

def tableBookingSelection(frame1, frame2, selection):
    frame1.destroy()
    frame2.destroy()
    
    tableTitleFrame = Frame()
    tableFrame = Frame()
    
    mainTitle = Label(tableTitleFrame, text="Bean and Brew", font=("Montserrat", 15))
    mainTitle.pack(pady=20)

    mainSubtitle = Label(tableTitleFrame, text=f"Pick a table for when you come to visit us in {selection}", wraplength=500, justify="center")
    mainSubtitle.pack(pady=10)       

            
    tables = []
    for i in range(1, 21):
        tables.append(f"Table {i}")

    rowCount = 0
    columnCount = 0

    for tableNum in tables:
        tableButton = Button(tableFrame, text=tableNum, command= lambda table=tableNum:tablePicked(selection, table, tableTitleFrame, tableFrame)) 
        tableButton.grid(row = rowCount, column = columnCount, padx=20, pady=20)
        columnCount += 1
        if columnCount == 4:
            columnCount = 0
            rowCount += 1

    tableTitleFrame.pack()
    tableFrame.pack()

def tablePicked(branch, table, frame1, frame2):
    frame1.destroy()
    frame2.destroy()

    tableTitleFrame = Frame()
    
    mainTitle = Label(tableTitleFrame, text="Bean and Brew", font=("Montserrat", 15))
    mainTitle.pack(pady=20)

    mainSubtitle = Label(tableTitleFrame, text=f"Amazing, you have booked {table} at our {branch} branch. Please check you emails for a confirmation letter.", wraplength=500, justify="center")
    mainSubtitle.pack(pady=10)

    waitVar = IntVar()
    mainMenuButton = Button(tableTitleFrame, text="Back to the main menu", command= lambda: waitVar.set(1), width=20)
    mainMenuButton.pack(pady=10)

    details = {"branch": branch,
               "tableNum": table}
    
    tableTitleFrame.pack()
    sendEmail(email, details)

    mainMenuButton.wait_variable(waitVar)

    tableTitleFrame.destroy()
    mainMenu()

#=============================================================#
def loginScreen(checkVar, frame): 
    if checkVar != "invalidDetails":
        loginTitleFrame = Frame()
        loginFrame = Frame()
        
        #creating main title
        mainTitle = Label(loginTitleFrame, text="Welcome to the Bean and Brew app", font=("Montserrat", 15))
        mainTitle.pack(pady=20)

        mainSubtitle = Label(loginTitleFrame, text="Enter your details then either login or sign up")
        mainSubtitle.pack(pady=10)

        emailLabel = Label(loginFrame, text="Email")
        emailLabel.grid(row=0, column=0, padx=20, pady=20)

        emailEntry = Entry(loginFrame, text=0, width=25)
        emailEntry.grid(row=0, column=1, padx=20, pady=20)

        passwordLabel = Label(loginFrame, text="Password")
        passwordLabel.grid(row=1, column=0, padx=20, pady=20)

        passwordEntry = Entry(loginFrame, text=1, width=25, show="*")
        passwordEntry.grid(row=1, column=1, padx=20, pady=20)

        loginButton = Button(loginFrame, text="Login", width=30, command=lambda: loginCheck(emailEntry, passwordEntry, loginTitleFrame, loginFrame))
        loginButton.grid(row=2, column=0, columnspan = 2, padx=20, pady=20)

        signupLabel = Label(loginFrame, text="Or you can sign up here")
        signupLabel.grid(row=3, column=0, columnspan = 2, padx=20, pady=20)

        signupButton = Button(loginFrame, text="Signup", width=30, command=lambda: signupScreen(emailEntry, passwordEntry, loginTitleFrame, loginFrame))
        signupButton.grid(row=4, column=0, columnspan = 2, padx=20, pady=20)

    if checkVar == "getDetails":
        return emailEntry, passwordEntry, loginTitleFrame, loginFrame
            
    elif checkVar == "invalidDetails":
        warningLabel = Label(frame, text="Invalid details, please try again")
        warningLabel.grid(row=5, column=0, columnspan = 2, padx=20, pady=20)

    else:
        loginTitleFrame.pack()
        loginFrame.pack()
        


def loginCheck(emailEntry, passwordEntry, loginTitleFrame, loginFrame):
    global email
    email = emailEntry.get()
    password = passwordEntry.get()
    typeCheck = "login"
    if checkDatabase(typeCheck, email, password):
        loginTitleFrame.destroy()
        loginFrame.destroy()
        mainMenu()
    else:
        checkVar = "invalidDetails"
        loginScreen(checkVar, loginFrame)
        

def signupScreen(emailEntry, passwordEntry, loginTitleFrame, loginFrame):
    global email
    email = emailEntry.get()
    password = passwordEntry.get()
    if "@" not in email or password == "":
        checkVar = "invalidDetails"
        loginScreen(checkVar, loginFrame)
    else:
        typeCheck = "signup"
        if checkDatabase(typeCheck, email, password):
            loginTitleFrame.destroy()
            loginFrame.destroy()
            
            f = open("userDetails.txt", "a")
            f.write(encrypt(email))
            f.write("\n")
            f.write(encrypt(password))
            f.write("\n")
            f.close()
            mainMenu()
        else:
            checkVar = "invalidDetails"
            loginScreen(checkVar, loginFrame)

def checkDatabase(typeCheck, email, password):
    f = open("userDetails.txt", "r")
    email = encrypt(email)
    password = encrypt(password)
    if typeCheck == "signup":
        emailUsed = False
        for line in f.readlines():
            line = line.strip('\n')
            if line == email:
                emailUsed = True
                break
        if emailUsed:
            return False
        else:
            return True
        
    elif typeCheck == "login":
        checkNext = False
        for line in f.readlines():
            line = line.strip('\n')
            if line == email:
                checkNext = True
            elif checkNext == True and line.strip('\n') == password:
                    f.close()
                    return True
        

if __name__ == "__main__":
    w = Tk()
    w.title("Bean and Brew")
    w.option_add("*Font", "Montserrat")
    w.geometry("800x600")
    w.resizable(False, False)

    style = Style()
    style.configure('TButton', font =('Montserrat', 12), borderwidth = '4')
    
    loginScreen(True, None)
    w.mainloop()
