import argparse
import sys

from termcolor import colored

scales = [
    ("major", [0, 2, 4, 5, 7, 9, 11]),
    ("minor", [0, 2, 3, 5, 7, 8, 10]),
    ("melodic_minor", [0, 2, 3, 5, 7, 9, 11]),
    ("harmonic_minor", [0, 2, 3, 5, 7, 8, 11]),
    ("major_pentatonic", [0, 2, 4, 7, 9]),
    ("minor_pentatonic", [0, 3, 5, 7, 10]),
    ("dorian", [0, 2, 3, 5, 7, 9, 10]),
    ("phrygian", [0, 1, 3, 5, 7, 8, 10]),
    ("lydian", [0, 2, 4, 6, 7, 9, 11]),
    ("mixolydian", [0, 2, 4, 5, 7, 9, 10]),
    ("locrian", [0, 1, 3, 5, 6, 8, 10]),
    ("whole_tone", [0, 2, 4, 6, 8, 10]),
    ("half_whole_dim", [0, 1, 3, 4, 6, 7, 9, 10]),
    ("whole_half_dim", [0, 2, 3, 5, 6, 8, 9, 11]),
    ("messiaen3", [0, 2, 3, 4, 6, 7, 8, 10, 11]),
    ("messiaen4", [0, 1, 2, 5, 6, 7, 8, 11]),
    ("messiaen5", [0, 1, 5, 6, 7, 11]),
    ("messiaen6", [0, 2, 4, 5, 6, 8, 10, 11]),
    ("messiaen7", [0, 1, 2, 3, 5, 6, 7, 8, 9, 11]),
    ("chromatic", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
]

notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
tab_width = 3


def parse_tuning(tuning: str) -> list[int]:
    degrees = [notes.index(x) for x in tuning.split(",")]
    degrees.append(-1)  # fret_number
    return list(reversed(degrees))


def print_guitar(root: int, xs: list[int], tuning: list[int], frets: int) -> None:
    for open_string in tuning:
        for fret in range(frets + 1):
            if open_string == -1:  # fret_number
                s = colored(str(fret).ljust(tab_width), "light_grey", attrs=["reverse"])
            else:
                y = (open_string + fret) % 12
                if y == root:
                    s = colored(notes[y].ljust(tab_width), "light_cyan", attrs=["reverse"])
                elif y in xs:
                    s = colored(notes[y].ljust(tab_width), "light_blue", attrs=["reverse"])
                else:
                    s = notes[y].ljust(tab_width)
            print(f"|{s}", end="")
        print("|")


parser = argparse.ArgumentParser(prog="guitar_scale")
parser.add_argument("-r", "--root", type=int, help="root note degree", default=0)
parser.add_argument("-s", "--scale", type=str, help="scale name", default="major")
parser.add_argument("-t", "--tuning", type=str, help="tuning", default="e,a,d,g,b,e")
parser.add_argument("-f", "--frets", type=int, help="fret range", default=20)
parser.add_argument("--scales", help="show available scales", action="store_true")
args = parser.parse_args()

if args.scales:
    print([x for x, _ in scales])
    sys.exit(0)


xs = [(x + args.root) % 12 for x in dict(scales)[args.scale]]
tuning = parse_tuning(args.tuning)
print_guitar(args.root, xs, tuning, args.frets)
