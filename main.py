#!/usr/bin/python3

import sys
import os


def main():
    languages = {
        "java": ("javac {}; java {}", 2),
        "py": ("python {}", 1),
        "cpp": ("g++ -std=c++17 -O3 {}; ./a.out", 1),
        "c": ("gcc -O3  {}; ./a.out", 1),
        "go": ("go run {}", 1),
        "js": ("node {}", 1),
        "html": ("open {}", 1),
        "sh": ("bash {}", 1),
        "rs": ("rustc {} -o a.out; ./a.out", 1),
    }

    inputFile = "input.txt"
    outputFile = "output.txt"

    if len(sys.argv) == 1:
        print("Usage: code_runner <filename> <inputFile(optinal)> <outputFile(optinal)>")
    if len(sys.argv) == 3:
        # print("Usage")
        inputFile = sys.argv[2]
    if len(sys.argv) == 4:
        # print("Usage")
        outputFile = sys.argv[3]

    filename = sys.argv[1]
    extension = filename.split(".")[-1]
    inputAndOutput = " < " + inputFile + " > " + outputFile

    if not os.path.exists(inputFile):
        # os.system("touch " + inputFile)
        inputAndOutput = ""

    if extension in languages:
        if extension != "java":
            os.system(languages[extension][0].format(filename) + inputAndOutput)
        else:
            code = ".".join(filename.split(".")[:-1])
            os.system(languages[extension][0].format(filename, code) + inputAndOutput)


if __name__ == "__main__":
    main()
