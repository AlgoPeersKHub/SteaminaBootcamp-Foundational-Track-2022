"""

## Introduction

Ever wondered how you could visualize the temperature using your micro:bit? 

This project allows you to do just that! You'll explore the temperature sensor, buttons, and LEDs of the micro:bit.



## Parts of the Micro:bit

1. **Temperature Sensor:** Measures and provides temperature data.
2. **LEDs (Light Emitting Diode):** Displays temperature-related information.
3. **Buttons:** Input for interaction with the micro:bit.


## Programming Concepts

 **Function:** A reusable block of code that performs a specific task.Exampe: Line 38


## Programming Language

  Python


## Coding Environment / Text Editor

  [Microsoft MakeCode Editor](https://makecode.microbit.org/#editor)


**Feel free to comment or contribute**

"""



# Project Code / Program ...

def on_button_pressed_ab():   # Define a function to display the temperature when both buttons A and B are pressed
    basic.show_number(input.temperature())

input.on_button_pressed(Button.AB, on_button_pressed_ab) # An event handler for the A and B buttons

