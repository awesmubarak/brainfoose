#!/usr/bin/env python3

BOLD = '\033[1m'
END_BOLD = '\033[0m'

print(BOLD + "\nBraingoose REPL\n" + END_BOLD)

while True:
    program = input("bg >  ")
    end_index = len(program) - 1

    if end_index < 0: end_index = 0
    if end_index >= len(program): end_index = len(program) - 1
    array = [0] * 30000
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
            input_data = input("input > ")
            array[pointer] = ord(input_data[0])
        elif token =="[":
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
        program_location += 1
print("\n")
