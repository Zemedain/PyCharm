from arithmetic import *
import tkinter as tk

app = tk.Tk()

app.geometry("850x500")
app.title("My calculator")

text = tk.Label(app, text = "Calculator", font = ("Arial", 18))
text.pack(padx=20, pady=30)

textbox = tk.Text(app, height = 3, font =("Arial", 15))
textbox.pack(padx=200, pady=20)
butframe = tk.Frame(app)
butframe.columnconfigure(0, weight=1)
butframe.columnconfigure(1, weight=1)
butframe.columnconfigure(2, weight=1)

btn1 = tk.Button(butframe, text="1", font = ("Arial", 16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(butframe, text="2", font = ("Arial", 16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(butframe, text="3", font = ("Arial", 16))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(butframe, text="4", font = ("Arial", 16))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(butframe, text="5", font = ("Arial", 16))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(butframe, text="6", font = ("Arial", 16))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(butframe, text="7", font = ("Arial", 16))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(butframe, text="8", font = ("Arial", 16))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(butframe, text="9", font = ("Arial", 16))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn10 = tk.Button(butframe, text="0", font = ("Arial", 16))
btn10.grid(row=2, column=2, sticky=tk.W+tk.E)

btn11 = tk.Button(butframe, text="(", font = ("Arial", 16))
btn11.grid(row=2, column=2, sticky=tk.W+tk.E)

btn12 = tk.Button(butframe, text=")", font = ("Arial", 16))
btn12.grid(row=2, column=2, sticky=tk.W+tk.E)

butframe.pack(fill="x")

app.mainloop()