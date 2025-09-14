# Imports
from sorts import bogosort, bubble_sort, gnome_sort, heap_sort, insertion_sort, merge_sort, quicksort, selection_sort
import turtle as t
import time
import random

# Constants
ALL_ALGORITHMS = [bogosort, bubble_sort, gnome_sort, heap_sort, insertion_sort, merge_sort, quicksort, selection_sort]
ALL_ALGORITHMS_NAMES = ["bogosort", "bubblesort", "gnomesort", "heapsort", "insertionsort", "mergesort", "quicksort", "selectionsort"]
SORTED_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

screen = t.Screen()
screen.tracer(0)

# Variables
algrorithms = []
algrorithms_names = []
my_turtles = []
turns = 0
task_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random.shuffle(task_list)

include_input = input("Do you want to include all?: y/n ")
if include_input.lower().strip() != "n":
    algrorithms = ALL_ALGORITHMS
    algrorithms_names = ALL_ALGORITHMS_NAMES
else:
    for i in range(8):
        yesno = input(f"Do you want to include {ALL_ALGORITHMS_NAMES[i]} in the race?: y/n ")
        if yesno.lower().strip() != "n":
            algrorithms.append(ALL_ALGORITHMS[i])
            algrorithms_names.append(ALL_ALGORITHMS_NAMES[i])

# graphics
t.hideturtle()
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def smooth_goto(turtle_obj, target_x, steps=5):
    start_x = turtle_obj.xcor()
    delta = (target_x - start_x) / steps
    for _ in range(steps):
        turtle_obj.setx(turtle_obj.xcor() + delta)
        screen.update()
        time.sleep(0.0005)  # adjust for speed

# get all outputs from the algorithms
outputs = []
for alg in algrorithms:
    outputs.append(alg(task_list))

def turn(n):
    for i in range(len(algrorithms)):
        turtle_obj = my_turtles[i]
        if n < len(outputs[i]):
            alg_score = outputs[i][n][1]
        else:
            alg_score = outputs[i][-1][1]
        target_x = alg_score * 20 - 200
        smooth_goto(turtle_obj, target_x)  # smooth movement

    screen.update()   # manually refresh the screen
    time.sleep(0.001)  # small delay for animation

move_to(-400, 200)

for i in algrorithms_names:   
    t.write(i, move=False, align='left', font=('Courier', 25, 'bold')) 
    turtle = t.Turtle()
    turtle.penup()
    turtle.goto(t.xcor()+200, t.ycor()+12.5)
    turtle.speed(0)
    turtle.color(random.choice(["red", "orange", "purple", "green", "blue", "black", "brown", "pink"]))
    my_turtles.append(turtle)
    move_to(t.xcor(), t.ycor()-50)

move_to(-200, 250)
t.goto(-200, -250)
move_to(200, 250)
t.goto(200, -250)
screen.listen()
max_turns = max(len(out) for out in outputs)
for n in range(max_turns):
    turn(n)
for i in range(len(algrorithms)):
    print(len(outputs[i]), algrorithms_names[i])
t.mainloop()