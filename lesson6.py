#!/usr/bin/python3
#testing motor
import ev3dev2.motor as em
import time as t
m1= em.LargeMotor(em.OUTPUT_A)
m2= em.LargeMotor(em.OUTPUT_B)
m3= em.LargeMotor(em.OUTPUT_C)
m4= em.LargeMotor(em.OUTPUT_D)
m1.on(em.SpeedPercent(25))
m2.on(em.SpeedPercent(25))
m3.on(em.SpeedPercent(25))
m4.on(em.SpeedPercen(25))
t.sleep(1)
m1.off()
m2.off()
m3.off()
m4.off()


