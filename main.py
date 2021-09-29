from tkinter import *
from tkinter.ttk import *

 
def mainMenu():
    #creating the menu frame
    menuFrame = Frame()

    #creating main title
    mainTitle = Label(menuFrame, text="Welcome to the Bean and Brew app", font=("Montserrat", 15))
    mainTitle.pack(pady=20)

    mainSubtitle = Label(menuFrame, text="Enjoy your stay on our app")
    mainSubtitle.pack(pady=10)

    menuGridFrame = Frame()
    
    bookTableButton = Button(menuGridFrame, text="Book a Table", width=20)
    bookTableButton.grid(row = 0, column = 0, padx=20, pady=20)

    preOrderButton = Button(menuGridFrame, text="Pre Order Coffee", width=20)
    preOrderButton.grid(row = 0, column = 1, padx=20, pady=20)

    bookBakingButton = Button(menuGridFrame, text="Book Baking Lessons", width=20)
    bookBakingButton.grid(row = 1, column = 0, padx=20, pady=20)

    POGoodsButton = Button(menuGridFrame, text="Pre Order Baked Goods", width=20)
    POGoodsButton.grid(row = 1, column = 1, padx=20, pady=20)

    customiseButton = Button(menuGridFrame, text="Customise Hamper", width=20)
    customiseButton.grid(row = 2, column = 0, padx=20, pady=20)

    postingButton = Button(menuGridFrame, text="Posts", width=20)
    postingButton.grid(row = 2, column = 1, padx=20, pady=20)

    exitButton = Button(menuGridFrame, text="Exit", command=exit, width=20)
    exitButton.grid(row = 3, column = 0, columnspan = 2, padx=20, pady=20)
    
    #packing the entire frame
    menuFrame.pack()
    menuGridFrame.pack()
    


def loginScreen(checkVar, frame): 
    if checkVar != "invalidDetails":
        loginTitleFrame = Frame(w)
        loginFrame = Frame(w)
        
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

        loginButton = Button(loginFrame, text="Login", width=30, command=loginCheck)
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
        


def loginCheck():
    emailEntry, passwordEntry, loginTitleFrame, loginFrame = loginScreen(checkVar = "getDetails")
    email = emailEntry.get()
    password = passwordEntry.get()
    typeCheck = "login"
    if checkDatabase(typeCheck, email, password):
        mainMenu()
    else:
        None
        

def signupScreen(emailEntry, passwordEntry, loginTitleFrame, loginFrame):
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
            mainMenu()
        else:
            checkVar = "invalidDetails"
            loginScreen(checkVar, loginFrame)

def checkDatabase(typeCheck, email, password):
    f = open("userDetails.txt", "r+")
    if typeCheck == "signup":
        counter = -1
        for line in f.readlines():
            counter =+ 1
            line = line.strip('\n')
            if line == email:
                print(f.readline(counter+1).strip('\n'))
                print(password)
                if f.readline(counter+1).strip('\n') == password:
                    return True
        

if __name__ == "__main__":
    w = Tk()
    w.title("Bean and Brew")
    w.option_add("*Font", "Montserrat")
    w.geometry("600x600")
    w.resizable(False, False)

    style = Style()
    style.configure('TButton', font =('Montserrat', 12), borderwidth = '4')
    
    loginScreen(True, None)
    
    w.mainloop()
