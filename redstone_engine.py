import command_chainer
    

def main():
    commands = list()

    commands.append("setblock ~7 %s ~6 minecraft:wall_sign %s")

    print command_chainer.chain_commands(commands)


if __name__ == "__main__":
    main()
