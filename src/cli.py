import sys
from NumberToWords import convert_to_words

def main(argv=sys.argv):
    res = convert_to_words(int(v:=argv[1].strip()))
    print(f"RESULT: {v} -> {res}")

if __name__ == '__main__':
    sys.exit(main())

    