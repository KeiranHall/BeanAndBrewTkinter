from tkinter import *
from tkinter import ttk

w = Tk()
w.title("Scrollbar")
w.geometry("500x400")

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

for i in range(15):
    Button(secondFrame, text=f"Button {i} YO YO").pack(padx=20, pady=20)

