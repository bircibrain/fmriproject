# import psychopy modules
from psychopy import visual, core, event, sound, gui, data, logging
# import math (for rounding function)
import math
from psychopy.iohub import launchHubServer
from psychopy.iohub.devices.keyboard import KeyboardInputEvent
io=launchHubServer()
keyboard=io.devices.keyboard

#set parent directory
parent_dir = "./"

# info about the screen
win = visual.Window(size = [1920,1080],
                    color = "white",
                    fullscr = False,
                    units = "pix")

# Set up text displays
Rhand_txt = visual.TextStim(win, text = "Curl your right hand.",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

Lhand_txt = visual.TextStim(win, text = "Curl your left hand.",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

Rfoot_txt = visual.TextStim(win, text = "Curl your right foot.",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

Lfoot_txt = visual.TextStim(win, text = "Curl your left foot.",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

tongue_txt = visual.TextStim(win, text = "Curl your tongue.",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

null_txt = visual.TextStim(win, text = "+",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

#logging data 
# overwrite (filemode='w') a detailed log of the last run in this dir
lastLog = logging.LogFile("lastRun.log", level=logging.INFO, filemode='w')

# in the data source, there are two columns: Time (0-502) and StimType (1-6)
# Link the numbers in StimType to the names of the text displays
STIM = {1: Rhand_txt, 2: Lhand_txt, 3: Rfoot_txt, 4: Lfoot_txt, 5: tongue_txt, 6: null_txt}
# load in our stimulus timing csv file
TRIAL_LIST = data.importConditions(fileName = parent_dir + "localizer_datasource.csv")
#defining get_keypress to use as esc from experiment 
def get_keypress():
    keys = event.getKeys()
    if keys:
        return keys[0]
    else:
        return None
def shutdown():
    win.close()
    core.quit()

#create clock
globalClock = core.Clock()
#wait for a 5 or t keypress to start
print "Waiting for scanner..."
key = get_keypress ()
if key == 't' or '5' 
    keyboard.waitForKeys() = False 
else:
    keyboard.waitForKeys() = True 
# Create variable for start point from when scanner began (t0)
t0 = globalClock.getTime()
#creating variable for flip duration
flip_duration= 20
# create a variable for the time (t1)
t1=globalClock.getTime()-t0

# while the clock is running...
while globalClock.getTime()-t0 < 503.25:
# Goal for this section: Check what time it is. If the time matches a value in the column "Time"
# then present the text display from that same row for 1.25 seconds and then go back to blank
# if  the time is greater than 503.25 seconds, end the while loop
#setting up the first stimulus outside  the loop
    Rhand_txt.draw()
    null_txt.draw() 
# look through the rows of the data source     
    for index in range(len(TRIAL_LIST)):
# if the number in the "Time" column matches the timestamp (rounded down to nearest integer)
        while True TRIAL_LIST[index]["Time"] >= math.floor(t1) :
# draw the screen indicated in the StimType column and then present it
            STIM[TRIAL_LIST[index]["StimType"]].win.flip()
# wait for 1.25 seconds
            core.wait(1.25)
# then flip back to crosshair
            null_txt.flip() 
#while current stimulus is presented, draw next stimulus 
        while True TRIAL_LIST[index]["Time"] >= math.floor(t1)+flip_duration :
            STIM[TRIAL_LIST[index]["StimType"]].draw() 
#if esc key pressed, abort the task
        keys = get_keypress()
        if keys[0] == 'Esc' :
                shutdown() 
        elif globalClock.getTime()-t0 > 503.25:
            break

# close everything
win.close()
core.quit()

