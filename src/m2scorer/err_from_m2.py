import argparse

def main(args):
    with open(args.input, "r", encoding="utf-8") as inf, open(args.output, "w", encoding="utf-8") as outf:
        infile = inf.read().splitlines()
        outfile = [line.split("S ")[1] for line in infile if line.startswith("S ")]
        for sent in outfile:
            print(sent, file=outf)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input',
                        help='Path to the source file',
                        required=True)
    parser.add_argument('-out', '--output',
                        help='Path to the target file',
                        required=True)
    args = parser.parse_args()
    main(args)
