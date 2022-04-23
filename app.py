import time
from enum import Enum
from pysabertooth import Sabertooth


# Sabertooth connection info
port = '/dev/serial/by-id/usb-Dimension_Engineering_Sabertooth_2x32_160089D22190-if01'
baudrate=9600
address=128


# Actions
class Action(Enum):
    IDLE = 1
    STOP = 2
    ACTIVATE = 3
    DEACTIVATE = 4
    FORWARD = 5
    REVERSE = 6
    TURN_LEFT = 7
    TURN_RIGHT = 8
    SLOWDOWN = 9
    SPEEDUP = 10


#simple turn right function
def turn_right():
  saber.drive(1, -15)
  saber.drive(2, -15)
  
  
#turn left function
def turn_left():
  saber.drive(1, 15)
  saber.drive(2, 15)
  
  
#drive straight function
def go_forward():
  saber.drive(1, 15)
  saber.drive(2, -15)
  
  
#reverse function
def reverse():
  saber.drive(1, -15)
  saber.drive(2, 15)


def get_next_action():
    # If we need something initialized then ACTIVATE

    # If we need to close properly before shutdown DEACTIVATE

    # If we are shutting down SHUTDOWN

    # If we are moving, decide how (FORWARD, REVERSE, TURN_LEFT, TURN_RIGHT...
    # SLOWDOWN, SPEEDUP, STOP)

    # If no other actions are occuring, then just IDLE
    return Action.IDLE


def main():
    # NOTE: sometimes switches from 9600 to 19200
    saber = Sabertooth(port, baudrate, address)
    print("Starting Fender")
    saber.info()
    
    # TODO: check PID to determine which branch to take
    if(True):
        while(True):
            user_input = input("> ").strip()
            if user_input == "stop" or user_input == "exit" or user_input == "quit":
                break
            elif user_input == "turn right":
                turn_right()
            elif user_input == "turn left":
                turn_left()
            elif user_input == "reverse":
                reverse()
            elif user_input == "go forward":
                go_forward()
    else:
        while(True):
            # TODO: split into child process
            action = get_next_action()

            if action == Action.IDLE:
                pass
            elif action == Action.ACTIVATE:
                # Some code to initialize sensors/cameras
                pass
            elif action == Action.STOP:
                saber.stop()
            elif action == Action.DEACTIVATE:
                saber.stop()
                break
            elif action == Action.FORWARD:
                pass
            elif action == Action.REVERSE:
                pass
            elif action == Action.TURN_LEFT:
                pass
            elif action == Action.TURN_RIGHT:
                pass
            elif action == Action.SPEEDUP:
                pass
            elif action == Action.SLOWDOWN:
                pass
    print("Stopping Fender")
    saber.stop()

if __name__ == "__main__":
    main()