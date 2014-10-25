import sys, math
from collections import defaultdict

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in input().split()]

elevator = defaultdict(list)
for i in range(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    elevatorFloor, elevatorPos = [int(i) for i in input().split()]
    elevator[elevatorFloor].append(elevatorPos)
    
print(nbAdditionalElevators, nbTotalClones, elevator, file=sys.stderr)

def act(action):
    global nbTotalClones
    global nbAdditionalElevators
    if action == 'BLOCK':
        nbTotalClones = nbTotalClones - 1
    elif action == 'ELEVATOR':
        elevator[cloneFloor].append(clonePos)
        nbAdditionalElevators = nbAdditionalElevators - 1
    print(action)

def closest(positionClone, positionElevators):
    return min(positionElevators, key=lambda x:abs(x - positionClone))

# game loop
while 1:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)
        
    if clonePos == width - 1 or clonePos == 0:  # has reached outer bounds.
        act('BLOCK')
    elif cloneFloor != exitFloor and cloneFloor not in elevator:  # floor is empty...
        if cloneFloor != -1:  # and clone exists.
            act('ELEVATOR')
        else:
            act('WAIT')
    elif cloneFloor == exitFloor:  # if floor has the exit....
        if clonePos < exitPos and direction == 'LEFT':  # and going opposite direction of exit.
            act('BLOCK')
        elif clonePos > exitPos and direction == 'RIGHT':  # and going opposite direction of exit.
            act('BLOCK')
        else:
            act('WAIT')
    elif cloneFloor in elevator:  # if floor has an elevator...
        if abs(clonePos - closest(clonePos, elevator[cloneFloor])) >= width / 2 and nbAdditionalElevators >= nbFloors - len(elevator):  # and elevator too far away.
            act('ELEVATOR')
        elif clonePos < closest(clonePos, elevator[cloneFloor]) and direction == 'LEFT':  # and going opposite direction of closest elevator.
            act('BLOCK')
        elif clonePos > closest(clonePos, elevator[cloneFloor]) and direction == 'RIGHT':  # and going opposite direction of closest elevator.
            act('BLOCK')
        else:
            act('WAIT')
    else:
      act("WAIT") # action: WAIT or BLOCK
      
    nbRounds = nbRounds - 1