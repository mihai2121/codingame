import random as r
import sys as s
r.seed()

  
def read_zone(id_, zones):
    match = None
    matches = list(filter(lambda z: z['id'] == id_, zones))
    if len(matches) > 0:
        match = matches[0]
        if len(matches) > 1:
            print('warning: found duplicate zone ids.', file=s.stderr)
    return match


def create_zone(id_, platinum, enemies=0, friends=0, owner=-1, paths=None):
    return {
        'enemies': enemies,
        'friends': friends,
        'id': id_,
        'owner': owner,
        'paths': paths if paths is not None else set(),
        'platinum': platinum
    }


def write_zone(zone, zones):
    zones = list(filter(lambda z: z['id'] != zone['id'], zones))
    zones.append(zone)
    return zones


def update_zone(id_, enemies, friends, owner, zones):
    zone = read_zone(id_, zones)
    zone['enemies'] = enemies
    zone['friends'] = friends
    zone['owner'] = owner
    return write_zone(zone, zones)
    

def suggest_move(zone):
    move, target = '', ''
    if len(zone['paths']) > 0:
        target = r.sample(zone['paths'], 1)[0]
        move = str(zone['friends']) + ' ' + str(zone['id']) + ' ' + str(target)
    return move
    
def is_safe(id_):
    # ensure enemies are not within one turns' range.
    pass
    
def suggest_spawn(zones):
    spawn = '1 102'
    return spawn


zones = []
playerCount, myId, zoneCount, linkCount = [int(i) for i in input().split()]
for i in range(zoneCount):
    id_, platinum = [int(i) for i in input().split()]
    zone = create_zone(id_, platinum)
    zones = write_zone(zone, zones)
for i in range(linkCount):
    source, target = [int(i) for i in input().split()]
    zone = read_zone(source, zones)
    zone['paths'].add(target)
    print(source, target, zone, file=s.stderr)
    zones = write_zone(zone, zones)
while 1:
    moves = []
    spawns = []
    platinum = int(input())
    for _ in range(int(platinum / 20)):
        spawn = suggest_spawn(zones)
        spawns.append(spawn)
    for i in range(zoneCount):
        zId, ownerId, podsP0, podsP1, podsP2, podsP3 = [int(i) for i in input().split()]
        players = [podsP0, podsP1, podsP2, podsP3]
        enemies = sum(players[:myId] + players[myId + 1:])
        friends = players[myId]
        update_zone(zId, enemies, friends, ownerId, zones)
    for zone in zones:
        if zone['friends'] > 0:
            move = suggest_move(zone)
            moves.append(move)
    print(' '.join(moves) if len(moves) > 0 else 'WAIT')
    print(' '.join(spawns) if len(spawns) > 0 else 'WAIT')