import jamspell
import argparse
import os 

workdir = os.path.dirname(__file__)

min_len = 5


with open(os.path.join(workdir, "../us_filter/us2gb.txt"), 'r') as infile:
    txt = infile.readlines()[1:]
    gb, us = list(zip(*[el.strip().split("\t") for el in txt]))
    
    skip_region_words = set().union(gb,us)

# print(skip_region_words)



def main(args):
    corrector = jamspell.TSpellCorrector()
    bin_file = os.path.join(workdir, 'en.bin')
    print(bin_file)
    corrector.LoadLangModel(bin_file) # (default) download from github page and place it in same folder

    with open(args.input, "r", encoding="utf-8") as inf, open(args.output, "w", encoding="utf-8") as outf:
        infile = inf.read().splitlines()

        for sent in infile :
            corr = corrector.FixFragment(sent)
            err_tok = sent.split(' ')
            corr_tok = corr.split(' ')

            # Assuming that jamspell doesn't change the number of tokens in the sentence
            for i in range(len(err_tok)):

                # here is the filtering of regionalized words
                # and of the short words

                if err_tok[i] in skip_region_words or len(err_tok[i]) < min_len:
                    corr_tok[i] = err_tok[i]

            out_sent = ' '.join(corr_tok)
            print(out_sent, file=outf)


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
