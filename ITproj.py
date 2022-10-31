import gui
import threading
import queue

from globals import *



def main():
    print("start")

    guiThread = threading.Thread(target=gui.threadGUI)
    guiThread.start()

    while True:
        message = cmdGui.get()
        print(message)

if __name__ == "__main__":
    main()


