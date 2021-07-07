from unidecode import unidecode
import argparse
from tqdm import tqdm
import language_tool_python
import spacy

def predict_for_sentences(input_sentences, tool):
    """Returns a list of corrected sentences."""
    predictions = [tool.correct(sent) for sent in tqdm(input_sentences)]
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
    tool = language_tool_python.LanguageTool('en-US')
    nlp = spacy.load("en_core_web_sm")
    input_sentences = load_data(args.input)
    output_sentences = predict_for_sentences(input_sentences, tool)
    output_sentences = [' '.join([token.text for token in nlp(sent)]) for sent in output_sentences]
    write_file(output_sentences, args.output)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GEC using Language Tools')
    parser.add_argument('-i', '--input', type=str, help='file containting one sentence per line')
    parser.add_argument('-o', '--output', type=str, help='file to store predictions')
    args = parser.parse_args()
    main(args)
