def chain_commands(commands):
    chain_start = "summon falling_block ~ ~1 ~ {Block:log,Time:1,Passengers:[" \
                  "{id:falling_block,Block:redstone_block,Time:1,Passengers:[" \
                  "{id:falling_block,Block:activator_rail,Time:1,Passengers:["
    chained_commands = ""
    chain_end = "{id:commandblock_minecart," \
                "Command:\"setblock ~ ~ ~1 command_block 0 0 " \
                "{Command:\\\"fill ~ ~-2 ~-1 ~ ~ ~ air\\\"}\"}," \
                "{id:commandblock_minecart," \
                "Command:\"setblock ~ ~-1 ~1 redstone_block\"}," \
                "{id:commandblock_minecart," \
                "Command:\"kill @e[type=commandblock_minecart,r=1]\"}]}]}]}"

    for c in commands:
        chained_commands += "{id:commandblock_minecart,Command:\"%s\"}," % c

    return chain_start + chained_commands + chain_end


def main():
    commands = list()
    commands.append("setblock ~3 80 ~3 minecraft:quartz_stairs 0")
    commands.append("setblock ~3 81 ~3 minecraft:quartz_stairs 0")
    commands.append("setblock ~3 82 ~3 minecraft:quartz_stairs 0")

    result = chain_commands(commands)
    print result


if __name__ == "__main__":
    main()
