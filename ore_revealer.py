import command_chainer

TOP = 60 - 1
BOTTOM = 0


def main():
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:log" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:log2" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:grass" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:dirt" % (y, y))
        y -= 1

    print "Soil / Vegetation"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:water" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:lava" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:sand" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:gravel" % (y, y))
        y -= 1

    print "Liquids and sands"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP
    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:lava 0 replace minecraft:water" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:water 0 replace minecraft:lava" % (y, y))
        y -= 1

    print "Reverse Lava Water"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP

    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:sandstone" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:stone" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:cobblestone" %
                        (y, y))
        y -= 1

    print "stones"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP
    while y >= BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:bedrock" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:obsidian" % (y, y))
        y -= 1

    print "Hard rocks"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP

    while y >= BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:coal_ore" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:iron_ore" % (y, y))

        y -= 1

    print "Coal and Iron"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP

    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:redstone_ore" %
                        (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:lapis_ore" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:gold_ore" % (y, y))
        y -= 1

    print "Precious Ores"
    print command_chainer.chain_commands(commands)
    commands = list()
    y = TOP

    while y > BOTTOM:
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:fence" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:planks" % (y, y))
        commands.append("fill ~90 %s ~90 ~-90 %s ~-90 "
                        "minecraft:air 0 replace minecraft:web" % (y, y))
        y -= 1

    print "Mine shafts"
    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
