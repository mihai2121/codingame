#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CodingGame: Onboarding

The goal of this game is to protect a ship from oncoming enemies.
Each turn a set number of enemies will be within shooting range.
Each enemy has a name and a distance from the ship.
This information fills the stdin buffer in their respective order.
To target and shoot an enemy, the program must print its name to stdout.

The strategy chosen in this case is to always shoot the enemy that is closest.
The algorithm for this strategy runs within a standard game loop.
The loop is to run until there are no remaining enemies.

Each cycle, the program detects enemies within range.
An enemy is then set as the target object if its distance is smaller than any of
    the other enemies.

By this point the targeted enemy is also the closest to the ship.
Thus, the program then shoots the enemy by outputting its name to stdout.
"""


def main():
    """Setup and run the game loop."""
    while True:
        target = detect()
        for _ in range(2):
            target_new = detect(str(input()), int(input()))
            target = choose(target, target_new)
        target = shoot(target)


def choose(target_a, target_b):
    """Choose the target with the smallest distance.
    
    Args:
        target_a (dict): A dictionary containing first target's name and
            distance.
        target_b (dict): A dictionary containing second target's name and
            distance.
    Returns:
        dict: A dictionary containing the closest target's name and distance.
    """
    target = target_a
    if (target_a['distance'] == -1 or
            target_b['distance'] < target_a['distance']):
        target = target_b
    return target


def shoot(target):
    """Shoot at the specified target.
    
    Args:
        target (dict): A dictionary containing the target name and distance.
        
    Returns:
        dict: A dictionary containing the target name and distance.
    """
    print(target['name'])
    return target


def detect(name='', distance=-1):
    """Detect and create a new target.
    
    Args:
        name (str): The name of the target.
        distance (int): The target's distance is from the player.
        
    Returns:
        dict: A dictionary containing the target's name and distance.
    """
    return {
        'name': name,
        'distance': distance
    }


if __name__ == '__main__':
    main()
