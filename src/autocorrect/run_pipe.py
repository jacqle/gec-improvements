from autocorrect import Speller
import argparse
import os 

workdir = os.path.dirname(__file__)


def main(args):
    spell = Speller()

    with open(args.input, "r", encoding="utf-8") as inf, open(args.output, "w", encoding="utf-8") as outf:
        infile = inf.read().splitlines()
        outfile = [spell(sent) for sent in infile]

        for sent in outfile:
            print(sent, file=outf)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input',
                        help='Path to the source file',
                        required=True)
    parser.add_argument('-out', '--output',
                        help='Path to the output file',
                        required=True)
    args = parser.parse_args()
    main(args)
