import gui
import threading
import queue
import camera
import udp_rec
import controller

from globals import *



def main():
    print("start")

    guiThread = threading.Thread(target=gui.threadGUI)
    camThread = threading.Thread(target=camera.camThread)
    udpRecThread = threading.Thread(target=udp_rec.udpRecThread)
    conThread = threading.Thread(target= controller.controllerTread)

    guiThread.start()
    camThread.start()
    udpRecThread.start()
    conThread.start()

    while True:
        message = cmdGui.get()
        print(message)

if __name__ == "__main__":
    main()


