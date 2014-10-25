# the goal of this game is to protect a ship from oncoming enemies.
# each turn a set number of enemies will be within shooting range.
# each enemy is given a name and a distance from the ship.
# all of this information is retrieved via stdin in their repective order.
# to target at shoot an enemy, its name must be printed to stdout.
# 
# the strategy chosen in this case is to always shoot the enemy that is closest.

# the algorithm for this strategy is contained within a standard game loop.
# the loop is to run continuall until there are no remaining enemies.
while True:
  # each cycle, initially the enemy count is read.
  # in addition a target object is constructed.
  enemies = int(input())  
  target = {
    'name': '', 
    'distance': -1
  }
  
  # target an enemy if its distance is smaller than any other enemy.
  for enemy in range(enemies):
    name, distance = input().split()
    distance = int(distance)
    if target['distance'] == -1 or distance < target['distance']:
      target['name'], target['distance'] = name, distance
      
  # by this point the targeted enemy is also the closest to the ship.
  # shoot the enemy by outputing its name to stdout.
  print(target['name'])