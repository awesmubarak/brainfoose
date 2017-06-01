# Brainfoose

Yet another brainfuck interperator.

### Usage

The following characters make up the language:

| Character | Meaning                                                          |
| --------- | ---------------------------------------------------------------- |
| `>`       | Increment the data pointer.                                      |
| `<`       | Decrement the data pointer.                                      |
| `+`       | Increment the value at the data pointer.                         |
| `-`       | Decrement the value at the data pointer.                         |
| `.`       | Output the byte at the data pointer.                             |
| `,`       | Store a value at the data pointer's position.                    |
| `[`       | If the value at the data pointer is 0, move to matching `]`.     |
| `]`       | If the value at the data pointer is not 0, more to matching `[`. |
| `&`       | Reset array.                                                     |
| `%`       | Load program from file, syntax: `% [filename.bf]`.               |

To quit the prompt press <kbd>ctrl</kbd> <kbd>c</kbd>.

[![demo](https://asciinema.org/a/9ecaa1s4wj8rctm0hypzrg595.png)](https://asciinema.org/a/9ecaa1s4wj8rctm0hypzrg595?autoplay=1)

The following is hello world program, taken from [wikipedia][wbfe].

```brainfuck
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
Cell No :   0   1   2   3   4   5   6
Contents:   0   0  72 104  88  32   8
Pointer :   ^

>>.                     Cell #2 has value 72 which is 'H'
>---.                   Subtract 3 from Cell #3 to get 101 which is 'e'
+++++++..+++.           Likewise for 'llo' from Cell #3
>>.                     Cell #5 is 32 for the space
<-.                     Subtract 1 from Cell #4 for 87 to give a 'W'
<.                      Cell #3 was set to 'o' from the end of 'Hello'
+++.------.--------.    Cell #3 for 'rl' and 'd'
>>+.                    Add 1 to Cell #5 gives us an exclamation point
>++.                    And finally a newline from Cell #6
```

This code can also be rewritten without comments as:

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

[wbfe]: https://en.wikipedia.org/wiki/Brainfuck#Hello_World.21
