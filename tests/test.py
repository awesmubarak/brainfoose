#!/usr/bin/env python3

import brainfoose
import unittest

from termcolor import colored


def read_file(filename: str):
    with open(filename) as file:
        return file.readline()


class TestExecution(unittest.TestCase):

    def setUp(self):
        pass

    # basic stuff
    def test_create_tape(self):
        tape = brainfoose.new_tape()
        correct = [0] * 3000
        self.assertEqual(tape, correct)

    def test_create_tape_5_cells(self):
        tape = brainfoose.new_tape(5)
        correct = [0] * 5
        self.assertEqual(tape, correct)

    def test_add_10_to_first_cell(self):
        tape = brainfoose.new_tape(tape_size=5)
        bf, out = brainfoose.execute_program("++++++++++", tape)
        correct = [10, 0, 0, 0, 0]
        self.assertEqual(bf, correct)

    def test_add_5_to_first_two_cells(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program("+++++>+++++", tape)
        correct = [5, 5, 0, 0, 0]
        self.assertEqual(bf, correct)

    def test_add_5_subtract_4(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program("+++++----", tape)
        correct = [1, 0, 0, 0, 0]
        self.assertEqual(bf, correct)

    def test_add_2_to_all_cells(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program("++>++>++>++>++", tape)
        correct = [2, 2, 2, 2, 2]
        self.assertEqual(bf, correct)

    def test_add_2_to_all_cells_then_take_away_1(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program("++>++>++>++>++<-<-<-<-<-", tape)
        correct = [1, 1, 1, 1, 1]
        self.assertEqual(bf, correct)

    def test_add_first_two_cells(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program("++>++<[->+<]", tape)
        correct = [0, 4, 0, 0, 0]
        self.assertEqual(bf, correct)

    # errors
    def test_error_if_unequal_brackets(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program("[", tape)
        correct = colored("Brackets don't match.", "red")
        self.assertEqual(out, correct)

    def test_error_if_tape_too_small(self):
        tape = brainfoose.new_tape(5)
        bf, out = brainfoose.execute_program(">>>>>+", tape)
        correct = colored("Not enough tape.", "red")
        self.assertEqual(out, correct)

    # misc
    def test_hello_world(self):
        tape = brainfoose.new_tape()
        bf, out = brainfoose.execute_program(read_file("hello_world.txt"), tape)
        correct = "Hello World!\n"
        self.assertEqual(out, correct)


if __name__ == "__main__":
    unittest.main()
