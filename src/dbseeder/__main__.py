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
    print(argv)

    argv = sys.argv

    print(argv)

    seeder = DbSeeder()

    if '--length' in argv:
        argv.remove('--length')
        print(argv)

        seeder.get_lengths(argv[1])

    else:
        seeder.process(argv[1])

    return 0

if __name__ == "__main__":
    sys.exit(main())
