# The goal of this game is to protect a ship from oncoming enemies. 
# Each turn a set number of enemies will be within shooting range. 
# Each enemy has a name and a distance from the ship. 
# This information fills the stdin buffer in their respective order. 
# To target and shoot an enemy, the program must print its name to stdout.
# 
# The strategy chosen in this case is to always shoot the enemy that is closest.
# The algorithm for this strategy runs within a standard game loop. 
# The loop is to run until there are no remaining enemies.
while True:
  # Each cycle, the program reads the initial enemy count. 
  # It also constructs a target object.
  enemies = int(input())  
  target = {
    'name': '', 
    'distance': -1
  }
  
  # An enemy is then set as the target object if its distance is smaller than any of the other enemies.
  for enemy in range(enemies):
    name, distance = input().split()
    distance = int(distance)
    if target['distance'] == -1 or distance < target['distance']:
      target['name'], target['distance'] = name, distance
      
  # By this point the targeted enemy is also the closest to the ship.
  # Thus, the program then shoots the enemy by outputting its name to stdout.
  print(target['name'])