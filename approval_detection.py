import sys

from src import get_address_approvals


def main():
    argv = sys.argv
    if len(argv) == 3 and argv[1] == "--address":
        get_address_approvals(argv[2])
    else:
        print("no good address")


if __name__ == '__main__':
    main()
