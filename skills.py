import game_framework
import game_world
import play_state
import player
import ai
from character_data import *

debuff = 1

def use_skill(character):
    match character.character_name:
        case "among":
            skill_speed_up(character, get_speed_pps(5))
        case "human":
            skill_throw_obstacle(character)
        case "iacrus":
            skill_throw_obstacle(character)
        case "ninja":
            skill_teleport(character, 400)
        case "sonic":
            skill_speed_up(character, get_speed_pps(5))
        case "witch":
            skill_set_speed_all(character, VERY_SLOW)

def use_end_skill(character):
    match character.character_name:
        case "among":
            skill_end_speed_up(character)
        case "sonic":
            skill_end_speed_up(character)
        case "witch":
            skill_end_set_speed_all(character)

def skill_teleport(character, x):
    character.x += x


def skill_speed_up(character, value):
    character.buff = True
    character.set_speed(value)

def skill_build_obstacle(character, obstacle):
    game_world.add_object(obstacle, 1)


def skill_throw_obstacle(character):
    pass

def skill_remove_debuff(character):
    character.debuff.clear()
    character.set_default_speed()

def skill_set_speed_all(character, value):
    for obj in game_world.all_objects():
        if obj == character:
            continue
        if type(obj) == ai.AI or type(obj) == player.Player:
            obj.debuff.append(debuff)
            obj.set_speed(value)

def skill_end_set_speed_all(character):
    for obj in game_world.all_objects():
        if obj == character:
            continue
        if type(obj) == ai.AI or type(obj) == player.Player:
            if obj.debuff:
                obj.debuff.pop()
            obj.set_default_speed()

def skill_end_speed_up(character):
    character.set_default_speed()