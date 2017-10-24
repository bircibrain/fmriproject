# import psychopy modules
from psychopy import visual, core, event, sound, gui, data, logging
# import math (for rounding function)
import math
import numpy as np 

#set parent directory
parent_dir = "./"

#get some startup information from the user
info = {'participant_id':'', 'session': '1'}
dlg = gui.DlgFromDict(info, title = 'Localizer Startup')
if not dlg.OK:
    core.quit()

# info about the screen
win = visual.Window(size = [1280,768],
                    color = "black",
                    fullscr = True, allowGUI=False,
                    units = "pix")

# Set up text displays
ScannerWait_txt = visual.TextStim(win, text = "Waiting for scanner....",
                        pos = [0.0,0.0],
                        color = "white",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

Rhand_txt = visual.TextStim(win, text = "Curl your right hand.",
                        pos = [0.0,0.0],
                        color = "white",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

Lhand_txt = visual.TextStim(win, text = "Curl your left hand.",
                        pos = [0.0,0.0],
                        color = "white",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

Rfoot_txt = visual.TextStim(win, text = "Curl your right foot.",
                        pos = [0.0,0.0],
                        color = "white",
                        height = 50,
                        font = "Arial",
                        autoLog=True)

Lfoot_txt = visual.TextStim(win, text = "Curl your left foot.",
                        pos = [0,0],
                        color = "white",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

tongue_txt = visual.TextStim(win, text = "Curl your tongue.",
                        pos = [0,0],
                        color = "white",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

null_txt = visual.TextStim(win, text = "+",
                        pos = [0.0,0.0],
                        color = "white",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)
                        
instruct_txt = visual.TextStim(win, text = "     For the next eight minutes, you will be asked to curl various part of your body.\n\n\
     When you see instructions on the screen (e.g.-Curl your right hand), \n\
     Please perform the action ONLY when the instructions are on the screen.\n\n\
     When you see a fixation (+), please relax your body.\n\n\
     Press the space bar when you are ready to continue.",
                        pos = [0.0,0.0],
                        color = "white",
                        height = 24,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        wrapWidth= 1000,
                        autoLog=True)


 
prefix = 'sub-%s_ses-%s_task-localizer' % (info['participant_id'], info['session'])

#logging data 
# overwrite (filemode='w') a detailed log of the last run in this dir
errorLog = logging.LogFile(prefix + "_errorlog.log", level=logging.DATA, filemode='w')
#win.logonFlip(msg=' ', level=logging.DATA)
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
logging.setDefaultClock(globalClock)
#showing instructions first 
instruct_txt.draw()
win.flip() 
#waiting for space bar to continue
keys =event.waitKeys(keyList=['space'], timeStamped=globalClock)
check_exit()
#show waiting for scanner until keypress
ScannerWait_txt.draw()
win.flip()  
#wait for a 5 or t keypress to start
keys =event.waitKeys(keyList=['t','5'], timeStamped=globalClock)
t0 = float(keys[0][0])
#creating variable for flip duration
flip_duration= 21
# header for data log
data = np.hstack(("StimType","onset"))
# Goal for this section: Check what time it is. If the time matches a value in the column "Time"
# then present the text display from that same row for 1.25 seconds and then go back to blank

#setting up the first stimulus outside  the loop
#STIM[TRIAL_LIST[0]["StimType"]].draw()
# look through the rows of the data source     
for index in range(len(TRIAL_LIST)):
    #draw so we are ready to flip
    
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
        STIM[TRIAL_LIST[index]["StimType"]].draw();
        win.flip()
        onset = globalClock.getTime()
        logging.log("Datalog.log",level=logging.EXP)
        win.logOnFlip("Datalog.log",level=logging.EXP)

        if j ==0 :
            block_onset = onset - t0

        core.wait(1.25-(globalClock.getTime()-onset))
        
        null_txt.draw()
        win.flip()
        onset = globalClock.getTime()
        core.wait(1.25-(globalClock.getTime()-onset))
#clear screen
    null_txt.draw()
    win.flip()
    
    
# store data into the numpy array
    data = np.vstack((data, np.hstack((
                                       TRIAL_LIST[index]["StimType"],
                                       block_onset,
                                       ))))# round the onset time (in seconds) to the third decimal place

### SAVE DATA ###
np.savetxt(parent_dir+prefix+"_onsets.tsv",
            data, fmt='%s', delimiter='\t', newline='\n',
            header='', footer='', comments='# ')
# close everything
win.close()
core.quit()

