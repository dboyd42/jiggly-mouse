#!/usr/bin/env python3
# Copyright 2022 David Boyd, all rights reserved
# Program: jiggly-mouse.py
# Description:
#     Jiggles the mouse to prevent device from sleeping.
# Date: 2022-03-15
# Revised:

import tkinter as tk
import pyautogui as mouse

##################
### JigglyPuff ###
##################
class JigglyPuff:
    def __init__(self):

        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title('Jiggly Mouse')
        self.main_window.geometry('500x500')

        # Create the frame to group widgets
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create a label widgets containing the instructions
        self.start_label = tk.Label(self.top_frame, \
                                    text='START: Click \'Jiggle Me!\' to begin jiggling.')
        self.stop_label = tk.Label(self.top_frame, \
                                    text='STOP: Jiggle the mouse to stop me jiggling.')
        self.quit_label = tk.Label(self.top_frame, \
                                    text='QUIT: Click \'QUIT\' to exit the program.')

        # Pack the top frame's widgets
        self.start_label.pack(side='top')
        self.stop_label.pack(side='top')
        self.quit_label.pack(side='top')

        # Create the button widgets for the main frame
        self.run_button = tk.Button(self.bottom_frame, \
                                    text='Jiggle Me!', \
                                    command=self.jiggle)
        self.quit_button = tk.Button(self.bottom_frame, \
                                            text='Quit', \
                                            command=self.main_window.destroy)

        # Pack the buttons
        self.run_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tk main loop
        tk.mainloop()

    ##############
    ### jiggle ###
    ##############
    def jiggle(self):
        '''The jiggle method is a callback fns for the for the Run button'''

        # Declare and init coordinates
        x1, y1 = x2, y2 = mouse.position()  # Current mouse position
        range = 100                         # Out-of-bounds range
        x1_min = x1-range
        x1_max = x1+range
        y1_min = y1-range
        y1_max = y1+range

        # Jiggle the mouse from left to right
        #   Break when out of range
        while (x1_min < x2 < x1_max) and (y1_min < y2 < y1_max):
            mouse.moveRel(10, 0)
            mouse.moveRel(-10, 0)

            # Get new position of mouse
            x2, y2 = mouse.position()

##############
### Main() ###
##############

if __name__ == "__main__":
    # Create an instance of the JigglyPuff class
    i_am_jiggly_puff = JigglyPuff()

