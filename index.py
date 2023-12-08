import time
import sys
import os
import pyperclip

clipboard_val = pyperclip.paste()

while True:
    if clipboard_val != pyperclip.paste():
        clipboard_val = pyperclip.paste()

    if "//twitter.com" in clipboard_val:
        clipboard_val = clipboard_val.replace("//twitter.com", "//vxtwitter.com")
        pyperclip.copy(clipboard_val)

    time.sleep(0.001)