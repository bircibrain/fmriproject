# import psychopy modules
from psychopy import visual, core, event, sound, gui, data
# import math (for rounding function)
import math

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


# in the data source, there are two columns: Time (0-502) and StimType (1-6)
# Link the numbers in StimType to the names of the text displays
STIM = {1: Rhand_txt, 2: Lhand_txt, 3: Rfoot_txt, 4: Lfoot_txt, 5: tongue_txt, 6: null_txt}
# load in our stimulus timing csv file
TRIAL_LIST = data.importConditions(fileName = parent_dir + "localizer_datasource.csv")

#create clock
globalClock = core.Clock()

# start clock from 5 from scanner --- TIM ADD HERE
# Create variable for start point from when scanner began (t0)
t0 = globalClock.getTime()

# while the clock is running...
while globalClock.getTime()-t0 < 503.25:
# Goal for this section: Check what time it is. If the time matches a value in the column "Time"
# then present the text display from that same row for 1.25 seconds and then go back to blank
# if  the time is greater than 503.25 seconds, end the while loop
# create a variable for the time (t1)
    t1=globalClock.getTime()-t0
# look through the rows of the data source
    for index in range(len(TRIAL_LIST)):
# if the number in the "Time" column matches the timestamp (rounded down to nearest integer)
        if TRIAL_LIST[index]["Time"] == math.floor(t1):
# draw the screen indicated in the StimType column and then present it
            STIM[TRIAL_LIST[index]["StimType"]].draw(); win.flip()
# wait for 1.25 seconds
            core.wait(1.25)
# then flip back to the blank screen
            win.flip()
# else, if we're past the run time, end the loop
        elif globalClock.getTime()-t0 > 503.25:
            break

# TIM -- it would be useful to add something in the while loop above to break out using a keypress

# close everything
win.close()
core.quit()

