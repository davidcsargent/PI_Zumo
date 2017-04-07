# import curses
import curses
from gpiozero import OutputDevice
from time import sleep

a = OutputDevice(4)
b = OutputDevice(17)
c = OutputDevice(27)


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                print "forward"
                a.on()
                sleep(1)
                a.off()
            elif char == curses.KEY_DOWN:
                print "back"
            elif char == curses.KEY_RIGHT:
                print "right"
            elif char == curses.KEY_LEFT:
                print "left"
            elif char == 10:
                print "stop"    
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

