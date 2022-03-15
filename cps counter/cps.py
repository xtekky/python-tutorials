#importimg our modules
from pynput.mouse import Listener
import time

#defining variables
raw_clicks = 0 #click count
sec = 0.6 #refresh time - raw_clicks / sec = cps

print('click to start', end="")

#click to start function
def click_to_start(x, y, button, pressed):
    global start
    listener.stop() #stopping listener
    print("\r", end="") #erasing 'click to start'
    start = time.time() #starting time
    print('')

#listener function that is going to listen to the mouse input
with Listener(on_click=click_to_start) as listener:
    listener.join()


#while true loop to keep the code refreshing and printing a new cps value
while True:

    #main function that is going to calculate and print the cps
    def cps_counter(x, y, button, pressed):

        #enabeling the variables
        global start
        global sec
        global raw_clicks

        raw_clicks = raw_clicks + 1 #click count

        #function to stop the cps count and refresh with new value
        if time.time() - start > sec: #function to count time
            listener.stop() #stopping listener
            raw_raw = (raw_clicks/2) #dividing clicks because pynput listens to press and release so the value is doubled
            raw_raw = round(raw_raw/sec, 1) #calculating cps and rounding up to one decimal after comma - ex: 1.3
            print("\r", end="") # erasing previous cps value
            print(raw_raw, 'cps', end="") #printing ne cps value
            raw_clicks = 0 #resetting clicks
            start = time.time() # restarting timer


    # listener function that is going to listen to the mouse input
    with Listener(on_click=cps_counter) as listener:
        listener.join()
