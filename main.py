#Simple LED strip control with python and arduino
import serial
import struct
from tkinter import *

root = Tk()
redIntensity = IntVar()
greenIntensity = IntVar()
blueIntensity = IntVar()

arduino = serial.Serial("COM3", 9600, timeout=None)

def updateLights(*_):
    #callback function for sliders
    arduino.write(struct.pack('>BBB', int(redIntensity.get()), int(greenIntensity.get()), int(blueIntensity.get())))

#Red GUI components
textR = StringVar()
textR.set("RED")
labelR = Label(root, textvariable=textR)
scaleR = Scale(root, variable = redIntensity, command = updateLights,orient = HORIZONTAL, to=255)

#Green GUI components
textG = StringVar()
textG.set("GREEN")
labelG = Label(root, textvariable=textG)
scaleG = Scale(root, variable = greenIntensity, command = updateLights,orient = HORIZONTAL, to=255)

#Blue GUI components
textB = StringVar()
textB.set("BLUE")
labelB = Label(root, textvariable=textB)
scaleB = Scale(root, variable = blueIntensity, command = updateLights, orient = HORIZONTAL, to=255)

#GUI frame structure
labelR.pack()
scaleR.pack()
labelG.pack()
scaleG.pack()
labelB.pack()
scaleB.pack()

root.mainloop()
