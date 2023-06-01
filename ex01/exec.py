import sys
if len(sys.argv) > 1:
    str = ' '.join(sys.argv[1::])
    print(str[::-1].swapcase())