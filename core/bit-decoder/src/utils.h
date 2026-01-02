#ifndef UTILS_H

#include <stdio.h>
#include <stdbool.h>

#define UTILS_H
#define BITS_IN_BYTE 8

bool get_bit(int mem_block, int bit_pos);
int file_size(FILE *source_file);

#endif
