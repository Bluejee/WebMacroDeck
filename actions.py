import pyautogui
from time import sleep


# Sample Actions
def type_text():
    pyautogui.typewrite('This is a sample line. Without a newline charecter.....')
    sleep(1)
    pyautogui.typewrite('This line has a newline charecter.' + '\n')
    sleep(1)
    pyautogui.typewrite('hence it acts similar to typing a sentence and pressing enter.' + '\n')
    pyautogui.typewrite('Sleep can be used to wait for sittuations like in ssh where you might want to wait for a second for the password promt to show.')



