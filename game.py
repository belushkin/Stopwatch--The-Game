# template for "Stopwatch: The Game"

import simplegui
    
# define global variables
time = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    seconds = time // 10
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(time // 600) + ":" + str(seconds) + "." + str(time % 10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global x, y
    if (timer.is_running()):
        x += 1
        if (time % 10) == 0:
            y += 1
    timer.start()
    
def stop_handler():
    timer.stop()
    
def reset_handler():
    global time, x, y
    time = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    #print time

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (170, 200), 34, "Red")
    canvas.draw_text(str(x), (290, 50), 32, "Green")
    canvas.draw_text("/", (330, 50), 32, "Green")
    canvas.draw_text(str(y), (360, 50), 32, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 400)


# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler, 200)
frame.add_button("Stop", stop_handler, 200)
frame.add_button("Reset", reset_handler, 200)

# start frame
frame.start()

