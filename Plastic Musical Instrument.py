"""
## Introduction
Step into the world of music by creating your very own instruments using plastic bottles and the micro:bit. 
In this project, you'll turn recyclable plstic bottle into a symphony of sounds with just a touch!

## Micro:bit Parts Used
1. **Pins:** Connected to plastic bottles to create a musical instrument.
2. **LEDs (Light Emitting Diode):** Displays icons corresponding to different musical tones.

## Programming Concepts
Functions: Reusable blocks of code that perform specific tasks.

##Feel free to comment or contribute.
"""

## Project code / program
def on_pin_pressed_p0():  # Define a function to play a musical tune and show an icon when TouchPin.P0 is pressed
    # Play musical tones
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(311, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.HEART)  # Show the heart icon
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0) # Set up an event handler for TouchPin.P0

def on_pin_pressed_p2(): # Define a function to play a musical tune and show an icon when TouchPin.P2 is pressed
    # Play musical tones
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.YES)  # Show the YES icon
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2) # Set up an event handler for TouchPin.P2

def on_pin_pressed_p1(): # Define a function to play a musical tune and show an icon when TouchPin.P1 is pressed
    # Play musical tones
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.FABULOUS)   # Show the FABULOUS icon
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1) # Set up an event handler for TouchPin.P1
