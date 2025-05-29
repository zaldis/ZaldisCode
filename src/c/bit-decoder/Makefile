# https://makefiletutorial.com/#getting-started
main: build
	@mkdir -p out
	@./bin/bit-decoder ./tests/source_files/main ./out/decode.txt

ast:
	clang ./main.c -S -emit-llvm -o -

build:
	@mkdir -p ./bin
	@clang main.c -o ./bin/bit-decoder

