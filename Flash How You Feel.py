"""
## Introduction

The objective of this project is to bring your emotions to life by creating animated emojis that flash on the micro:bit.


Parts of the micro:bit used

  Accelerometer Sensor: Detects micro:bit shakes to express your emotions.
   
  LEDs: Output that visually displays your emotions on the micro:bit.


Programming concepts

  Function:  A function is a reusable block of code that performs a specific task or a set of tasks. Example: Line 40

   Loop :  Loops help computers do things repeatedly or over and over again. Example Line 42

          There are differnt types of loops the one used in the above program is called **for loop**. 
          
          **For Loop: It's like telling the micro:bit, "Display how I feel four(4) times.**


Programming Language
       Python


Text Editor / Coding Environment
      [Microsoft Makecode for Micro:bit](https://makecode.microbit.org/#editor)


** Feel free to comment or contribute**
"""



# Project Code / Program ...


def on_gesture_shake():  # Display a sequence of icons when the micro:bit is shaken
    
    for index in range(4):
        basic.show_icon(IconNames.HAPPY)   # Show a happy face :smile:
        basic.pause(1000)                  # Pause for 1 second
        basic.show_icon(IconNames.SAD)     # Show a sad face :sad:
        basic.pause(2000)                  # Pause for 2 seconds
        basic.show_icon(IconNames.SURPRISED)  # Show a surprised face
        basic.pause(5000)                  # Pause for 5 seconds
        basic.show_icon(IconNames.ASLEEP)  # Show a sleeping face

input.on_gesture(Gesture.SHAKE, on_gesture_shake)  # Set up an event handler for the SHAKE gesture









