# Code Runner

This Python script, `code_runner.py`, is a simple tool designed to compile and execute various programming language code files with ease.

## Usage

To use the `code_runner.py` script, follow the syntax below:

```bash
python3 code_runner.py <filename> <inputFile(optional)> <outputFile(optional)>
```

## Supported Languages and Commands

The script supports the following programming languages along with their corresponding compilation and execution commands:

- **Java**: `javac <filename>; java <filename_without_extension>`
- **Python**: `python <filename>`
- **C++**: `g++ -std=c++17 -O3 <filename>; ./a.out`
- **C**: `gcc -O3 <filename>; ./a.out`
- **Go**: `go run <filename>`
- **JavaScript**: `node <filename>`
- **HTML**: `open <filename>` (assumed for opening in a browser)
- **Shell Script**: `bash <filename>`
- **Rust**: `rustc <filename> -o a.out; ./a.out`
