"""

## Introduction
How does it feel when you express your emotions using emojis while chatting with friends? 
Imagine being able to create emojis yourself! 
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

**Feel free to comment or contribute**"""


#Below is the Project Code / Program ...

def on_button_pressed_a():
    basic.show_icon(IconNames.HEART) #feeling loved
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.ASLEEP) #feeling sleepy
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HAPPY) #feeling happy
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_icon(IconNames.FABULOUS) #feeling fabulous
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)#feeling surprised
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_pin_pressed_p0():
    basic.show_icon(IconNames.SAD) #feeling sad
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

