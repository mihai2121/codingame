while True:
  enemies = int(input())
  target = {
    'name': '', 
    'distance': -1
  }
  for enemy in range(enemies):
    name, distance = input().split()
    distance = int(distance)
    if target['distance'] == -1 or distance < target['distance']:
      target['name'], target['distance'] = name, distance
  print(target['name'])