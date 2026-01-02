# https://makefiletutorial.com/#getting-started
main: build
	@mkdir -p ./out
	@./bin/bit-decoder ./tests/source_files/main ./out/decode.txt

build:
	@mkdir -p bin/
	@clang main.c -c -o bin/main
	@clang src/bin-decoder.c -c -o bin/bin-decoder
	@clang src/utils.c -c -o bin/utils
	@clang bin/utils bin/bin-decoder bin/main -o bin/bit-decoder

debug:
	@mkdir -p bin/
	@clang main.c -D DEBUG -c -o bin/main
	@clang src/bin-decoder.c -D DEBUG -c -o bin/bin-decoder
	@clang src/utils.c -c -o bin/utils
	@clang bin/utils bin/bin-decoder bin/main -o bin/bit-decoder
	@./bin/bit-decoder ./tests/source_files/main ./out/decode.txt

ast:
	clang ./main.c -S -emit-llvm -o -
