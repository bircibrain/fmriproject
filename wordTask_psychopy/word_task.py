# import psychopy modules
from psychopy import visual, core, event, sound, gui, data, logging
# import math (for rounding function)
import math
import numpy as np 

#set parent directory
parent_dir = "./"


# info about the screen
win = visual.Window(size = [1280,768],
                    color = "white",
                    fullscr = False,
                    units = "pix")

# Set up text displays
ScannerWait_txt = visual.TextStim(win, text = "Waiting for scanner....",
                        pos = [0.0,0.0],
                        color = "black",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

FinalThankYou_txt = visual.TextStim(win, text = "Thank you!",
                        pos = [0.0,0.0],
                        color = "black",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)

null_txt = visual.TextStim(win, text = "+",
                        pos = [0.0,0.0],
                        color = "black",
                        height = 50,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        autoLog=True)
                        
instruct_txt = visual.TextStim(win, text = " In this experiment you will be reading words.\n Please, read them carefully.\n Press the space bar when you are ready to continue.",
                        pos = [0.0,0.0],
                        color = "black",
                        height = 24,
                        alignHoriz='center',
                        alignVert='center',
                        font = "Arial",
                        wrapWidth= 1000,
                        autoLog=True)

#get some startup information from the user
info = {'participant_id':'', 'session': '1'}
dlg = gui.DlgFromDict(info, title = 'Word Task Startup')
if not dlg.OK:
    core.quit()
 
prefix = 'sub-%s_ses-%s_task-word' % (info['participant_id'], info['session'])

#logging data 
# overwrite (filemode='w') a detailed log of the last run in this dir
errorLog = logging.LogFile(prefix + "_errorlog.log", level=logging.DATA, filemode='w')
#win.logonFlip(msg=' ', level=logging.DATA)
# in the data source, there are three columns: Time, StimType and Stim
# load in our stimulus timing xlsx file
TRIAL_LIST = data.importConditions(fileName = parent_dir + "RunTest.xlsx")
totalTrials = len(TRIAL_LIST)
                        
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
#show waiting for scanner until keypress
ScannerWait_txt.draw()
win.flip()  
#wait for a 5 or t keypress to start
keys =event.waitKeys(keyList=['t','5'], timeStamped=globalClock)
t0 = float(keys[0][0])
#creating variable for flip duration
flip_duration= 21
# header for data log
data = np.hstack(("Stim","StimType","onset"))
# Goal for this section: Check what time it is. If the time matches a value in the column "Time"
# then present the text display from that same row for 1.25 seconds and then go back to blank
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
    #init stim
    stim = visual.TextStim(win, text=TRIAL_LIST[index]['Stim'], 
                        pos = [0.0,0.0],
                        color="black",
                        height=50,
                        alignHoriz='center',
                        alignVert='center',
                        font="Arial", 
                        wrapWidth= 1000,
                        autoLog=True)
    stim.draw();
    win.flip()
    logging.log("Datalog.log",level=logging.EXP)
    win.logOnFlip("Datalog.log",level=logging.EXP)
    onset = globalClock.getTime()
    core.wait(1.25-(globalClock.getTime()-onset))
    null_txt.draw()
    win.flip()
    onset = globalClock.getTime() 
    core.wait(1.25-(globalClock.getTime()-onset))
    # store data into the numpy array
    data = np.vstack((data, np.hstack((TRIAL_LIST[index]["Stim"],TRIAL_LIST[index]['StimType'],onset,))))# round the onset time (in seconds) to the third decimal place
#clear screen
null_txt.draw()
win.flip()
#display a Thank You message
FinalThankYou_txt.draw()
win.flip()
core.wait(5-(globalClock.getTime()-onset))
win.flip()
    
### SAVE DATA ###
np.savetxt(parent_dir+prefix+"_onsets.tsv",
            data, fmt='%s', delimiter='\t', newline='\n',
            header='', footer='', comments='# ')
# close everything
win.close()
core.quit()
