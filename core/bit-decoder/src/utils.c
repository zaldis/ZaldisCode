#include "utils.h"
#include <stdbool.h>


int file_size(FILE *source_file) {
  fseek(source_file, 0, SEEK_END);
  int file_size = ftell(source_file);
  fseek(source_file, 0, SEEK_SET);
  return file_size;
}


bool get_bit(int mem_block, int bit_pos) {
    int bit_mask = 1 << bit_pos;
    return (mem_block & bit_mask) > 0;
}
