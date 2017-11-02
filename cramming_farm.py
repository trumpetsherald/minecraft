import command_chainer

GROUND = 70
ORIENTATION = "EW"  # NS
MATERIAL = "minecraft:concrete 5"

UP_STAIR_ORIENTATION = {
    "North": 3,
    "South": 2,
    "East": 0,
    "West": 1
}

DOWN_STAIR_ORIENTATION = {
    "North": 2,
    "South": 3,
    "East": 1,
    "West": 0
}


def main():
    commands = list()
    commands.append(
        "fill ~2 %s ~1 ~5 %s ~8 %s" % (GROUND - 1, GROUND - 2, MATERIAL)
    )
    commands.append(
        "fill ~1 %s ~2 ~1 %s ~7 %s" % (GROUND - 1, GROUND - 2, MATERIAL)
    )
    commands.append(
        "fill ~6 %s ~3 ~6 %s ~6 %s" % (GROUND - 1, GROUND - 2, MATERIAL)
    )
    commands.append(
        "fill ~-2 %s ~4 ~8 %s ~5 minecraft:air 0" % (GROUND - 1, GROUND - 4)
    )
    commands.append(
        "fill ~3 %s ~4 ~3 %s ~5 minecraft:air 0" % (GROUND - 4, GROUND - 6)
    )
    commands.append(
        "setblock ~3 %s ~4 minecraft:redstone_torch 0" % (GROUND - 6)
    )
    commands.append(
        "setblock ~3 %s ~5 minecraft:redstone_torch 0" % (GROUND - 6)
    )
    commands.append(
        "fill ~3 %s ~4 ~3 %s ~5 %s" % (GROUND - 5, GROUND - 5, MATERIAL)
    )
    commands.append(
        "fill ~-2 %s ~4 ~8 %s ~5 minecraft:golden_rail 0" %
        (GROUND - 4, GROUND - 4)
    )
    commands.append(
        "fill ~1 %s ~3 ~6 %s ~6 %s" % (GROUND - 1, GROUND - 3, MATERIAL)
    )
    commands.append(
        "fill ~3 %s ~4 ~5 %s ~5 minecraft:stone_slab 8" %
        (GROUND - 3, GROUND - 3)
    )
    commands.append(
        "fill ~3 %s ~4 ~5 %s ~5 minecraft:air 0" % (GROUND - 1, GROUND - 2)
    )
    commands.append(
        "fill ~3 %s ~3 ~5 %s ~3 minecraft:dispenser 3 replace {Items:[{id:water_bucket,Count:1b,Slot:4b}]}" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~3 %s ~6 ~5 %s ~6 minecraft:dispenser 2 replace {Items:[{id:water_bucket,Count:1b,Slot:4b}]}" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~3 %s ~2 ~5 %s ~2 minecraft:unpowered_repeater 2" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~3 %s ~7 ~5 %s ~7 minecraft:unpowered_repeater 0" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~2 %s ~1 ~5 %s ~1 minecraft:redstone_wire 0" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~2 %s ~2 ~1 %s ~2 minecraft:redstone_wire 0" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~1 %s ~3 ~1 %s ~6 minecraft:redstone_wire 0" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~1 %s ~7 ~2 %s ~7 minecraft:redstone_wire 0" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "fill ~2 %s ~8 ~5 %s ~8 minecraft:redstone_wire 0" %
        (GROUND - 2, GROUND - 2)
    )
    commands.append(
        "setblock ~1 %s ~5 minecraft:stone_button 5" % GROUND
    )

    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
