FLOOR = 12
TOP = 63-1
FACES = "East"
FIRST_FLOOR = 15
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
    print "fill ~2 ~ ~2 ~10 ~ ~10 minecraft:carpet 9"
    print "fill ~4 ~ ~4 ~8 ~ ~8 minecraft:carpet 1"


def excavate_and_cap():
    # Top + 1 to clear the carpet
    print "fill ~2 %s ~2 ~10 %s ~10 minecraft:air 0" % (FLOOR, TOP+1)
    print "fill ~2 %s ~2 ~10 %s ~10 minecraft:glass 0" % (TOP-2, TOP)


def build_elevator_enclosure():
    print "fill ~4 %s ~4 ~8 %s ~8 minecraft:planks 0" % (FLOOR, TOP)


def dig_shafts():
    if FACES == "East" or FACES == "West":
        print "fill ~6 %s ~5 ~6 %s ~5 minecraft:air 0" % (FLOOR, TOP)
        print "fill ~6 %s ~7 ~6 %s ~7 minecraft:air 0" % (FLOOR, TOP)
    else:
        print "fill ~7 %s ~6 ~7 %s ~6 minecraft:air 0" % (FLOOR, TOP)
        print "fill ~5 %s ~6 ~5 %s ~6 minecraft:air 0" % (FLOOR, TOP)


def configure_up_shaft():
    ladder = LADDER_ORIENTATION.get(FACES, 2)
    x = FIRST_FLOOR
    while x < TOP:
        if FACES == "East" or FACES == "West":
            print "setblock ~6 %s ~7 minecraft:ladder %s {Rotation:[90f,0f]}" % (x, ladder)
            print "summon minecraft:minecart ~6 %s ~7" % (x+1)
        else:
            print "setblock ~5 %s ~6 minecraft:ladder %s" % (x, ladder)
            print "summon minecraft:minecart ~5 %s ~6" % (x+1)

        x += FLOOR_SPACING


def configure_down_shaft():
    height = FIRST_FLOOR-1
    sign = SIGN_ORIENTATION.get(FACES, 2)
    if FACES == "East" or FACES == "West":
        print "setblock ~6 %s ~5 minecraft:wall_sign %s" % (height, sign)
        print "setblock ~6 %s ~5 minecraft:water 0" % FIRST_FLOOR
    else:
        print "setblock ~7 %s ~6 minecraft:wall_sign %s" % (height, sign)
        print "setblock ~7 %s ~6 minecraft:water 0" % FIRST_FLOOR


def make_bottom_entrance_exit():
    if FACES == "North":
        print "fill ~7 %s ~4 ~7 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1)
        print "fill ~5 %s ~4 ~5 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1)
    elif FACES == "South":
        print "fill ~7 %s ~7 ~7 %s ~8 minecraft:air 0" % (FLOOR, FLOOR+1)
        print "fill ~5 %s ~7 ~5 %s ~8 minecraft:air 0" % (FLOOR, FLOOR+1)
    elif FACES == "East":
        print "fill ~7 %s ~5 ~8 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1)
        print "fill ~7 %s ~7 ~8 %s ~7 minecraft:air 0" % (FLOOR, FLOOR+1)
    else:
        print "fill ~5 %s ~5 ~4 %s ~5 minecraft:air 0" % (FLOOR, FLOOR+1)
        print "fill ~5 %s ~7 ~4 %s ~7 minecraft:air 0" % (FLOOR, FLOOR+1)


def make_top_entrance_exit():
    pass


def main():
    print "Do these two first from a command " \
          "block to mark where this will happen."
    mark_the_location()
    print "Paste these into a command block combiner " \
          "tool once you are sure where you want things."
    excavate_and_cap()
    build_elevator_enclosure()
    dig_shafts()
    configure_up_shaft()
    configure_down_shaft()
    make_bottom_entrance_exit()
    make_top_entrance_exit()
    # x = 15  # 12 is the floor. First ladder should be 3 up
    # while x < 68:
    #     print "setblock ~6 %s ~7 minecraft:ladder 3" % x
    #     x += 3
    #
    # x = 16  # 15 is the first ladder. First minecart goes on top
    # while x < 68:
    #     print "summon minecraft:minecart ~6 %s ~7" % x
    #     x += 3


if __name__ == "__main__":
    main()
