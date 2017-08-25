# import psychopy modules
from psychopy import visual, core, event, sound, gui, data, logging
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
ScannerWait_txt = visual.TextStim(win, text = "Waiting for scanner....",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

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


def check_exit():
#abort if esc was pressed
    if event.getKeys('escape'):
        win.close()
        core.quit()
        
#create clock
globalClock = core.Clock()
#show waiting for scanner until keypress
ScannerWait_txt.draw()
win.flip()  
#wait for a 5 or t keypress to start
keys =event.waitKeys(keyList=['t','5'], timeStamped=globalClock)
t0 = float(keys[0][0])
#creating variable for flip duration
flip_duration= 21
# Goal for this section: Check what time it is. If the time matches a value in the column "Time"
# then present the text display from that same row for 1.25 seconds and then go back to blank

#setting up the first stimulus outside  the loop
STIM[TRIAL_LIST[0]["StimType"]].draw()
# look through the rows of the data source     
for index in range(len(TRIAL_LIST)):
    #draw so we are ready to flip
    STIM[TRIAL_LIST[index]["StimType"]].draw();
    #wait until the right moment
    #abort if esc was pressed
    #exit will be delayed until the end of a block
    check_exit()
    while globalClock.getTime()-t0 < TRIAL_LIST[index]['Time']:
        #abort if esc was pressed
        check_exit()
        
        #wait a tick
        core.wait(1.0/60.0)
    
    #done waiting
    #hard coding the number of cycles
    for j in range(8):
        win.flip()
        onset = globalClock.getTime()
        null_txt.draw()
        core.wait(1.25-(globalClock.getTime()-onset))
        win.flip()
        onset = globalClock.getTime()
        STIM[TRIAL_LIST[index]["StimType"]].draw();
        core.wait(1.25-(globalClock.getTime()-onset))
    
    #clear screen
    null_txt.draw()
    win.flip()
    
# close everything
win.close()
core.quit()

