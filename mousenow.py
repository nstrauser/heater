#!/usr/bin/env python3
#import subprocess
import pyautogui


def run():
    try:
        while True:
            # Print mouse coordinates
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\nDone.')

if __name__=='__main__':
    #subprocess.Popen(['clear'])
    print('\nPress Ctrl-C to quit.\n')
    run()
