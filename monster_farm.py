import command_chainer

GROUND = 13
HEIGHT = 20
FACES = "South"
STOREYS = 4
C_HEIGHT = 6  # This is how tall each kill chamber is from channel to roof

HOPPER_ORIENTATION = {
    "North": 2,
    "South": 3,
    "East": 5,
    "West": 4
}

CHEST_ORIENTATION = {
    "North": 2,
    "South": 3,
    "East": 5,
    "West": 4
}


def mark_the_location():
    print "fill ~2 ~ ~2 ~5 ~ ~5 minecraft:carpet 11"


def build_shaft(commands):
    bottom = GROUND - 1
    glass_end = GROUND + 6
    commands.append("fill ~2 %s ~2 ~5 %s ~5 minecraft:glass 0 hollow" % (
        bottom, glass_end))
    commands.append("fill ~2 %s ~2 ~5 %s ~5 minecraft:cobblestone 0 hollow" % (
        glass_end, GROUND+HEIGHT))


def clear_spawner_space(commands):
    bottom = GROUND + HEIGHT
    top = (GROUND + HEIGHT) + (STOREYS * C_HEIGHT) - 1
    commands.append("fill ~13 %s ~13 ~-6 %s ~-6 minecraft:air 0" % (
        bottom, top))


def build_channel_floors(commands, storey=0):
    y = (GROUND+HEIGHT) + (storey*C_HEIGHT)
    commands.append("fill ~3 %s ~2 ~4 %s ~-5 minecraft:cobblestone 0" % (y, y))
    commands.append("fill ~4 %s ~5 ~3 %s ~12 minecraft:cobblestone 0" % (y, y))
    commands.append("fill ~5 %s ~3 ~12 %s ~4 minecraft:cobblestone 0" % (y, y))
    commands.append("fill ~2 %s ~3 ~-5 %s ~4 minecraft:cobblestone 0" % (y, y))


def build_channel_walls(commands, storey=0):
    y1 = (GROUND+HEIGHT+1) + (storey*C_HEIGHT)
    y2 = (GROUND+HEIGHT+2) + (storey*C_HEIGHT)
    # North channel walls
    commands.append(
        "fill ~2 %s ~2 ~2 %s ~-5 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~5 %s ~2 ~5 %s ~-5 minecraft:cobblestone 0" % (y1, y2))
    # South channel walls
    commands.append(
        "fill ~2 %s ~5 ~2 %s ~12 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~5 %s ~5 ~5 %s ~12 minecraft:cobblestone 0" % (y1, y2))
    # East channel walls
    commands.append(
        "fill ~6 %s ~2 ~12 %s ~2 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~6 %s ~5 ~12 %s ~5 minecraft:cobblestone 0" % (y1, y2))
    # West channel walls
    commands.append(
        "fill ~1 %s ~2 ~-5 %s ~2 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~1 %s ~5 ~-5 %s ~5 minecraft:cobblestone 0" % (y1, y2))


def build_channel_caps(commands, storey=0):
    y1 = (GROUND+HEIGHT + 1) + (storey*C_HEIGHT)
    y2 = (GROUND+HEIGHT + 2) + (storey*C_HEIGHT)
    # North
    commands.append(
        "fill ~3 %s ~-6 ~4 %s ~-6 minecraft:cobblestone 0" % (y1, y2))
    # South
    commands.append(
        "fill ~3 %s ~13 ~4 %s ~13 minecraft:cobblestone 0" % (y1, y2))
    # East
    commands.append(
        "fill ~13 %s ~3 ~13 %s ~4 minecraft:cobblestone 0" % (y1, y2))
    # West
    commands.append(
        "fill ~-6 %s ~3 ~-6 %s ~4 minecraft:cobblestone 0" % (y1, y2))


def build_floors(commands, storey=0):
    y = (GROUND+HEIGHT+2) + (storey*C_HEIGHT)
    commands.append(
        "fill ~6 %s ~1 ~12 %s ~-5 minecraft:cobblestone 0" % (y, y))
    commands.append(
        "fill ~1 %s ~1 ~-5 %s ~-5 minecraft:cobblestone 0" % (y, y))
    commands.append(
        "fill ~6 %s ~6 ~12 %s ~12 minecraft:cobblestone 0" % (y, y))
    commands.append(
        "fill ~1 %s ~6 ~-5 %s ~12 minecraft:cobblestone 0" % (y, y))


def build_walls(commands, storey=0):
    y1 = (GROUND+HEIGHT + 3) + (storey*C_HEIGHT)
    y2 = (GROUND+HEIGHT + 4) + (storey*C_HEIGHT)
    commands.append(
        "fill ~-6 %s ~-6 ~13 %s ~-6 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~-6 %s ~13 ~13 %s ~13 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~13 %s ~-5 ~13 %s ~12 minecraft:cobblestone 0" % (y1, y2))
    commands.append(
        "fill ~-6 %s ~-5 ~-6 %s ~12 minecraft:cobblestone 0" % (y1, y2))


def set_trap_doors(commands, storey=0):
    y = (GROUND+HEIGHT + 2) + (storey*C_HEIGHT)
    commands.append("fill ~-5 %s ~3 ~12 %s ~3 minecraft:trapdoor 13" % (y, y))
    commands.append("fill ~-5 %s ~4 ~12 %s ~4 minecraft:trapdoor 12" % (y, y))
    commands.append("fill ~4 %s ~-5 ~4 %s ~12 minecraft:trapdoor 14" % (y, y))
    commands.append("fill ~3 %s ~-5 ~3 %s ~12 minecraft:trapdoor 15" % (y, y))
    commands.append("fill ~3 %s ~3 ~4 %s ~4 minecraft:air 0" % (y, y))


def place_waters(commands):
    top = (GROUND + HEIGHT) + (STOREYS * C_HEIGHT) - 2
    commands.append(
        "fill ~13 %s ~13 ~-6 %s ~-6 minecraft:air 0 replace minecraft:water" %
        (GROUND, top))
    x = 0
    while x < STOREYS:
        y = (GROUND+HEIGHT + 1) + (x*C_HEIGHT)
        commands.append("fill ~3 %s ~-5 ~4 %s ~-5 minecraft:water 0" % (y, y))
        commands.append("fill ~3 %s ~12 ~4 %s ~12 minecraft:water 0" % (y, y))
        commands.append("fill ~12 %s ~3 ~12 %s ~4 minecraft:water 0" % (y, y))
        commands.append("fill ~-5 %s ~3 ~-5 %s ~4 minecraft:water 0" % (y, y))
        x += 1


def build_roof(commands, storey=0):
    y = (GROUND + HEIGHT + 5) + (storey * C_HEIGHT)
    commands.append(
        "fill ~-5 %s ~-5 ~12 %s ~12 minecraft:cobblestone 0" % (y, y))


def build_kill_platform(commands):
    y1 = GROUND+1
    glass_end = GROUND + 6
    top = (GROUND + HEIGHT) + (STOREYS * C_HEIGHT) - 2
    hopper = HOPPER_ORIENTATION.get(FACES, 2)
    chest = CHEST_ORIENTATION.get(FACES, 2)
    commands.append("fill ~3 %s ~3 ~4 %s ~4 minecraft:stone_slab 0" % (y1, y1))
    commands.append(
        "fill ~3 %s ~3 ~4 %s ~4 minecraft:hopper %s" % (GROUND, GROUND, hopper)
    )

    if FACES == "North":
        commands.append("fill ~3 %s ~2 ~4 %s ~2 minecraft:chest %s" % (
                GROUND, GROUND, chest))
    elif FACES == "South":
        commands.append("fill ~3 %s ~5 ~4 %s ~5 minecraft:chest %s" % (
            GROUND, GROUND, chest))
    elif FACES == "East":
        commands.append("fill ~5 %s ~3 ~5 %s ~4 minecraft:chest %s" % (
            GROUND, GROUND, chest))
    else:
        commands.append("fill ~2 %s ~3 ~2 %s ~4 minecraft:chest %s" % (
            GROUND, GROUND, chest))

    commands.append(
        "fill ~3 %s ~3 ~4 %s ~4 minecraft:air 0" % (glass_end, top))
    

def main():
    print "Use this one to mark where the fun will happen."
    mark_the_location()
    print "Paste these into a command block combiner " \
          "tool once you are sure where you want things."
    commands = list()
    build_shaft(commands)
    clear_spawner_space(commands)
    x = 0
    while x < STOREYS:
        build_channel_floors(commands, x)
        build_channel_walls(commands, x)
        build_channel_caps(commands, x)
        build_floors(commands, x)
        build_walls(commands, x)
        set_trap_doors(commands, x)
        # place_waters(x)
        build_roof(commands, x)
        x += 1

    place_waters(commands)

    build_kill_platform(commands)

    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
