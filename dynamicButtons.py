import tkinter as tk
my_w = tk.Tk()
my_w.geometry("200x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str, width=10 )
l1.grid(row=0,column=1,columnspan=5) 

def show_lan(my_language):
    my_str.set(my_language)

list_languages = ("PHP","Python","HTML","Tkinter")
var = 0


for language in list_languages:
    btn = tk.Button(my_w, text=language, command=lambda lan=language:show_lan(lan))
    btn.grid(row=1,column=var)
    var += 1

root.mainloop()
