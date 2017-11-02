import command_chainer

TOP = 95
BOTTOM = 10


def main():
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 13 replace minecraft:grass" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 12 replace minecraft:dirt" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 7 replace minecraft:gravel" %
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
                        "minecraft:stained_glass 6 replace minecraft:stone 1" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 0 replace minecraft:stone 3" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:stained_glass 8 replace minecraft:stone" %
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
                        "minecraft:sea_lantern 0 replace minecraft:diamond_ore" %
                        (y, y))
        y -= 1

    print "Diamonds"
    print command_chainer.chain_commands(commands)
    # commands = list()
    # y = TOP
    #
    # while y >= BOTTOM:
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:coal_ore" % (y, y))
    #     commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
    #                     "minecraft:air 0 replace minecraft:iron_ore" % (y, y))
    #
    #     y -= 1
    #
    # print "Coal and Iron"
    # print command_chainer.chain_commands(commands)
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
