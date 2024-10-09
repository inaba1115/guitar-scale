import argparse
import sys

from termcolor import colored

scales = [
    ("major", [0, 2, 4, 5, 7, 9, 11]),
    ("minor", [0, 2, 3, 5, 7, 8, 10]),
    ("dorian", [0, 2, 3, 5, 7, 9, 10]),
    ("mixolydian", [0, 2, 4, 5, 7, 9, 10]),
    ("lydian", [0, 2, 4, 6, 7, 9, 11]),
    ("phrygian", [0, 1, 3, 5, 7, 8, 10]),
    ("locrian", [0, 1, 3, 5, 6, 8, 10]),
    ("whole_tone", [0, 2, 4, 6, 8, 10]),
    ("half_whole_dim", [0, 1, 3, 4, 6, 7, 9, 10]),
    ("whole_half_dim", [0, 2, 3, 5, 6, 8, 9, 11]),
    ("minor_blues", [0, 3, 5, 6, 7, 10]),
    ("minor_pentatonic", [0, 3, 5, 7, 10]),
    ("major_pentatonic", [0, 2, 4, 7, 9]),
    ("harmonic_minor", [0, 2, 3, 5, 7, 8, 11]),
    ("harmonic_major", [0, 2, 4, 5, 7, 8, 11]),
    ("dorian_#4", [0, 2, 3, 6, 7, 9, 10]),
    ("phrygian_dominant", [0, 1, 4, 5, 7, 8, 10]),
    ("melodic_minor", [0, 2, 3, 5, 7, 9, 11]),
    ("lydian_augmented", [0, 2, 4, 6, 8, 9, 11]),
    ("lydian_dominant", [0, 2, 4, 6, 7, 9, 10]),
    ("super_locrian", [0, 1, 3, 4, 6, 8, 10]),
    ("8_tone_spanish", [0, 1, 3, 4, 5, 6, 8, 10]),
    ("bhairav", [0, 1, 4, 5, 7, 8, 11]),
    ("hungarian_minor", [0, 2, 3, 6, 7, 8, 11]),
    ("hirajoshi", [0, 2, 3, 7, 8]),
    ("in_sen", [0, 1, 5, 7, 10]),
    ("iwato", [0, 1, 5, 6, 10]),
    ("kumoi", [0, 2, 3, 7, 9]),
    ("pelog_selisir", [0, 1, 3, 7, 8]),
    ("pelog_tembung", [0, 1, 5, 7, 8]),
    ("messiaen3", [0, 2, 3, 4, 6, 7, 8, 10, 11]),
    ("messiaen4", [0, 1, 2, 5, 6, 7, 8, 11]),
    ("messiaen5", [0, 1, 5, 6, 7, 11]),
    ("messiaen6", [0, 2, 4, 5, 6, 8, 10, 11]),
    ("messiaen7", [0, 1, 2, 3, 5, 6, 7, 8, 9, 11]),
    ("chromatic", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
]

choices = [x for x, _ in scales]
degrees = dict((x, y) for x, y in scales)

notes = {
    0: "c",
    1: "c#",
    2: "d",
    3: "d#",
    4: "e",
    5: "f",
    6: "f#",
    7: "g",
    8: "g#",
    9: "a",
    10: "a#",
    11: "b",
}

TUNING = [-1, 4, 11, 7, 2, 9, 4]  # <fret_number>, E, B, G, D, A, E
TAB_WIDTH = 3


def print_guitar(root: int, xs: list[int], frets: int) -> None:
    for open_string in TUNING:
        for fret in range(frets + 1):
            if open_string == -1:
                s = colored(str(fret).ljust(TAB_WIDTH), "light_grey", attrs=["reverse"])
            else:
                y = (open_string + fret) % 12
                if y == root:
                    s = colored(notes[y].ljust(TAB_WIDTH), "light_cyan", attrs=["reverse"])
                elif y in xs:
                    s = colored(notes[y].ljust(TAB_WIDTH), "light_blue", attrs=["reverse"])
                else:
                    s = notes[y].ljust(TAB_WIDTH)
            print(f"|{s}", end="")
        print("|")


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--root", type=int, help="root note degree", default=0)
parser.add_argument("-s", "--scale", type=str, help="scale name", default="major", choices=choices)
parser.add_argument("-f", "--frets", type=int, help="fret range", default=20)
parser.add_argument("--scales", help="show available scales", action="store_true")
args = parser.parse_args()

if args.scales:
    print(choices)
    sys.exit(0)


xs = [(x + args.root) % 12 for x in degrees[args.scale]]
print_guitar(args.root, xs, args.frets)
