import game_framework
import game_world
import play_state
import player
import ai

among, dog, ghost, hulk, human, icarus, kirby, ninja, patrick_star, pikachu, sonic, spiderman, turtle, witch, zombie = range(15)
VERY_SLOW, SLOW, NORMAL, FAST, VERY_FAST = 1, 1.5, 2, 2.5, 3
def use_skill(character):
    match character.character_name:
        case "among":
            skill_speed_up(character, VERY_FAST)
        case "human":
            skill_throw_obstacle(character)
        case "iacrus":
            skill_throw_obstacle(character)
        case "ninja":
            skill_teleport(character)
        case "sonic":
            skill_speed_up(character, VERY_FAST)
        case "witch":
            skill_set_speed_all(VERY_SLOW)



def skill_teleport(character, x):
    character.x += x


def skill_speed_up(character, value):
    character.buff = True
    character.speed = value


def skill_build_obstacle(character, obstacle):
    game_world.add_object(obstacle, 1)


def skill_throw_obstacle(character):
    pass

def skill_remove_debuff(character):
    pass

def skill_set_speed_all(character, value):
    for obj in game_world.all_objects():
        if type(obj) == ai.AI or type(obj) == player.Player:
            if obj is not character:
                obj.debuff = True
                obj.set_speed(value)

