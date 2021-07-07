from unidecode import unidecode
import argparse
from tqdm import tqdm

from model import load_model
from utils.helpers import read_lines
from gector.gec_model import GecBERTModel
from utils.preprocess_data import align_sequences, convert_tagged_line

import os

workdir = os.path.dirname(__file__)


def predict_for_sentences(input_sentences, model, batch_size=32):
    """Returns a list of corrected sentences."""

    predictions = []
    cnt_corrections = 0
    batch = []
    for sent in tqdm(input_sentences):
        batch.append(sent)
        if len(batch) == batch_size:
            preds, cnt = model.handle_batch(batch)
            predictions.extend(preds)
            cnt_corrections += cnt
            batch = []
    if batch:
        preds, cnt = model.handle_batch(batch)
        predictions.extend(preds)
        cnt_corrections += cnt
    return predictions
    
#class Corrector:
#    def __init__(self, input_sentences, model):
#        self.input_sentences = input_sentences
#        self.model = model

def load_data(input_file):
    input_sentences = []
    with open(input_file) as istr:
        for l in istr.readlines():
            input_sentences.append(l.strip())
    return input_sentences
    
def write_file(output_sentences, output_file):
    with open(output_file, 'w') as ostr:
        ostr.write("\n".join([" ".join(x) for x in output_sentences]) + '\n') 

def main(args): 
    model = load_model(
        vocab_path = os.path.join(workdir, "data/output_vocabulary"),
        model_paths = [os.path.join(workdir,"data/model_files/xlnet_0_gector.th")],
        model_name = "xlnet",
        confidence = args.confidence_bias,
        min_error_probability = args.min_error_prob,
    )
    input_sentences = load_data(args.input)
    input_sentences = [sent.split() for sent in input_sentences]
    output_sentences = predict_for_sentences(input_sentences, model)
    write_file(output_sentences, args.output)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GEC using gector')
    parser.add_argument('-i', '--input', type=str, help='file containting one sentence per line', required=True)
    parser.add_argument('-o', '--output', type=str, help='file to store predictions', required=True)
    parser.add_argument('--confidence_bias', type=float, default=0.3, help='value for the confidence bias')
    parser.add_argument('--min_error_prob', type=float, default=0.77, help='value for the min error probability')
    args = parser.parse_args()
    main(args)
