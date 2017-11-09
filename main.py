from gpiozero import LightSensor, OutputDevice
from time import sleep
import threading

ldr = LightSensor(4)
laser = OutputDevice(2)
doorClosed = True

print('Started')

def closeDoor():
    print('Closing door')
    

class checker(threading.Thread):
    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    

    def run(self):
        global ldr
        global doorClosed
        
        while True:
            sleep(0.5)
            if ldr.value < 0.2:
                doorClosed = False
            else:
                doorClosed = True
                #print('Set to True')

class wait(threading.Thread):
    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    

    def run(self):
        global doorClosed
        global ldr
        
        while True:
            sleep(0.1)
            if not doorClosed:
                print('Door opened')
                #buzzer.on()
                sleep(2)
                #buzzer.off()
                sleep(10)
                if not doorClosed:
                    print('Closing door')
                else:
                    print('Door was closed')

class cool(threading.Thread):
    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    

    def run(self):
        global laser
    
        while True:
            laser.on()
            sleep(55)
            print('Cooling...')
            laser.off()
            sleep(8)

class debug(threading.Thread):
    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    

    def run(self):
        global ldr
        global doorClosed
    
        while True:
            sleep(1)
            print(doorClosed, ':', ldr.value)


checkerThread = checker(1, 'checkerThread')
waitThread = wait(2, 'waitThread')
coolThread = cool(3, 'coolThread')
debugThread = debug(4, 'debugThread')
#debugThread.start()
waitThread.start()
coolThread.start()
checkerThread.start()
