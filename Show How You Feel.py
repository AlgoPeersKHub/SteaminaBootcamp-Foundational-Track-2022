"""

## Introduction

How does it feel when you express your emotions using emojis while chatting with friends? Imagine being able to create emojis yourself! 

In this project, you'll learn how to write a program to display your feelings on your micro:bit.


## Parts of the Micro:bit used

1. **LEDs (Light Emitting Diode):** Displays your emotions.
2. **Buttons:** Input for sending information to the micro:bit.


## Programming Concepts

**Function:** A reusable block of code that performs a specific task. In this program, a forever function makes your emoji loop or repeat.


## Programming Language

 **Python**


## Coding Environment / Text Editor

[Microsoft MakeCode Editor](https://makecode.microbit.org/#editor)


**Feel free to comment or contribute**

"""



# Project Code / Program ...

def on_button_pressed_a():
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)



