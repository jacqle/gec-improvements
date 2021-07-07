from unidecode import unidecode
import argparse
from tqdm import tqdm
import requests
import spacy

def predict_for_sentences(input_sentences, url):
    """Returns a list of corrected sentences."""
    predictions = []
    for sent in tqdm(input_sentences):
        parameters = {"text":sent}
        response = requests.get(url, params=parameters)
        json = response.json()
        predictions.append(json['gec']['autocorrect'])
    return predictions

def load_data(input_file):
    input_sentences = []
    with open(input_file) as istr:
        for l in istr.readlines():
            input_sentences.append(l.strip())
    return input_sentences
    
def write_file(output_sentences, output_file):
    with open(output_file, 'w') as ostr:
        ostr.write("\n".join([sent for sent in output_sentences]) + '\n') 

def main(args): 
    url = "https://api.writify.io/gec"
    nlp = spacy.load("en_core_web_sm")
    input_sentences = load_data(args.input)
    output_sentences = predict_for_sentences(input_sentences, url)
    output_sentences = [' '.join([token.text for token in nlp(sent)]) for sent in output_sentences]
    write_file(output_sentences, args.output)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GEC using Writify')
    parser.add_argument('-i', '--input', type=str, help='file containting one sentence per line')
    parser.add_argument('-o', '--output', type=str, help='file to store predictions')
    args = parser.parse_args()
    main(args)
