#include "bin-decoder.h"
#include "utils.h"


void print_byte_block(int mem_block, int byte_pos, FILE *out);


void binary_decode(char *source_file_name, char *out_file_name) {
  FILE *source_file = fopen(source_file_name, "rb");
  printf("Target file: %s\n", source_file_name);
  int bytes_in_file = file_size(source_file);
  printf("Size of target file: %d bytes\n", bytes_in_file);
  FILE *decoded_file = fopen(out_file_name, "wb");

  int buffer[BUFFER_SIZE];
  const int bytes_in_buff_item = sizeof(int);
  const int bits_in_buff_item = bytes_in_buff_item * BITS_IN_BYTE;
  int byte_order = 1;
  int read_buff_items = 0;

  while ((read_buff_items = fread(buffer, sizeof(int), BUFFER_SIZE, source_file)) > 0) {
    for (int pos = 0; pos < read_buff_items; ++pos) {
      int mem_block = buffer[pos];
      for (int byte_pos = 0; byte_pos < bytes_in_buff_item; byte_pos++) {
        #ifdef DEBUG
          printf("Decode byte #%d: ", byte_order++);
        #endif
        print_byte_block(mem_block, byte_pos, decoded_file);
      }
    }
  };
  printf("Target file has been successfuly decoded into %s", out_file_name);

  fclose(source_file);
  fclose(decoded_file);
}

void print_byte_block(int mem_block, int byte_pos, FILE *out) {
  int bit_start = byte_pos * BITS_IN_BYTE;
  int bit_end = bit_start + BITS_IN_BYTE;
  for (int bit_pos = bit_start; bit_pos < bit_end; ++bit_pos) {
    #ifdef DEBUG
      printf("%d", get_bit(mem_block, bit_pos));
    #endif
    fprintf(out, "%d", get_bit(mem_block, bit_pos));
  }
  #ifdef DEBUG
    printf("\n");
  #endif
}
