# Control panel for SK2GJ
# Based on https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
# SM2YHP 2021

import tkinter
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
import time
import webcam

class Panel(tkinter.Frame):
    # Set up the main window
    def __init__(self, root, appTitle):
        super().__init__(root)
        self.root = root
        self.root.title(appTitle)
        # Add video frame
        self.create_video()
        # Add buttons
        self.create_buttons()
        # Stream the video
        self.update_video()
        
    def create_video(self, video_source=0):
        # open video source (by default this will try to open the computer webcam)
        self.vid = webcam.VideoCapture(video_source)
        # Create a canvas that can fit the above video source size
        self.videoDisplay = tkinter.Canvas(self.root, width = self.vid.width, height = self.vid.height)     
        self.videoDisplay.grid(row=1, column=0, rowspan=5, columnspan=2)
        l = tkinter.Label(self.root, text="Remote control (C) SM2YHP", font =('calibri', 12, 'bold'))
        l.grid(row=0, column=0, columnspan=2, sticky=tkinter.S)
        self.delay = 15
       
    def update_video(self):
        # Update thw video frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.videoDisplay.create_image(10, 50, image = self.photo, anchor = tkinter.NW)
        self.videoDisplay.after(self.delay, self.update_video)

    def create_buttons(self):
        # Create the button widgets
        # Power relay button
        self.power_on = False
        self.power = tkinter.Button(self.root, text="POWER", bg="red", fg="white", command=self.toggle_power)
        self.power.grid(row=0, column=2, ipady=20)
        # Rotor CCW button
        self.ccw = tkinter.Button(self.root, text="<- CCW", bd=3, bg="black", activebackground="yellow", fg="yellow", activeforeground="black", command=print("Hello"))
        self.ccw.grid(row=6, column=0, ipadx=50, ipady=20)
        # Rotor CW button
        self.ccw = tkinter.Button(self.root, text="CW ->", bd=3, bg="black", activebackground="yellow", fg="yellow", activeforeground="black", command=print("Hello"))
        self.ccw.grid(row=6, column=1, ipadx=50, ipady=20)
        # Quit button
        self.quitBtn = tkinter.Button(self.root, text="Quit", fg="red", command=self.confirm_exit)
        self.quitBtn.grid(row=6, column=2)
        # Antenna selector
        self.antNo = tkinter.IntVar(self.root, 1)
        self.ant1 = tkinter.Radiobutton(self.root, text = "Antenna 1", variable = self.antNo, value=1, indicator = 0)
        self.ant2 = tkinter.Radiobutton(self.root, text = "Antenna 2", variable = self.antNo, value=2, indicator = 0)
        self.ant3 = tkinter.Radiobutton(self.root, text = "Antenna 3", variable = self.antNo, value=3, indicator = 0)
        self.ant4 = tkinter.Radiobutton(self.root, text = "Antenna 4", variable = self.antNo, value=4, indicator = 0)
        self.ant5 = tkinter.Radiobutton(self.root, text = "Antenna 5", variable = self.antNo, value=5, indicator = 0)
        self.ant1.grid(row=1, column=2, ipadx=10, ipady=20)
        self.ant2.grid(row=2, column=2, ipadx=10, ipady=20)
        self.ant3.grid(row=3, column=2, ipadx=10, ipady=20)
        self.ant4.grid(row=4, column=2, ipadx=10, ipady=20)
        self.ant5.grid(row=5, column=2, ipadx=10, ipady=20)

    def confirm_exit(self):
        answer = askyesno(title="Exit", message="Are you sure?")
        if answer:
            self.root.destroy()

    def toggle_power(self):
        answer = askyesno(title="Power relay", message=f"Really turn power relay {'OFF' if self.power_on else 'ON'}?")
        if answer:
            if self.power_on:
                # Turn OFF
                self.power_on = False
                self.power["bg"] = "red"
            else:
                # Turn ON
                self.power_on = True
                self.power["bg"] = "green"
        
        
if __name__ == '__main__':
    app=Panel(tkinter.Tk(), "SK2GJ Control Panel")
    app.mainloop()
