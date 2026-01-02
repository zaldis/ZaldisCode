#include "src/bin-decoder.h"
#include <stdbool.h>

#ifdef DEBUG
#include <stdio.h>
#endif

/* TODO: Add CUnit tests
 * 
 * URL: https://www.geeksforgeeks.org/a-comprehensive-guide-to-unit-testing-in-c/
 * GitHub: https://github.com/jacklicn/CUnit/tree/master
 *
 * Add proper logging:
 * - logc, zlog, 
 **/

int main(int argc, char *argv[]) {
  #ifdef DEBUG
    printf("Amount of program arguments: %d\n", argc);
  #endif
  char *source_file_path = argv[1];
  char *decoded_file_path = argv[2];
  binary_decode(source_file_path, decoded_file_path);
  return 0;
}

