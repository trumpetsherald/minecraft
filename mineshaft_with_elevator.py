import command_chainer

FLOOR = 70
TOP = 241  # -1 subtract 1 if you start from top
FACES = "South"
FLOOR_SPACING = 4

LADDER_ORIENTATION = {
    "North": 2,
    "South": 3,
    "East": 5,
    "West": 4
}

SIGN_ORIENTATION = {
    "North": 2,
    "South": 3,
    "East": 5,
    "West": 4
}


def mark_the_location():
    commands = ["fill ~2 %s ~2 ~10 %s ~10 minecraft:carpet 9" % (FLOOR, FLOOR),
                "fill ~4 %s ~4 ~8 %s ~8 minecraft:carpet 1" % (FLOOR, FLOOR)]
    print command_chainer.chain_commands(commands)


def excavate_and_cap(commands):
    # Top + 1 to clear the carpet
    commands.append(
        "fill ~2 %s ~2 ~10 %s ~10 minecraft:air 0" % (FLOOR, TOP+1))
    commands.append(
        "fill ~2 %s ~2 ~10 %s ~10 minecraft:glass 0" % (TOP-2, TOP))


def build_elevator_enclosure(commands):
    commands.append(
        "fill ~4 %s ~4 ~8 %s ~8 minecraft:concrete 7" % (FLOOR, TOP))


def dig_shafts(commands):
    if FACES == "East" or FACES == "West":
        commands.append(
            "fill ~6 %s ~5 ~6 %s ~5 minecraft:air 0" % (FLOOR, TOP))
        commands.append(
            "fill ~6 %s ~7 ~6 %s ~7 minecraft:air 0" % (FLOOR, TOP))
    else:
        commands.append(
            "fill ~7 %s ~6 ~7 %s ~6 minecraft:air 0" % (FLOOR, TOP))
        commands.append(
            "fill ~5 %s ~6 ~5 %s ~6 minecraft:air 0" % (FLOOR, TOP))


def configure_up_shaft(commands):
    ladder = LADDER_ORIENTATION.get(FACES, 2)
    x = FLOOR + 2  # Ladder, cart, then opening if you want
    while x < TOP:
        if FACES == "East" or FACES == "West":
            commands.append(
                "setblock ~6 %s ~7 minecraft:ladder %s {Rotation:[90f,0f]}" %
                (x, ladder))
            commands.append("summon minecraft:minecart ~6 %s ~7" % (x+1))
        else:
            commands.append("setblock ~5 %s ~6 minecraft:ladder %s" %
                            (x, ladder))
            commands.append("summon minecraft:minecart ~5 %s ~6" % (x+1))

        x += FLOOR_SPACING


def configure_down_shaft(commands):
    brake = FLOOR + 2
    sign = SIGN_ORIENTATION.get(FACES, 2)
    if FACES == "East" or FACES == "West":
        commands.append(
            "setblock ~6 %s ~5 minecraft:wall_sign %s" % (brake, sign))
        commands.append("setblock ~6 %s ~5 minecraft:water 0" % (brake + 1))
    else:
        commands.append(
            "setblock ~7 %s ~6 minecraft:wall_sign %s" % (brake, sign))
        commands.append("setblock ~7 %s ~6 minecraft:water 0" % (brake + 1))


def make_bottom_entrance_exit(commands):
    if FACES == "North":
        commands.append(
            "fill ~7 %s ~4 ~7 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1))
        commands.append(
            "fill ~5 %s ~4 ~5 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1))
    elif FACES == "South":
        commands.append(
            "fill ~7 %s ~7 ~7 %s ~8 minecraft:air 0" % (FLOOR, FLOOR+1))
        commands.append(
            "fill ~5 %s ~7 ~5 %s ~8 minecraft:air 0" % (FLOOR, FLOOR+1))
    elif FACES == "East":
        commands.append(
            "fill ~7 %s ~5 ~8 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1))
        commands.append(
            "fill ~7 %s ~7 ~8 %s ~7 minecraft:air 0" % (FLOOR, FLOOR+1))
    else:
        commands.append(
            "fill ~5 %s ~5 ~4 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1))
        commands.append(
            "fill ~5 %s ~7 ~4 %s ~7 minecraft:air 0" % (FLOOR, FLOOR+1))


def make_top_entrance_exit():
    pass


def main():
    print "Do these two first from a command " \
          "block to mark where this will happen."
    mark_the_location()
    print "Paste these into a command block combiner " \
          "tool once you are sure where you want things."
    commands = []
    # excavate_and_cap(commands)
    build_elevator_enclosure(commands)
    dig_shafts(commands)
    configure_up_shaft(commands)
    configure_down_shaft(commands)
    make_bottom_entrance_exit(commands)
    make_top_entrance_exit()

    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
