# Made By Prashanth Umapathy
# Specialises in Extreme Laziness

# Very important imports
import webbrowser, time
import pyautogui as pag
import schedule

# Meeing info
url = "https://meet.google.com/nwq-cjwj-yvi"
meeting_time = 1
comment_ask = 'yes'
meet_join_time = "09:32"


meet_join_time = str(meet_join_time)

# Comment Check
if (comment_ask.lower() == 'yes' or 'y' or 'Y'):
    name = "Stefan"
    regNo = "12A1/27"
    classSec = "hadir"
    foo = True
else:
    foo = False

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


# Opens the meeting ID
def meeting_join():
    webbrowser.get(chrome_path).open(url)

    time.sleep(4)

    pag.hotkey('ctrl','d')
    pag.hotkey('ctrl','e')

    time.sleep(3)

    for i in range(5):
        pag.press('tab')

    time.sleep(2)
    pag.press('enter')

    print("Session has started and will continue for %s minutes"%meeting_time)
    print('Press (Ctrl+c) to exit the program ')
    time.sleep(2)

# Adds the comment in meeting
def comment(name,regNo,classSec):
    time.sleep(15)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('enter')

    time.sleep(4)

    pag.write(name, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(regNo, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(classSec, interval=0.1)
    pag.press('enter')

# Where the wizards work
def mainFunc():
    meeting_join()
    if(foo):
        comment(name,regNo,classSec)
    time.sleep(meeting_time*60)
    pag.hotkey('ctrl','w')
    print('Meeting ended')

if __name__ == "__main__":
    # Schedule it to the time given
    schedule.every().day.at("%s"%meet_join_time).do(mainFunc)
    print("Scheduling meeting at ",meet_join_time)

    while True: 
    # Check whether any scheduled task is pending to run or not
        schedule.run_pending() 
        time.sleep(1) 