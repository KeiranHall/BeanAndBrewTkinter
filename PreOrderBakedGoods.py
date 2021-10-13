from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

#Initialising the root
root=Tk()

#Main subroutine
def OrderBakedGoodsMain(root):
    #Setting the windows dimensions
    root.title("Pre-order baked goods")
    root.geometry("300x310")

    #Defining the list that stores added content
    mainList=[]

    #Initialising the Frames
    frame=Frame()
    frame2=Frame()
    frame3=Frame()

    #Creating a title
    title=Label(frame,text="Select a baked good and quantity")
    title.pack(pady=10)

    #Adding items and respective price into a dictonary
    dropdownOptions={
        'Item 1 - £2.00':2.00,
        'Item 2 - £1.89':1.89,
        'Item 3 - £2.15':2.15,
        'Item 4 - £1.50':1.50,
        'Item 5 - £3.00':3.00
    }
    #Defining the varaiables for the dropdown menu
    clicked=StringVar()
    keys=dropdownOptions.keys()

    #Defining and packing the dropdown menu
    dropdown=OptionMenu(frame,clicked,list(keys)[0],*dropdownOptions)
    dropdown.pack(padx=15,pady=10,side=LEFT)

    #Defining and packing the spinbox
    spin=Spinbox(frame,from_=1,to=10,width=3,
                 font=Font(size=11))
    spin.pack(padx=5,pady=10,side=LEFT)
    spin.set(1)

    #Adding a wait variable and defining the add button
    waitVar=IntVar()
    add=Button(frame2,text="Add",command=lambda:waitVar.set(1))
    add.pack(padx=5,pady=10,side=LEFT)

    #Defining the Next or Submit button
    submit=Button(frame2,text="Next",command=lambda:OrderBakedGoodsReceipt(frame,frame2,frame3,mainList))
    submit.pack(pady=10,padx=5)

    #Defining and packing the outputBox
    outputBox=Text(frame3,width=30,height=10)
    outputBox.pack()

    #Packing the frames so everything displays
    frame.pack()
    frame2.pack()
    frame3.pack()

    #This loop waits for the add button to be pressed
    while True:
        add.wait_variable(waitVar)
        quantity=spin.get()
        item=clicked.get()
        #Then does some error checking / handling to make sure its usable and
        #if it is, it adds it to the mainList
        try:
            if int(quantity) in range(1,11):
                mainList.append(item)
                mainList.append(quantity)
                mainList.append("{:.2f}".format(dropdownOptions[item]*float(quantity)))
        except:
            pass
        #Once added to the list, the added items are displayed to a text box.
        outputBox.delete('1.0',END)
        outputBox.insert(END,"Item".ljust(11)+"Quantity".ljust(12)+"Total\n")
        maxLength=int(len(mainList))
        #This text box rebuilds it's self everytime to avoid human error such
        #as deleting the content
        if maxLength != 0:
            for i in range(0,maxLength,3):
                outputBox.insert(END,"{:<11}{:<12}£{:<}\n".format((mainList[i])[:6],mainList[i+1],mainList[i+2]))
        
#Receipt subroutine
def OrderBakedGoodsReceipt(a,b,c,mainList):
    #The previous frames are passed in and deleted to clear the screen
    a.destroy()
    b.destroy()
    c.destroy()

    #A new frame is defined
    frame=Frame()

    #A new title is made and packed
    title=Label(frame,text="Receipt")
    title.pack(pady=15)

    #New output box is defined and packed
    outputBox=Text(frame,width=30,height=15)
    outputBox.pack()

    #Formatted titles are added to the output box
    outputBox.insert(END," "*12+"Reciept\n\n")
    outputBox.insert(END,"Item".ljust(11)+"Quantity".ljust(13)+"Total\n")

    #Adds up the total of all the items and makes adjustments to the spacing
    #to avoid the total going of the edge
    if len(mainList) > 0:
        total=float(0)
        for i in range(0,len(mainList),3):
            total=float(total)+float(mainList[i+2])
            total="{:.2f}".format(total)
        totalSpacing=26
        if len(total) >= 6:
            totalSpacing=24
        elif len(total) >=5:
            totalSpacing=25

        #Builds the output box back with all the content within
        for i in range(0,len(mainList),3):
            outputBox.insert(END,"{:<11}{:<13}£{:<}\n".format((mainList[i])[:6],mainList[i+1],mainList[i+2]))
        outputBox.insert(END,"\n".ljust(totalSpacing)+"Total")
        outputBox.insert(END,"\n".ljust(totalSpacing)+"£{}".format(total))

    #Packs the frame so it can be outputted
    frame.pack()

#Calls the main function
OrderBakedGoodsMain(root)
