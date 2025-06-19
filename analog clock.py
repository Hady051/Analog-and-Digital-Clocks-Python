
import tkinter as ui
import time
import math

window = ui.Tk()
window.geometry("400x400")



def update_clock():
    hours = int(time.strftime("%I")) + 1
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # update seconds hand per second
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_of_x                       # 360 divide by 60 sec
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_of_y                  # bec the clk origin is at 200,200 not 0,0
    canvas.coords(seconds_hand, center_of_x, center_of_y, seconds_x, seconds_y)

    # update to minutes hand per minute
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_of_x                        # 360 divide by 60 min
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_of_y
    canvas.coords(minutes_hand, center_of_x, center_of_y, minutes_x, minutes_y)

    # update to hours hand per hour
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_of_x                              # times 30 beacause hours are 12, and we divide 360 by 12
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_of_y
    canvas.coords(hours_hand, center_of_x, center_of_y, hours_x, hours_y)

    window.after(1000, update_clock)

canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True)

# background creation
bg = ui.PhotoImage(file="clock img.png")
canvas.create_image(200,200, image=bg)     # should be midpoints of og pic

# clock hands
center_of_x = 200
center_of_y = 200                # origin (x,y) of the center of clk
hours_hand_len = 60
minutes_hand_len = 80
seconds_hand_len = 95

# drawing clock hands

hours_hand = canvas.create_line(200,200,200 + hours_hand_len, 200+hours_hand_len, width=5, fill= "white")

minutes_hand = canvas.create_line(200,200,200 + minutes_hand_len, 200 + minutes_hand_len, width=3, fill="white")

seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=2, fill="blue")

update_clock()

window.mainloop()