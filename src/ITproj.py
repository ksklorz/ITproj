import gui
import threading
import queue
import camera
import udp_rec

from globals import *



def main():
    print("start")

    guiThread = threading.Thread(target=gui.threadGUI)
    camThread = threading.Thread(target=camera.camThread)
    udpRecThread = threading.Thread(target=udp_rec.udpRecThread)
    
    guiThread.start()
    camThread.start()
    udpRecThread.start()

    while True:
        message = cmdGui.get()
        print(message)

if __name__ == "__main__":
    main()


