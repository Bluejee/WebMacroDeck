import pyautogui
import subprocess
from time import sleep

# Text Manipulation Functions
# ---------------------------

def type_text():
    """
    Simulates typing text into the active window, including the use of new line characters
    and incorporating delays to mimic natural typing and wait times for certain actions like
    password prompts.
    """
    pyautogui.typewrite('This is a sample line. Without a newline character.....')
    sleep(1)
    pyautogui.typewrite('This line has a newline character.' + '\n')
    sleep(1)
    pyautogui.typewrite('Hence it acts similar to typing a sentence and pressing enter.' + '\n')
    pyautogui.typewrite('Sleep can be used to wait for situations like in ssh where you might want to wait for a second for the password prompt to show.')

# Application and Web Navigation Functions
# ----------------------------------------

def open_app():
    """
    Opens an application by name using the Windows Run dialog.
    The function simulates pressing the Win+R keys, types the application name,
    and presses Enter. Useful for quickly opening applications without navigating through menus.
    """
    app_name = 'Chrome'
    pyautogui.hotkey('win', 'r')
    sleep(1)
    pyautogui.typewrite(app_name)
    sleep(1)
    pyautogui.press('enter')

def open_website():
    """
    Opens a website in a specified browser using the Windows Run dialog.
    This function can be customized to open websites in different browsers by specifying
    the browser's command.
    """
    url='www.example.com'
    browser='firefox'

    pyautogui.hotkey('win', 'r')
    sleep(1)
    pyautogui.typewrite(browser + ' ' + url + '\n')

def open_workspace():
    """
    Opens a specified folder in Windows Explorer, PyCharm, and Visual Studio Code.
    This function is useful for setting up a workspace with a single command, allowing you to
    quickly start working on a project across multiple applications.
    """
    folder_path = 'C:\Users\Username\Documents' # Change it to work correctly
    # Open the folder in Windows Explorer
    subprocess.Popen(f'explorer "{folder_path}"')

    # Open the folder in PyCharm (Adjust the path as necessary)
    subprocess.Popen([r"C:\Program Files\JetBrains\PyCharm 2021.1\bin\pycharm64.exe", folder_path])

    # Open the folder in Visual Studio Code
    subprocess.Popen(['code', folder_path])

# System Control Functions
# ------------------------

def volume_up():
    """Increases the system volume."""
    pyautogui.press('volumeup')

def volume_down():
    """Decreases the system volume."""
    pyautogui.press('volumedown')

def mute_unmute():
    """Toggles mute/unmute on the system volume."""
    pyautogui.press('volumemute')

# Clipboard Functions
# -------------------

def copy():
    """Copies the selected text or item to the clipboard."""
    pyautogui.hotkey('ctrl', 'c')

def cut():
    """Cuts the selected text or item and copies it to the clipboard."""
    pyautogui.hotkey('ctrl', 'x')

def paste():
    """Pastes the content from the clipboard into the current application."""
    pyautogui.hotkey('ctrl', 'v')
