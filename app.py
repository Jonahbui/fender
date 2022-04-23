from pysabertooth import Sabertooth
from enum import Enum
import time

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
def turnRight():
  saber.drive(1, -15)
  saber.drive(2, -15)
#turn left function
def turnLeft():
  saber.drive(1, 15)
  saber.drive(2, 15)
#drive straight function
def goStraight():
  saber.drive(1, 15)
  saber.drive(2, -15)
#reverse function
def reverse():
  saber.drive(1, -15)
  saber.drive(2, 15)
# NOTE: sometimes switches from 9600 to 19200
saber = Sabertooth(port, baudrate, address)
print("Starting Fender")
saber.info()


def get_next_action():
    # if we need shit initialized then ACTIVATE

    # if we need to close properly before shutdown DEACTIVATE

    # if we are shutting down SHUTDOWN

    # if we are moving, decide how (FORWARD, REVERSE, TURN_LEFT, TURN_RIGHT...
    # SLOWDOWN, SPEEDUP, STOP)

    # if no other actions are occuring, then just IDLE
    return Action.IDLE

while(True):
    user_input = input("> ").strip()
    if user_input == "stop" or user_input == "exit" or user_input == "quit":
        break
    elif user_input == "turn right":
        turnRight()
    elif user_input == "turn left":
        turnLeft()
    elif user_input == "reverse":
        reverse()
    elif user_input == "go straight":
        goStraight()

    action = get_next_action()

    if action == Action.IDLE:
        pass
    elif action == Action.ACTIVATE:
        # Some code to initialize sensors/cameras
        pass
    elif action == Action.STOP:
        saber.stop()
    elif action == Action.DEACTIVATE:
        pass
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

