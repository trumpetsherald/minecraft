import command_chainer

GROUND = 70
LENGTH = 17
CEILING = 4
FACES = "North"

STAIR_ORIENTATION = {
    "North": 3,
    "South": 2,
    "East": 0,
    "West": 1
}

CHEST_ORIENTATION = {
    "North": 2,
    "South": 3,
    "East": 5,
    "West": 4
}


def main():
    commands = list()
    stairs = STAIR_ORIENTATION.get(FACES, 0)
    step_height = GROUND + CEILING
    if FACES == "North":
        y = GROUND
        z = -2  # start this two in front of the block
        c = 0
        while c < LENGTH:
            commands.append(
                "fill ~ %s ~%s ~1 %s ~%s minecraft:air 0 destroy" % (
                    y, z, step_height, z
                )
            )
            commands.append(
                "setblock ~ %s ~%s minecraft:quartz_stairs %s" % (y, z, stairs)
            )
            commands.append(
                "setblock ~1 %s ~%s minecraft:quartz_stairs %s" % (y, z, stairs)
            )
            z -= 1
            y += 1
            c += 1
            step_height += 1
    elif FACES == "South":
        y = GROUND
        z = 2  # start this two in front of the block
        c = 0
        while c < LENGTH:
            commands.append(
                "fill ~ %s ~%s ~-1 %s ~%s minecraft:air 0 destroy" % (
                    y, z, step_height, z
                )
            )
            commands.append(
                "setblock ~ %s ~%s minecraft:quartz_stairs %s" % (y, z, stairs)
            )
            commands.append(
                "setblock ~-1 %s ~%s minecraft:quartz_stairs %s" % (y, z, stairs)
            )
            z += 1
            y += 1
            c += 1
            step_height += 1
    elif FACES == "East":
        y = GROUND
        x = 2  # start this two in front of the block
        c = 0
        while c < LENGTH:
            commands.append(
                "fill ~%s %s ~ ~%s %s ~1 minecraft:air 0 destroy" % (
                    x, y, x, step_height
                )
            )
            commands.append(
                "setblock ~%s %s ~ minecraft:quartz_stairs %s" % (x, y, stairs)
            )
            commands.append(
                "setblock ~%s %s ~1 minecraft:quartz_stairs %s" % (x, y, stairs)
            )
            x += 1
            y += 1
            c += 1
            step_height += 1
    else:
        y = GROUND
        x = -2  # start this two in front of the block
        c = 0
        while c < LENGTH:
            commands.append(
                "fill ~%s %s ~ ~%s %s ~-1 minecraft:air 0 destroy" % (
                    x, y, x, step_height
                )
            )
            commands.append(
                "setblock ~%s %s ~ minecraft:quartz_stairs %s" % (x, y, stairs)
            )
            commands.append(
                "setblock ~%s %s ~-1 minecraft:quartz_stairs %s" % (x, y, stairs)
            )
            x -= 1
            y += 1
            c += 1
            step_height += 1

    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
