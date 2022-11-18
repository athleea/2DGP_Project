key_Idle, key_Run, key_Sturn, key_Skill, key_Speed, key_Cool_Time, key_Hording_Time, method_Skill = range(8)

PIXEL_PER_METER = (50.0 / 0.3)

VERY_SLOW, SLOW, NORMAL, FAST, VERY_FAST = 1, 1.5, 2, 2.5, 3

among, dog, ghost, hulk, human, icarus, kirby, ninja, patrick_star, pikachu, sonic, spiderman, turtle, witch, zombie = range(15)


def get_speed_pps(RUN_SPEED_KMPH):
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    return RUN_SPEED_PPS


characters = {
    patrick_star: {
        "name": "PatrickStar",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 7, "bottom": 120, "width": 30, "height": 50},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 9, "bottom": 60, "width": 32, "height": 50},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 4, "bottom": 0, "width": 40, "height": 50},
        key_Skill: None,
        key_Speed: get_speed_pps(NORMAL),
        key_Cool_Time: 0,
    }, sonic: {
        "name": "sonic",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 174, "width": 30, "height": 40},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 8, "bottom": 126, "width": 42, "height": 38},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 2, "bottom": 71, "width": 40, "height": 45},
        key_Skill: {"ActionPerTime": 0, "FramePerAction": 6, "bottom": 0, "width": 32, "height": 27},
        key_Speed: get_speed_pps(FAST),
        key_Cool_Time: 10,
        key_Hording_Time: 5
    }, hulk: {
        "name": "hulk",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 3, "bottom": 200, "width": 60, "height": 90},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 6, "bottom": 100, "width": 90, "height": 90},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 5, "bottom": 0, "width": 100, "height": 90},
        key_Skill: None,
        key_Speed: get_speed_pps(SLOW),
        key_Cool_Time: 0,
    }, kirby: {
        "name": "kirby",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 6, "bottom": 85, "width": 50, "height": 40},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 45, "width": 50, "height": 40},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 4, "bottom": 0, "width": 50, "height": 45},
        key_Skill: None,
        key_Speed: get_speed_pps(FAST),
        key_Cool_Time: 0,
    }, turtle: {
        "name": "turtle",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 5, "bottom": 56, "width": 70, "height": 47},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 6, "bottom": 0, "width": 70, "height": 46},
        key_Sturn: None,
        key_Skill: None,
        key_Speed: get_speed_pps(VERY_SLOW),
        key_Cool_Time: 0,
    }, ghost: {
        "name": "ghost",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 8, "bottom": 65, "width": 75, "height": 63},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 6, "bottom": 0, "width": 75, "height": 55},
        key_Sturn: None,
        key_Skill: None,
        key_Speed: get_speed_pps(FAST),
        key_Cool_Time: 0,
    }, pikachu: {
        "name": "pikachu",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 85, "width": 60, "height": 45},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 50, "width": 60, "height": 35},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 3, "bottom": 0, "width": 60, "height": 50},
        key_Skill: None,
        key_Speed: get_speed_pps(NORMAL),
        key_Cool_Time: 0,
    }, among: {
        "name": "among",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 1, "bottom": 110, "width": 30, "height": 25},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 75, "width": 30, "height": 25},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 4, "bottom": 35, "width": 30, "height": 30},
        key_Skill: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 0, "width": 30, "height": 25},
        key_Speed: get_speed_pps(NORMAL),
        key_Cool_Time: 10,
        key_Hording_Time: 5,
    }, dog: {
        "name": "dog",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 2, "bottom": 150, "width": 100, "height": 45},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 7, "bottom": 85, "width": 100, "height": 65},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 6, "bottom": 0, "width": 100, "height": 85},
        key_Skill: None,
        key_Speed: get_speed_pps(FAST),
        key_Cool_Time: 0,
    }, human: {
        "name": "human",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 1, "bottom": 158, "width": 38, "height": 42},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 108, "width": 38, "height": 40},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 2, "bottom": 52, "width": 38, "height": 46},
        key_Skill: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 2, "bottom": 0, "width": 38, "height": 42},
        key_Speed: get_speed_pps(NORMAL),
        key_Cool_Time: 10,
        key_Hording_Time: 2,
    }, icarus: {
        "name": "icarus",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 204, "width": 65, "height": 60},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 6, "bottom": 144, "width": 65, "height": 60},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 8, "bottom": 84, "width": 65, "height": 60},
        key_Skill: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 24, "width": 65, "height": 60},
        key_Speed: get_speed_pps(VERY_FAST),
        key_Cool_Time: 10,
        key_Hording_Time: 2,
    }, ninja: {
        "name": "ninja",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 210, "width": 60, "height": 75},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 6, "bottom": 145, "width": 60, "height": 65},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 4, "bottom": 70, "width": 80, "height": 75},
        key_Skill: {"ActionPerTime": 1.5, "FramePerAction": 7, "bottom": 0, "width": 60, "height": 70},
        key_Speed: get_speed_pps(NORMAL),
        key_Cool_Time: 10,
        key_Hording_Time: 1,
    }, witch: {
        "name": "witch",
        key_Idle: {"ActionPerTime": 1, "FramePerAction": 5, "bottom": 305, "width": 100, "height": 95},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 2, "bottom": 205, "width": 100, "height": 100},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 5, "bottom": 120, "width": 110, "height": 85},
        key_Skill: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 0, "width": 100, "height": 120},
        key_Speed: get_speed_pps(FAST),
        key_Cool_Time: 10.0,
        key_Hording_Time: 0.5,
    }, zombie: {
        "name": "zombie",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 4, "bottom": 145, "width": 90, "height": 75},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 5, "bottom": 70, "width": 90, "height": 75},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 8, "bottom": 0, "width": 90, "height": 70},
        key_Skill: None,
        key_Speed: get_speed_pps(VERY_SLOW),
        key_Cool_Time: 0,
    }, spiderman: {
        "name": "spiderman",
        key_Idle: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 3, "bottom": 110, "width": 70, "height": 70},
        key_Run: {"ActionPerTime": 1.0 / 0.5, "FramePerAction": 8, "bottom": 50, "width": 70, "height": 60},
        key_Sturn: {"ActionPerTime": 0, "FramePerAction": 3, "bottom": 0, "width": 50, "height": 50},
        key_Skill: None,
        key_Speed: get_speed_pps(FAST),
        key_Cool_Time: 0,
    }, 
}

