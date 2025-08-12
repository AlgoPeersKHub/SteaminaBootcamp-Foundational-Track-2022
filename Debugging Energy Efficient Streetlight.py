## The provided energy-efficient streetlight program contains errors. 
## Your task is to identify, analyze, and correct these bugs to ensure the energy-efficient streetlight operates as intended

##Feel free to comment, contribute, or use the code for your project.
#You can use the same pins or change them—just be sure to update the code accordingly so your project works correctly."""


## Project code / program
def on_forever():
    if input.light_level() > 50:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
