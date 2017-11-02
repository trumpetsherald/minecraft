import command_chainer

TOP = 80
BOTTOM = 10


def main():
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:glass 0 replace minecraft:grass" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:glass 0 replace minecraft:dirt" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:glass 0 replace minecraft:gravel" %
                        (y, y))
        y -= 1

    print "Grass and Dirt"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 4 replace minecraft:sandstone" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:glass 0 replace minecraft:sand" %
                        (y, y))
        y -= 1

    print "Sand and Stone"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:glass 0 replace minecraft:stone" %
                        (y, y))
        y -= 1

    print "Stones"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP

    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 15 replace minecraft:coal_ore" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 1 replace minecraft:iron_ore" %
                        (y, y))
        y -= 1

    print "Ores"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP
    while y >= BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:sea_lantern 0 replace minecraft:air" %
                        (y, y))
        y -= 1

    print "Air"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP

    while y >= BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:glass" % (y, y))

        y -= 1

    print "Glass"
    print command_chainer.chain_commands(commands)
    # commands = list()
    # y = TOP
    #
    # while y > BOTTOM:
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:redstone_ore" %
    #                     (y, y))
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:lapis_ore" % (y, y))
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:gold_ore" % (y, y))
    #     y -= 1
    #
    # print "Precious Ores"
    # print command_chainer.chain_commands(commands)
    # commands = list()
    # y = TOP
    #
    # while y > BOTTOM:
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:fence" % (y, y))
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:planks" % (y, y))
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:web" % (y, y))
    #     y -= 1
    #
    # print "Mine shafts"
    # print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
