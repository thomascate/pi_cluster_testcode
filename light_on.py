#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import signal
import sys
import time

pid_file = "/var/run/light_on"

f = open(pid_file, "w")
pid = str(os.getpid())
f.write("%s\n" % pid)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT, initial = 0)
GPIO.setup(15, GPIO.OUT, initial = 0)
p1 = GPIO.PWM(16, 1000)
p2 = GPIO.PWM(15, 1000)

dutyCycle = 0

p1.start(float(sys.argv[1]))
p2.start(float(sys.argv[2]))

def terminateProcess(signalNumber, frame):
  p1.stop()
  p2.stop()
  GPIO.cleanup()
  os.remove(pid_file)
  exit(0)

while True:
  signal.signal(signal.SIGTERM, terminateProcess)
  signal.signal(signal.SIGINT, terminateProcess)
