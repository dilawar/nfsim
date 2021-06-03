# nfsim main module.

__author__ = "Dilawar Singh"
__email__ = "dilawar.s.rajput@gmail.com"

from pathlib import Path
from typing import Dict

import nfsim._nfsim as _nfsim


def main(args: dict):
    opts = {}
    for k, v in args.items():
        if v:
            opts[k] = str(v)
    s = _nfsim.initSystemFromFlags(opts, args.get("verbose", False))
    _nfsim.runFromArgs(s)


if __name__ == "__main__":
    import argparse

    desc = (
        "To run NFsim at the command prompt, use flags to specify what you "
        ' want to do.  Flags are given in this format in any order: "-flagName".'
        " Some of the flags require an additional parameter.  For instance, the "
        " -xml flag requires the filename of the xml file.  The format would look "
        " something like: '-xml modelFile.xml'.  Simulation output is dumped to "
        " a file named: '[modelName]_nf.gdat' in the current directory by default."
    )

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "-xml",
        type=str,
        help=(
            "used to specify the input xml file to read. "
            "the xml file must be given directly after this flag."
        ),
    )

    parser.add_argument(
        "-rnf", type=str, help="used to specify an rnf script to execute."
    )

    parser.add_argument("-o", type=Path, help="used to specify the output file name.")

    parser.add_argument(
        "-sim",
        type=float,
        help=(
            " used to specify the length (in seconds) of a simulation "
            " when running an xml file.  Fractional seconds are valid."
            " for instance, you could use: -sim 525.50"
        ),
    )
    parser.add_argument(
        "-eq",
        type=float,
        help=(
            "used to specify the length (in seconds) to equilibrate the"
            " system before running the simulation."
        ),
    )

    parser.add_argument(
        "-oStep",
        type=int,
        help=(
            " used to specify the number of times throughout the "
            " simulation that observables will be outputted.  Must "
            " be an integer value.  Default is to output once per "
            " simulation second."
        ),
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        default=False,
        help="specify verbose output to the console.",
    )

    parser.add_argument(
        "-b",
        action="store_true",
        default=False,
        help="use this flag to tell NFsim to output in binary (not ascii)",
    )
    parser.add_argument(
        "-notf",
        action="store_true",
        default=False,
        help=(
            " tells NFsim to Not use On The Fly output.  Normally"
            " observables are computed On The Fly - that is they are"
            " updated after every simulation step.  This is good if you"
            " output frequently or have many molecules in your system."
            " However, it can be faster to recompute observable counts"
            " right before you output especially if you don't output"
            " too often.  Use this flag to switch to recomputing at"
            " every output step instead of using On The Fly output."
        ),
    )
    parser.add_argument(
        "-ogf",
        action="store_true",
        default=False,
        help="output the value of all global functions.",
    )

    parser.add_argument("-utl", type=int, help="sets the universal traversal limit")

    parser.add_argument(
        "-nocslf",
        action="store_true",
        default=False,
        help=(
            "disable evaluation of complex-scoped local functions."
            " This may reduce run-time for some models, but will lead "
            " to erroneous results if complex-scoped local functions "
            " are required."
        ),
    )

    parser.add_argument(
        "-test",
        default=False,
        action="store_true",
        help=(
            " used to specify a given preprogrammed test. Some tests "
            '  include "tlbr" and "simple_system".  Tests do not read '
            "  in other command line flags "
        ),
    )

    parser.add_argument(
        "-seed",
        type=int,
        help=(
            "  used to specify the seed for the random number generator. "
            "  This allows you to run the same simulation and get the"
            "  exact same results perhaps to compare performance"
        ),
    )

    parser.add_argument(
        "-logo",
        default=False,
        action="store_true",
        help="prints out the ascii NFsim logo, for your viewing pleasure.",
    )
    args = vars(parser.parse_args())
    main(args)
