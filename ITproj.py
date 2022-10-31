import gui
import threading




def main():
    print("start")
    guiThread = threading.Thread(target=gui.threadGUI)
    guiThread.start()

if __name__ == "__main__":
    main()


