import command_chainer

GROUND_LEVEL = 70
X_DIST = 63
Z_DIST = 63
# WALL_MATERIAL = "minecraft:stained_hardened_clay 9"
WALL_MATERIAL = "minecraft:concrete 15"
FLOOR_MATERIAL = "minecraft:stone 4"
WINDOW_MATERIAL = "minecraft:stained_glass_pane 3"
WINDOW_WIDTH = 3
WINDOW_SPACING = 2
CORNER_WIDTH = 2

HEIGHT = 241
FACES = "South"

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
    commands = ["fill ~2 %s ~2 ~%s %s ~%s minecraft:carpet 9" %
                (GROUND_LEVEL, X_DIST + 2, GROUND_LEVEL, Z_DIST + 2)]
    print command_chainer.chain_commands(commands)


def lay_flooring(commands):
    commands.append("fill ~2 %s ~2 ~%s %s ~%s %s" % (
        GROUND_LEVEL - 1,
        X_DIST + 2,
        GROUND_LEVEL - 1,
        Z_DIST + 2,
        FLOOR_MATERIAL)
    )


def build_x_walls(commands):
    commands.append("fill ~2 %s ~2 ~%s %s ~2 %s" % (
        GROUND_LEVEL - 1, X_DIST + 2, HEIGHT, WALL_MATERIAL))
    commands.append("fill ~2 %s ~%s ~%s %s ~%s %s" % (
        GROUND_LEVEL - 1,
        Z_DIST + 2,
        X_DIST + 2,
        HEIGHT,
        Z_DIST + 2,
        WALL_MATERIAL)
    )


def build_z_walls(commands):
    commands.append("fill ~2 %s ~2 ~2 %s ~%s %s" % (
        GROUND_LEVEL - 1, HEIGHT, Z_DIST + 2, WALL_MATERIAL))
    commands.append("fill ~%s %s ~2 ~%s %s ~%s %s" % (
        X_DIST + 2,
        GROUND_LEVEL - 1,
        X_DIST + 2,
        HEIGHT,
        Z_DIST + 2,
        WALL_MATERIAL)
    )


def build_x_windows(commands):
    # We want to start with the corners and work in
    # until there is no room left for window width + gap
    halfway = (X_DIST / 2) + 2
    x = CORNER_WIDTH + 2  # 2,2 is where we start things...
    # Starting from 2,2 put in windows until the next one goes past halfway
    while (x + WINDOW_SPACING) < halfway:
        commands.append("fill ~%s %s ~2 ~%s %s ~2 %s" % (
            x, GROUND_LEVEL, x + WINDOW_SPACING, HEIGHT - 2, WINDOW_MATERIAL))
        x += (WINDOW_SPACING + WINDOW_WIDTH)

    # Now get the other half working backwards
    x = (X_DIST + 2) - CORNER_WIDTH
    while (x - WINDOW_SPACING) > halfway:
        commands.append("fill ~%s %s ~2 ~%s %s ~2 %s" % (
            x, GROUND_LEVEL, x - WINDOW_SPACING, HEIGHT - 2, WINDOW_MATERIAL))
        x -= (WINDOW_SPACING + WINDOW_WIDTH)

    # Now do it all again for the wall at Z max
    x = CORNER_WIDTH + 2  # 2,2 is where we start things...
    while (x + WINDOW_SPACING) < halfway:
        commands.append("fill ~%s %s ~%s ~%s %s ~%s %s" % (
            x,
            GROUND_LEVEL,
            Z_DIST + 2,
            x + WINDOW_SPACING,
            HEIGHT - 2,
            Z_DIST + 2,
            WINDOW_MATERIAL)
        )
        x += (WINDOW_SPACING + WINDOW_WIDTH)

    # Now get the other half working backwards
    x = (X_DIST + 2) - CORNER_WIDTH
    while (x - WINDOW_SPACING) > halfway:
        commands.append("fill ~%s %s ~%s ~%s %s ~%s %s" % (
            x,
            GROUND_LEVEL,
            Z_DIST + 2,  # command block offset
            x - WINDOW_SPACING,
            HEIGHT - 2,
            Z_DIST + 2,  # command block offset
            WINDOW_MATERIAL)
        )
        x -= (WINDOW_SPACING + WINDOW_WIDTH)


def build_z_windows(commands):
    # We want to start with the corners and work in
    # until there is no room left for window width + gap
    halfway = (Z_DIST / 2) + 2
    z = CORNER_WIDTH + 2  # 2,2 is where we start things...
    # Starting from 2,2 put in windows until the next one goes past halfway
    while (z + WINDOW_SPACING) < halfway:
        commands.append("fill ~2 %s ~%s ~2 %s ~%s %s" % (
            GROUND_LEVEL, z, HEIGHT - 2, z + WINDOW_SPACING, WINDOW_MATERIAL))
        z += (WINDOW_SPACING + WINDOW_WIDTH)

    # Now get the other half working backwards
    z = (Z_DIST + 2) - CORNER_WIDTH
    while (z - WINDOW_SPACING) > halfway:
        commands.append("fill ~2 %s ~%s ~2 %s ~%s %s" % (
            GROUND_LEVEL, z, HEIGHT - 2, z - WINDOW_SPACING, WINDOW_MATERIAL))
        z -= (WINDOW_SPACING + WINDOW_WIDTH)

    # Now do it all again for the wall at X max
    z = CORNER_WIDTH + 2  # 2,2 is where we start things...
    while (z + WINDOW_SPACING) < halfway:
        commands.append("fill ~%s %s ~%s ~%s %s ~%s %s" % (
            X_DIST + 2,
            GROUND_LEVEL,
            z,
            X_DIST + 2,
            HEIGHT - 2,
            z + WINDOW_SPACING,
            WINDOW_MATERIAL)
        )
        z += (WINDOW_SPACING + WINDOW_WIDTH)

    # Now get the other half working backwards
    z = (Z_DIST + 2) - CORNER_WIDTH
    while (z - WINDOW_SPACING) > halfway:
        commands.append("fill ~%s %s ~%s ~%s %s ~%s %s" % (
            X_DIST + 2,  # command block offset
            GROUND_LEVEL,
            z,
            X_DIST + 2,
            HEIGHT - 2,
            z - WINDOW_SPACING,
            WINDOW_MATERIAL)
        )
        z -= (WINDOW_SPACING + WINDOW_WIDTH)


def main():
    print "Do these two first from a command " \
          "block to mark where this will happen."
    mark_the_location()
    print "Paste these into a command block combiner " \
          "tool once you are sure where you want things."
    commands = []

    lay_flooring(commands)
    build_x_walls(commands)
    build_z_walls(commands)
    build_x_windows(commands)
    build_z_windows(commands)

    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
