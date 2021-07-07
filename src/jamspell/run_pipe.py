import jamspell
import argparse
import os 

workdir = os.path.dirname(__file__)


def main(args):
    corrector = jamspell.TSpellCorrector()
    bin_file = os.path.join(workdir, 'en.bin')
    print(bin_file)
    corrector.LoadLangModel(bin_file) # (default) download from github page and place it in same folder

    with open(args.input, "r", encoding="utf-8") as inf, open(args.output, "w", encoding="utf-8") as outf:
        infile = inf.read().splitlines()
        outfile = [corrector.FixFragment(sent) for sent in infile]

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
