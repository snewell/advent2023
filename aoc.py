import argparse
import sys


def load(run_fns):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", action="store_true", help="Run problem b")
    parser.add_argument(
        "input", nargs="?", metavar="input", help="Input file (stdin if not provided)"
    )

    args = parser.parse_args()
    fn = run_fns[0]
    if args.b:
        fn = run_fns[1]
    if args.input:
        with open(args.input, "r") as input:
            print(fn(input))
    else:
        print(fn(sys.stdin))
