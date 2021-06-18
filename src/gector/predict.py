from gector.utils.preprocess_data import align_sequences, convert_tagged_line

from unidecode import unidecode


import argparse

from gector.utils.helpers import read_lines
from gector.gector.gec_model import GecBERTModel


def predict_for_sentences(input_sentences, model, batch_size=32):
    """Returns a list of corrected sentences."""

    predictions = []
    cnt_corrections = 0
    batch = []
    for sent in input_sentences:
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
    with open(output_file, w) as ostr:
        ostr.write("\n".join([" ".join(x) for x in predictions]) + '\n') 

def main(args): 
    model = model.load_model(
        vocab_path = "gector/data/output_vocabulary",
        model_paths = ["gector/data/model_files/xlnet_0_gector.th"],
        model_name = "xlnet"
    )
    input_sentences = load_data(args.input_file)
    output_sentences = predict_for_sentences(input_sentences, model)
    write_file(output_sentences, args.output_file)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GEC using gector')
    parser.add_argument('-i', '--input_file', type=str, help='file containting one sentence per line')
    parser.add_argument('-o', '--output_file', type=str, help='file to store predictions')
    args = parser.parse_args()
    main(args.input_file, args.output_file)
