# to implement: http://www.redblobgames.com/pathfinding/a-star/introduction.html
import sys as s
import collections as c

state = [int(x) for x in input().split()]
Point = c.namedtuple('Point', 'x y')
light, thor = Point(state[0], state[1]), Point(state[2], state[3])
print(light, thor, file=s.stderr)

def update_direction(position, goal):
    direction = ''
    if position.x < goal.x and position.y < goal.y:
        direction = 'SE'
    elif position.x > goal.x and position.y < goal.y:
        direction = 'SW'
    elif position.x < goal.x and position.y > goal.y:
        direction = 'NE'
    elif position.x < goal.x and position.y > goal.y:
        direction = 'NW'
    elif position.x < goal.x and position.y == goal.y:
        direction = 'E'
    elif position.x > goal.x and position.y == goal.y:
        direction = 'W'
    elif position.x == goal.x and position.y < goal.y: 
        direction = 'S'
    elif position.x == goal.x and position.y > goal.y:
        direction = 'N'
    return direction
        
def update_position(position, direction):
    return {
        'N': Point(position.x, position.y - 1),
        'NE': Point(position.x + 1, position.y - 1),
        'E': Point(position.x + 1, position.y),
        'SE': Point(position.x + 1, position.y + 1),
        'S': Point(position.x, position.y + 1),
        'SW': Point(position.x - 1, position.y + 1),
        'W': Point(position.x - 1, position.y),
        'NW': Point(position.x - 1, position.y - 1)
    }[direction]
    
while light != thor:
    direction = update_direction(thor, light)
    print(direction)
    thor = update_position(thor, direction)
