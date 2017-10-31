==========
Brainfoose
==========

A brainfuck REPL.

Installation
------------

Pypi (recommended):

``sudo pip3 install brainfoose``

Manual installation using git master:

``git clone https://github.com/abactel/brainfoose``

``cd brainfoose``

``pip install -r requirements.txt``

``sudo setup.py install``

Usage
-----

Usage:
    ``brainfoose [--run_command=<programs>]``

    ``brainfoose [--tape_size=<tape_size>]``

    ``brainfoose [--verify_program=<tape_size>]``

    ``brainfoose (-h | --help)``

    ``brainfoose --version``

Options:
    -h, --help               Show this message
    --version                Show version information
    --run                    Run a command without starting a REPL
    --tape_size=<tape_size>  Set size of tape [default: 3000]

The syntax of the language is as follows:

+--------+----------------------------------------------------------------------+
| Token  | Meaning                                                              |
+========+======================================================================+
| ``?``  | Print a help screen                                                  |
+--------+----------------------------------------------------------------------+
| ``>``  | Increment the data pointer by 1.                                     |
+--------+----------------------------------------------------------------------+
| ``<``  | Decrement the data pointer by 1.                                     |
+--------+----------------------------------------------------------------------+
| ``+``  | Increment the value at the data pointer by 1.                        |
+--------+----------------------------------------------------------------------+
| ``-``  | Decrement the value at the data pointer by 1.                        |
+--------+----------------------------------------------------------------------+
| ``.``  | Output the byte at the data pointer. The byte is formatted to the    |
|        | character it represents.                                             |
+--------+----------------------------------------------------------------------+
| ``,``  | Store a value at the data pointer’s position. The character is       |
|        | as a decimal byte representing the character. The character is       |
|        | accepted form a standard input prompt.                               |
+--------+----------------------------------------------------------------------+
| ``[``  | If the value at the data pointer is 0, move to matching ``]``.       |
+--------+----------------------------------------------------------------------+
| ``]``  | If the value at the data pointer is not 0, move to matching ``[``.   |
+--------+----------------------------------------------------------------------+
| ``$``  | Display tape up to last non-zero cell.                               |
+--------+----------------------------------------------------------------------+
| ``&``  | Reset tape.                                                          |
+--------+----------------------------------------------------------------------+
| ``%``  | Load program from file, syntax: ``%[filename]``.                     |
+--------+----------------------------------------------------------------------+

The wikipedia page on brainfuck includes the following tutorial:
::

    [ This program prints "Hello World!" and a newline to the screen, its
      length is 106 active command characters. [It is not the shortest.]

      This loop is an "initial comment loop", a simple way of adding a comment
      to a BF program such that you don't have to worry about any command
      characters. Any ".", ",", "+", "-", "<" and ">" characters are simply
      ignored, the "[" and "]" characters just have to be balanced. This
      loop and the commands it contains are ignored because the current cell
      defaults to a value of 0; the 0 value causes this loop to be skipped.
    ]
    ++++++++               Set Cell #0 to 8
    [
        >++++               Add 4 to Cell #1; this will always set Cell #1 to 4
        [                   as the cell will be cleared by the loop
            >++             Add 2 to Cell #2
            >+++            Add 3 to Cell #3
            >+++            Add 3 to Cell #4
            >+              Add 1 to Cell #5
            <<<<-           Decrement the loop counter in Cell #1
        ]                   Loop till Cell #1 is zero; number of iterations is 4
        >+                  Add 1 to Cell #2
        >+                  Add 1 to Cell #3
        >-                  Subtract 1 from Cell #4
        >>+                 Add 1 to Cell #6
        [<]                 Move back to the first zero cell you find; this will
                            be Cell #1 which was cleared by the previous loop
        <-                  Decrement the loop Counter in Cell #0
    ]                       Loop till Cell #0 is zero; number of iterations is 8

    The result of this is:
    Cell No :   0   1   2   3   4s


Further reading
---------------

- https://learnxinyminutes.com/docs/brainfuck/
- https://en.wikipedia.org/wiki/Brainfuck
- http://blog.klipse.tech/brainfuck/2016/12/17/brainfuck.html
