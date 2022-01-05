import tkinter as tk
from tkinter import font
print("Welcome Flag maker by Python")
user = input("1 Japan 2 the US 3 France")
user = int(user)
root = tk.Tk()

root.geometry("900x600")
canvas = tk.Canvas(root, background="#fff", width=900, height=600)
canvas.pack()

if (user == 1):
    canvas.create_oval(300, 150,600, 450,fill="red",outline="white")
    root.mainloop()

if (user == 2):
    font= font.Font(size=28)
    y:int = 5
    for l in range (8):
        n:int = -42

        for i in range(9):   
            n = n +  44
            n = str(n)
            name = "label" + n
            name = tk.Label(root, text="★",bg="#00205B",fg="white",font=font)
            n = int(n)
            name.place(x=n, y=y)
        y += 40
        #print(y)

    canvas.create_line(0, 15,
                    400, 15,width=660,fill="#00205B")

    y:int = 15
    for i in range(9):
        canvas.create_line(400, y,
                    900, y,width=20,fill="red")
        y+=40
    y = 375
    for i in range(6):
        canvas.create_line(0, y,
                        900, y,width=20,fill="red") 
        y += 40                          
    root.mainloop()
    
if (user == 3):
    canvas.create_line(150, 0,150, 600,width=300,fill="blue")
    canvas.create_line(450, 0, 450, 600,width=300,fill="white")
    canvas.create_line(750, 0, 750, 600,width=300,fill="red")
    root.mainloop()

