import tkinter as tk
from math import sqrt

root = tk.Tk()
root.title("Collision Simulator")
root.geometry("600x600")

mass1 = 0
mass2 = 0
velocity1 = 0
velocity2 = 0
momentum = 0
ke = 0
error = 0

def start():
    global velocity1, velocity2, mass1, mass2
    global momentum, ke
    global canvas
    global object1, object2
    global error
    global warning

    try:
        mass1 = float(entry1.get())
        mass2 = float(entry2.get())
        velocity1 = float(entry3.get())
        velocity2 = float(entry4.get())
    except:
        if not error:
            warning = tk.Label(root, text="Please enter a number between 0 and 15 for masses and between -15 and 15 for velocities", font = ("Arial", 16), wraplength = 400)
            warning.pack()
            error = 1
        return

    if 0 >= mass1 or mass1 >= 15 or 0 > mass2 or mass2 > 15 or -15 > velocity1 or velocity1> 15 or -15 > velocity2 or velocity2> 15:
        if not error:
            warning = tk.Label(root,text="Please enter a number between 0 and 15 for masses and between -15 and 15 for velocities",font=("Arial", 16), wraplength=400)
            warning.pack()
            error = 1
        return

    try:
        warning.destroy()
    except:
        pass


    momentum = 0.5*(mass1*velocity1 + mass2*velocity2)
    ke = 0.5*(mass1*velocity1*velocity1 + mass2*velocity2*velocity2)


    frame1.destroy()

    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()

    canvas.create_rectangle(0, 500, 600, 600, fill = "black")

    object2 = canvas.create_rectangle(500 -10*mass2, 500 - 10*mass2, 500, 500, fill = "gray")

    object1 = canvas.create_rectangle(100 + 10*mass1, 500 - 10*mass1, 100, 500, fill = "gray")

    move()

def wall_check():
    global velocity1, velocity2
    object1_x1, object1_y1, object1_x2, object1_y2 = canvas.coords(object1)
    object2_x1, object2_y1, object2_x2, object2_y2 = canvas.coords(object2)

    if object1_x1 <=10 or object1_x2 >= 590:
        velocity1 *= -1

    if object2_x1 <=10 or object2_x2 >= 590:
        velocity2 *= -1

def collision_check():
    global velocity1, velocity2, mass1, mass2
    object1_x1, object1_y1, object1_x2, object1_y2 = canvas.coords(object1)
    object2_x1, object2_y1, object2_x2, object2_y2 = canvas.coords(object2)

    if object2_x2 >= object1_x1 >= object2_x1 or object2_x2 >= object1_x2 >= object2_x1:
        if mass1 == mass2:
            temp = velocity1
            velocity1 = velocity2
            velocity2 = temp
        else:
            velocity1f = ((mass1 - mass2) * velocity1 + 2*mass2 * velocity2)/(mass1+mass2)
            velocity2f = ((mass2 - mass1) * velocity2 + 2 * mass1 * velocity1) / (mass1 + mass2)
            velocity1 = velocity1f
            velocity2 = velocity2f

def move():
    global mass1, mass2, velocity1, velocity2
    canvas.move(object1, velocity1, 0)
    canvas.move(object2, velocity2, 0)

    wall_check()
    collision_check()

    root.after(25, move)

    return

frame1 = tk.Frame(root)
frame1.pack()

prompt1 = tk.Label(frame1, text = "Enter mass of object 1: ", font = ("Arial", 16))
prompt1.grid( row = 0, column = 0, padx = 10, pady = 10)

entry1 = tk.Entry(frame1, font = ("Arial", 16))
entry1.grid( row = 0, column = 1, padx = 10, pady = 10)

prompt2 = tk.Label(frame1, text = "Enter mass of object 2: ", font = ("Arial", 16))
prompt2.grid( row = 1, column = 0, padx = 10, pady = 10)

entry2 = tk.Entry(frame1, font = ("Arial", 16))
entry2.grid( row = 1, column = 1, padx = 10, pady = 10)

prompt3 = tk.Label(frame1, text = "Enter initial velocity of object 1:  ", font = ("Arial", 16))
prompt3.grid( row = 2, column = 0, padx = 10, pady = 10)

entry3 = tk.Entry(frame1, font = ("Arial", 16))
entry3.grid( row = 2, column = 1, padx = 10, pady = 10)

prompt4 = tk.Label(frame1, text = "Enter initial velocity of object 2:  ", font = ("Arial", 16))
prompt4.grid( row = 3, column = 0, padx = 10, pady = 10)

entry4 = tk.Entry(frame1, font = ("Arial", 16))
entry4.grid( row = 3, column = 1, padx = 10, pady = 10)

start = tk.Button(frame1, text = "Start", font = ("Arial", 16), command = start)
start.grid( row = 4, column = 0, padx = 10, pady = 10)

root.mainloop()