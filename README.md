# Brainfoose

Yet another brainfuck interperator.

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
