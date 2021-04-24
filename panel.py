# Control panel for SK2GJ antenna remote control
# Tkinter tutorials see https://www.geeksforgeeks.org/python-tkinter-tutorial/
# Video code see https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
#
# SM2YHP 2021
# fredrik@kyla.kiruna.se

import tkinter
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
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
        # Put a title above
        l = tkinter.Label(self.root, text="Remote control (C) SM2YHP", font =('calibri', 12, 'bold'))
        l.grid(row=0, column=0, columnspan=2, sticky=tkinter.S)
        self.delay = 15
       
    def update_video(self):
        # Update the video frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.videoDisplay.create_image(10, 50, image = self.photo, anchor = tkinter.NW)
        self.videoDisplay.after(self.delay, self.update_video)

    def create_buttons(self):
        # Create the button widgets
        # Power relay button
        self.power_on = False
        self.power = tkinter.Button(self.root, text="POWER", bg="light gray", fg="white", command=self.toggle_power)
        self.power.grid(row=0, column=2, ipady=20)
        # Rotor CCW button
        self.ccw = tkinter.Button(self.root, text="<- CCW", bd=3, bg="black", activebackground="yellow", fg="yellow", activeforeground="black")
        self.ccw.grid(row=6, column=0, ipadx=50, ipady=20)
        # Rotor CW button
        self.cw = tkinter.Button(self.root, text="CW ->", bd=3, bg="black", activebackground="yellow", fg="yellow", activeforeground="black")
        self.cw.grid(row=6, column=1, ipadx=50, ipady=20)
        # Rotor actions: move when buttons pressed. NB Must be function of one variable "event"
        self.ccw.bind('<ButtonPress-1>', lambda event: self.start_rotor(direction='ccw'))
        self.ccw.bind('<ButtonRelease-1>', lambda event: self.stop_rotor())
        self.cw.bind('<ButtonPress-1>', lambda event: self.start_rotor(direction='cw'))
        self.cw.bind('<ButtonRelease-1>', lambda event: self.stop_rotor())
        # Quit button
        self.quitBtn = tkinter.Button(self.root, text="Quit", fg="red", command=self.confirm_exit)
        self.quitBtn.grid(row=6, column=2)
        # Antenna selector
        self.antNo = tkinter.IntVar(self.root, 1)
        self.ant1 = tkinter.Radiobutton(self.root, text = "Antenna 1", variable = self.antNo, value=1, indicator = 0, selectcolor="red", command=self.set_antenna)
        self.ant2 = tkinter.Radiobutton(self.root, text = "Antenna 2", variable = self.antNo, value=2, indicator = 0, selectcolor="red", command=self.set_antenna)
        self.ant3 = tkinter.Radiobutton(self.root, text = "Antenna 3", variable = self.antNo, value=3, indicator = 0, selectcolor="red", command=self.set_antenna)
        self.ant4 = tkinter.Radiobutton(self.root, text = "Antenna 4", variable = self.antNo, value=4, indicator = 0, selectcolor="red", command=self.set_antenna)
        self.ant5 = tkinter.Radiobutton(self.root, text = "Antenna 5", variable = self.antNo, value=5, indicator = 0, selectcolor="red", command=self.set_antenna)
        self.ant1.grid(row=1, column=2, ipadx=10, ipady=20)
        self.ant2.grid(row=2, column=2, ipadx=10, ipady=20)
        self.ant3.grid(row=3, column=2, ipadx=10, ipady=20)
        self.ant4.grid(row=4, column=2, ipadx=10, ipady=20)
        self.ant5.grid(row=5, column=2, ipadx=10, ipady=20)

    def start_rotor(self, direction):
        # Turn on one of the rotor relays
        if direction == 'cw':
            print("Starting to move CW")
        elif direction == 'ccw':
            print("Starting to move CCW")
        else:
            pass

    def stop_rotor(self):
        # Turn off rotor outputs
        print("Stopping rotor")
                    
    def set_antenna(self):
        print(f"You selected antenna: {self.antNo.get()}")

    def toggle_power(self):
        # Confirmation dialogue
        answer = askyesno(title="Power relay", message=f"Really turn power relay {'OFF' if self.power_on else 'ON'}?")
        if answer:
            if self.power_on:
                # Turn OFF
                self.power_on = False
                self.power["bg"] = "gray"
                print("You turned power OFF")
            else:
                # Turn ON
                self.power_on = True
                self.power["bg"] = "red"
                print("You turned power ON")
    
    def confirm_exit(self):
        # Confirmation dialogue
        answer = askyesno(title="Exit", message="Are you sure?")
        if answer:
            # Stop application
            self.root.destroy()

### Main block
if __name__ == '__main__':
    # Start the application
    app=Panel(tkinter.Tk(), "SK2GJ Control Panel")
    app.mainloop()
