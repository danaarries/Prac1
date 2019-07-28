#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Dana Arries>
Student Number: <ARRDAN001>
Prac: <1>
Date: <22/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from itertools import product #to access product function used create state LED values

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setting the button to increment LEDs
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setting the button to decrement LEDs

GPIO.setup(22,GPIO.OUT)   #setting the lowest bit LED
GPIO.setup(5,GPIO.OUT)    #setting the middle bit LED
GPIO.setup(6,GPIO.OUT)    #setting the highest bit LED

GPIO.output(22,0)    #ensure all LEDs are off when the programme starts
GPIO.output(5,0)
GPIO.output(6,0)


global state  #make an array of each state needed for binary counter
state=list(product([0,1], repeat=3))

global count #make a variabl counter to step through each state in array
count=0 #initialise the counter to 0 so all LEDs are off when programme starts

# Logic that you write
def main():
    GPIO.setwarnings(False) #set the warnings off and ensures main function has something in it so it runs
    
def callback_increment(channel): #the function to increase the value shown on the LEDs
    global count # call global count to access count variable
    count+=1 #when increment button is pressed  increase the count variable to access the next state in the array
    if (count==8):
       count=0 #ensures that LED value wraps around when counter reaches 8
    GPIO.output(22,state[count][2]) #lowest bit value assigned to this LED
    GPIO.output(5,state[count][1]) #middle bit value assigned to this LED
    GPIO.output(6,state[count][0])  #highest bit value assigned to this LED
    
def callback_decrement(channel): #the function to decrease the value shown on the LEDs
     global count # call global count to access count variable
     count-=1 #when decrement button is pressed decrease the count variable to access the previous state in the array
     if (count==-1):  #ensures that LED value wraps around when counter reaches -1
        count=7
     GPIO.output(22,state[count][2]) #lowest bit value assigned to this LED
     GPIO.output(5,state[count][1])  #middle bit value assigned to this LED
     GPIO.output(6,state[count][0])  #highest bit value assigned to this LED
     
GPIO.add_event_detect(17, GPIO.FALLING, callback=callback_increment,bouncetime=150) #call interrupt when increment button pressed (falling edge)
GPIO.add_event_detect(27, GPIO.FALLING, callback=callback_decrement,bouncetime=150)  #call interrupt when decrement button pressed (falling edge)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
       while True:
           main() #runs main function until programme is terminated

      #
       GPIO.output(22,0)
       GPIO.output(5,0)
       GPIO.output(6,0)

       GPIO.cleanup() #turns off GPIOs when main function ends
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup() 
#    except e:
#      print("Some other error occurred")
#      print(e.message) ##the programme wont run unless this except statement is commented out
