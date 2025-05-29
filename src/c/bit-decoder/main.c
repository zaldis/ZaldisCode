#include <stdio.h>

#define BUFFER_SIZE 100

int main(int argc, char *argv[]) {
    printf("Amount of program arguments: %d\n", argc);

    char *source_file_path = argv[1];
    FILE *source_file = fopen(source_file_path, "rb");

    fseek(source_file, 0, SEEK_END);
    int file_size = ftell(source_file);
    fseek(source_file, 0, SEEK_SET);
    
    printf("Size of target file: %d bytes\n", file_size);

    char *decoded_file_path = argv[2];
    FILE *decoded_file = fopen(decoded_file_path, "wb");

    int buffer[BUFFER_SIZE];
    fread(buffer, sizeof(int), BUFFER_SIZE, source_file);
    int byte_order = 1;
    const int int_size = sizeof(int);
    printf("Decode byte #%d: ", byte_order);

    for (int pos = 0; pos < BUFFER_SIZE; ++pos) {
      int val = buffer[pos];
      int bits[32];
      int checked_bits = 0;
      while (val) {
        int bit = val & 1;
        bits[checked_bits++] = bit;
        val <<= 1;
      }
      for (int byte_block = 0; byte_block < 4; byte_block++) {
        printf("\nDecode byte #%d: ", byte_order++);
        int bit_start = byte_block * 8;
        int bit_end = bit_start + 8;
        for (int bit_pos = bit_start; bit_pos < bit_end; ++bit_pos) {
          printf("%d", bits[bit_pos]);
          fprintf(decoded_file, "%d", bits[bit_pos]);
        }
      }
    }

    fclose(source_file);

    return 0;
}

