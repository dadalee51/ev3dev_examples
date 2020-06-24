#!/usr/bin/micropython
#testing motor
import ev3dev2.motor as em
import ev3dev2 as e
import utime as t
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
spkr = Sound()
leds = Leds()
leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "GREEN")

m1= em.LargeMotor(em.OUTPUT_A)
m1.on(em.SpeedPercent(25))
t.sleep(1)
m1.off()
leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "RED")
t.sleep(0.1)
leds.set_color("LEFT", "RED")
leds.set_color("RIGHT", "GREEN")
t.sleep(0.1)
leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "GREEN")
spkr.play_song((
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),
    ('D5', 'h')
),tempo=220)