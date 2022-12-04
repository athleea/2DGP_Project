import game_world
import player
import ai
import fireball
import knife
import server
from character_data import *

debuff = 1

def use_skill(character):
    match character.character_name:
        case "among":
            skill_speed_up(character, get_speed_pps(5))
        case "human":
            k = knife.Knife(character.x+40, character.y, character.char_id)
            skill_throws(k)
        case "icarus":
            fire_ball = fireball.FireBall(character.x+40, character.y, character.char_id)
            skill_throws(fire_ball)
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

def skill_teleport(character, distance):
    character.x += distance

def skill_speed_up(character, value):
    character.buff = True
    character.set_speed(value)

def skill_throws(obj):
    game_world.add_object(obj, 2)
    game_world.add_collision_pairs(server.player, obj, "character:throws")
    game_world.add_collision_pairs(server.ai, obj, "character:throws")

def skill_remove_debuff(character):
    character.debuff.clear()
    character.set_default_speed()

def skill_set_speed_all(character, value):
    for obj in game_world.all_objects():
        if obj == character:
            continue
        elif type(obj) == ai.AI or type(obj) == player.Player:
            obj.debuff.append(debuff)
            obj.set_speed(value)

def skill_end_set_speed_all(character):
    for obj in game_world.all_objects():
        if obj == character:
            continue
        elif type(obj) == ai.AI or type(obj) == player.Player:
            if obj.debuff:
                obj.debuff.pop()
            obj.set_default_speed()

def skill_end_speed_up(character):
    character.buff = False
    character.set_default_speed()