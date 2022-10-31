import gui
import threading
import queue
import camera

from globals import *



def main():
    print("start")

    guiThread = threading.Thread(target=gui.threadGUI)
    camThread = threading.Thread(target=camera.camThread)
    
    guiThread.start()
    camThread.start()

    while True:
        message = cmdGui.get()
        print(message)

if __name__ == "__main__":
    main()


