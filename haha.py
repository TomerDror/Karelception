import sys


def main():
    print("Funny calculator!! Enter expression (example: 5 + (3 * 2)):")
    blacklist = ["abs",
                 "all",
                 "any",
                 "ascii",
                 "bin",
                 "bool",
                 "bytearray",
                 "bytes",
                 "callable",
                 "chr",
                 "classmethod",
                 "compile",
                 "complex",
                 "delattr",
                 "dict",
                 "dir",
                 "divmod",
                 "enumerate",
                 "eval",
                 "exec",
                 "filter",
                 "float",
                 "format",
                 "frozenset",
                 "getattr",
                 "globals",
                 "hasattr",
                 "hash",
                 "help",
                 "hex",
                 "id",
                 "input",
                 "int",
                 "isinstance",
                 "issubclass",
                 "iter",
                 "len",
                 "list",
                 "locals",
                 "map",
                 "max",
                 "memoryview",
                 "min",
                 "next",
                 "object",
                 "oct",
                 "open",
                 "ord",
                 "pow",
                 "print",
                 "property",
                 "range",
                 "repr",
                 "reversed",
                 "round",
                 "set",
                 "setattr",
                 "slice",
                 "sorted",
                 "staticmethod",
                 "str",
                 "sum",
                 "super",
                 "tuple",
                 "type",
                 "vars",
                 "zip",
                 ]

    raw = input()
    for blackword in blacklist:  # filter malicious code
        if blackword in raw:
            print(f"Why malicious :( you entered {blackword}" )
            sys.exit(1)

    result = eval(raw)
    print("your result is: ", result)


if __name__ == '__main__':
    main()