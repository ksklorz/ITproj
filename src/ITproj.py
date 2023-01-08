import gui
import threading
import queue
import camera
import udp_rec
import controller
import udpSend

from globals import *



def main():
    print("start")

    guiThread = threading.Thread(target=gui.threadGUI)
    camThread = threading.Thread(target=camera.camThread)
    udpRecThread = threading.Thread(target=udp_rec.udpRecThread)
    conThread = threading.Thread(target= controller.controllerTread)
    udpSendThread = threading.Thread(target= udpSend.udpSendThread)

    # guiThread.start()
    camThread.start()
    udpRecThread.start()
    conThread.start()
    udpSendThread.start()

    # while True:
    #     message = cmdGui.get()
    #     print(message)

if __name__ == "__main__":
    main()


