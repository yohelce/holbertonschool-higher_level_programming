#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        print(f"{num} arguments.")
    elif num == 1:
        print(f"{num} argument:")
    else:
        print(f"{num} arguments:")

    for i in range(1, num + 1):
        print(f"{i}: {sys.argv[i]}")
