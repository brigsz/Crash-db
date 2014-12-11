import sys
from dbseeder import DbSeeder


def main(argv=()):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """

    argv = sys.argv

    print(argv)

    seeder = DbSeeder(argv[1])
    seeder.process(argv[2])

    return 0

if __name__ == "__main__":
    sys.exit(main())
