import argparse
import re
import os

workdir = os.path.dirname(__file__)

with open(os.path.join(workdir, "us2gb.txt"), 'r') as infile:
    txt = infile.readlines()[1:]
    gb, us = list(zip(*[el.strip().split("\t") for el in txt]))
    us2gb = dict(zip(us,gb))

# print(us2gb)

def filter_file(input_file, output_file):
    with open(input_file,'r') as infile:
        content = infile.read()
    
    # filtering
    for key, value in us2gb.items():
        content = re.sub(r"\b{}\b".format(key), value, content, flags = re.IGNORECASE | re. MULTILINE)

        # content.replace(key, value)

    with open(output_file, 'w') as outfile:
        print(content, file = outfile)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input',
                        help='Path to the source file',
                        required=True)
    parser.add_argument('-out', '--output',
                        help='Path to the output file',
                        required=True)
    args = parser.parse_args()

    filter_file(args.input, output_file = args.output)
    pass