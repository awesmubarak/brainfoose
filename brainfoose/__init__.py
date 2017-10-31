#!/usr/bin/env python3

"""Brainfoose.

A brainfuck REPL.

Usage:
    brainfoose [--run_command=<programs>]
    brainfoose [--tape_size=<tape_size>]
    brainfoose [--verify_program=<tape_size>]
    brainfoose (-h | --help)
    brainfoose --version

Options:
    -h, --help               Show this message
    --version                Show version information
    --run                    Run a command without starting a REPL
    --tape_size=<tape_size>  Set size of tape [default: 3000]

REPL syntax:
    ?  Print this help screen
    >  Increment the data pointer by 1
    <  Decrement the data pointer by 1
    +  Increment the value at the data pointer by 1
    -  Decrement the value at the data pointer by 1
    .  Output the byte at the data pointer. The byte is formatted to the
         character it represents
    ,  Store a value at the data pointer’s position. The character is as a
         decimal byte representing the character. The character is accepted
         form a standard input prompt
    [  If the value at the data pointer is 0, move to matching ]
    ]  If the value at the data pointer is not 0, move to matching [
    $  Display tape up to last non-zero cell
    &  Reset tape
    %  Load program from file, syntax: %[filename]

"""


from docopt import docopt      # Command line argument parsing
from termcolor import colored  # Color output


def get_input(text: str):
    """Handle user input.

    The function exits cleanly on ``KeyboardInterrupt`` and ``EOFError``
    (ctrl-c and ctrl-d).

    Args:
        Text (str): Prompt to print. A greater than symbol (">") is appended to
            the end and escape codes are used to make the prompt bold.

    Returns:
        Str: User's input.

    """
    try:
        user_input = input("\033[1m" + text + " > \033[0m")
    except (KeyboardInterrupt, EOFError):
        print("\nBye.")
        exit(0)
    return user_input


def get_program():
    """Gets user input and opens program file if needed.

    Returns:
        Str: program

    """
    program = get_input("bf") + " "  # space need to prevent out of index error
    if program.startswith("%"):
        try:
            with open(program[1:], "r") as file:
                program = ""
                for line in file.readlines():
                    program += line
        except FileNotFoundError:
            print("File not found: " + program[2:])
            program = ""
    elif program.startswith("?"):
        print(__doc__)
    return program


def new_tape(tape_size=3000):
    """Creates a new tape.

    Args:
        Tape_size (int) (optional): Size of the tape [default:3000].

    Returns:
        list: Tape. A list of integer ``0``s of specified size.

    """
    return [0] * tape_size


def execute_program(program: str, tape: list):
    """Runs the brainfuck program.

    Args:
        Program (str): A brainfuck program.
        Tape (list): A list of integers (see new_tape()).

    Returns:
        List: Tape (see above).
        Str: Output to print.

    """
    output = []
    if not program.count("[") == program.count("]"):
        output.append(colored("Brackets don't match.", "red"))
        return tape, "".join(output)
    if program.count(">") >= len(tape):
        output.append(colored("Not enough tape.", "red"))
        return tape, "".join(output)
    end_index = len(program) - 1
    pointer = 0
    program_location = 0
    while program_location <= end_index:
        token = program[program_location]
        print_at_end = ""  # adds final linebreak after printing chars
        if token == ">":
            pointer += 1
        elif token == "<":
            pointer -= 1
        elif token == "+":
            tape[pointer] += 1
        elif token == "-":
            tape[pointer] -= 1
        elif token == ".":
            output.append(chr(tape[pointer]))
        elif token == ",":
            output.append(print_at_end)
            print_at_end = ""
            tape[pointer] = ord(get_input("input")[0])
        elif token == "[":
            if tape[pointer] == 0:
                loop_level = 1
                while loop_level > 0:
                    program_location += 1
                    sub_token = program[program_location]
                    if sub_token == "[":
                        loop_level += 1
                    elif sub_token == "]":
                        loop_level -= 1
        elif token == "]":
            loop_level = 1
            while loop_level > 0:
                program_location -= 1
                sub_token = program[program_location]
                if sub_token == "[":
                    loop_level -= 1
                elif sub_token == "]":
                    loop_level += 1
            program_location -= 1
        elif token == "&":
            tape = new_tape()
        elif token == "$":
            last_important_value = 0
            for cell_n, cell in enumerate(tape):
                if cell != 0:
                    last_important_value = cell_n
            output.append(str(tape[:last_important_value + 1]))
        program_location += 1
    output.append(print_at_end)
    return tape, "".join(output)


def main():
    """Starts REPL or runs program."""
    arguments = docopt(__doc__, version="Brainfoose v2.0.0")
    tape = new_tape(int(arguments["--tape_size"]))
    print("\n\033[1mBrainfoose.\033[0m\n")  # brainfoose in bold plus newlines
    if arguments["--run_command"]:
        tape, output = execute_program(arguments["--run_command"], tape)
        print(output)
    else:
        while True:
            program = get_program()
            tape, output = execute_program(program, tape)
            print(output)


if __name__ == '__main__':
    main()
