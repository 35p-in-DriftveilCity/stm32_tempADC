import serial
# import time
import struct
import tkinter

# register window
window = tkinter.Tk()
window.title("Canvas") #title
window.geometry("640x480") #size
window.resizable(False,False) #can't control size

# generate canvas
canvas = tkinter.Canvas(window, relief="solid", bd=2, bg='white')
canvas.config(width=640, height = 480)

# canvas packing
canvas.pack()

# rxBuffer = [] not use in this code

ser = serial.Serial("COM7",115200)

def updateCanvas():
    if ser.in_waiting >0:
        byte = ser.read()

        # detect start code
        if byte == b'\x11':
            while ser.in_waiting == 0:
                pass
            byte = ser.read()
            if byte == b'\x22':
                while ser.in_waiting ==0:
                    pass

                # delete recent canvas
                canvas.delete('all')
                
                # read data
                byteX = ser.read(2)
                byteY = ser.read(2)
                
                # data parsing
                xValue = struct.unpack('>h',byteX)# bigendian
                yValue = struct.unpack('>h',byteY)# tupel 한번 설정하면 교체 불가.
                
                canvas.create_line(320, 240, 320+int(xValue[0])/274, 240+int(yValue[0])/274, fill='blue', width =3)

    # recursive call            
    canvas.after(100, updateCanvas) 


updateCanvas()
window.mainloop()
