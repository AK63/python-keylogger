from pynput.keyboard import Listener
from datetime import datetime
#listeners-listen to keystrokes
#use of 'with' keyword -release memory/resource automatically 
def writetofile(key):
    letter=str(key)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    letter=letter.replace("'"," ")
    if letter=='Key.space':
        letter=' '
    if letter=='Key.shift':
        letter=' '
    if letter=='Key.enter':
        letter="\n"
    if letter=='Key.esc':
        return False
    log_line = f"{timestamp} - {letter}\n"
    print(log_line.strip())
    print(letter)
    with open("log.txt",'a') as f:
        f.write(log_line)

#how to listen for keystroke in python by the help for pynput we can listen and control keyboard and mouse
with Listener(on_press=writetofile) as l:
    l.join()