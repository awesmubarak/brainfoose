#!/usr/bin/env python3

BOLD = '\033[1m'
END_BOLD = '\033[0m'

def main():
    def new_array():
        return [0] * 30000
    print(BOLD + "\nBrainfoose REPL" + END_BOLD)
    array = new_array()
    while True:
        program = input("\nbg > ")
        end_index = len(program) - 1
        pointer = 0
        program_location = 0

        while program_location <= end_index:
            token = program[program_location]
            if token == ">":
                pointer += 1
            elif token == "<":
                pointer -= 1
            elif token == "+":
                array[pointer] += 1
            elif token == "-":
                array[pointer] -= 1
            elif token == ".":
                print(chr(array[pointer]), end="")
            elif token == ",":
                array[pointer] = ord(input("input > ")[0])
            elif token == "[":
                if array[pointer] == 0:
                    loop_level = 1
                    while loop_level > 0:
                        program_location += 1
                        character = program[program_location]
                        if character == "[":
                            loop_level += 1
                        elif character == "]":
                            loop_level -= 1
            elif token == "]":
                loop_level = 1
                while loop_level > 0:
                    program_location -= 1
                    character = program[program_location]
                    if character == "[":
                        loop_level -= 1
                    elif character == "]":
                        loop_level += 1
                program_location -= 1
            elif token == "&":
                array = new_array()
            program_location += 1
    print("\n")


if __name__ == '__main__':
    main()
