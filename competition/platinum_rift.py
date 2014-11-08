import sys as s

  
def read_zone(id_, zones):
    match = None
    matches = list(filter(lambda z: z['id'] == id_, zones))
    if len(matches) > 0:
        match = matches[0]
        if len(matches) > 1:
            print('warning: found duplicate zone ids.', file=s.stderr)
    return match


def create_zone(id_, platinum, enemies=0, friends=0, owner=-1, paths=set()):
    return {
        'enemies': enemies,
        'friends': friends,
        'id': id_,
        'owner': owner,
        'paths': paths,
        'platinum': platinum
    }


def write_zone(zone, zones):
    zones = list(filter(lambda z: z['id'] != zone['id'], zones))
    zones.append(zone)
    return zones


zones = []
playerCount, myId, zoneCount, linkCount = [int(i) for i in input().split()]
for i in range(zoneCount):
    id_, platinum = [int(i) for i in input().split()]
    zone = create_zone(id_, platinum)
    print(zone, file=s.stderr)
    zones = write_zone(zone, zones)
for i in range(linkCount):
    source, target = [int(i) for i in input().split()]
    zone = read_zone(source, zones)
    zone['paths'].add(target)
    zones = write_zone(zone, zones)
while 1:
    platinum = int(input())
    for i in range(zoneCount):
        zId, ownerId, podsP0, podsP1, podsP2, podsP3 = [int(i) for i in input().split()]
    print("WAIT")
    print("1 73")