import math
import torch
import os
from pytorch_pretrained_bert import OpenAIGPTTokenizer, OpenAIGPTLMHeadModel
from collections import Counter
import argparse

workdir = os.path.dirname(__file__)

model = OpenAIGPTLMHeadModel.from_pretrained('openai-gpt')
model.eval()
# Load pre-trained model tokenizer (vocabulary)
tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')


def score(sentence):
        tokenize_input = tokenizer.tokenize(sentence)
        tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
        loss=model(tensor_input, lm_labels=tensor_input)
        return math.exp(loss)

def main(args):
    with open(args.input, "r") as infile:
        preds = infile.readlines()

    with open(os.path.join(workdir, "../../data/conll14st-test-data/origin_corpus.txt"), "r") as infile:
        errorful = infile.readlines()

    # Load pre-trained model (weights)
    
    scores = [(score(sents[0]), score(sents[1])) for sents in zip(errorful, preds)] # takes around 7 mins on colab on GPU

    print(Counter([score[0] >= score[1] for score in scores]))

    mask = [score[0] >= score[1] for score in scores]

    # if false: reject prediction
    final = [err if not m else pred for err, pred, m in zip(errorful, preds, mask)]

    with open(args.output, "w") as ostr:
        for s in final:
            print(s, file=ostr)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='GEC using Language Tools')
    parser.add_argument('-i', '--input', type=str, help='file containting one sentence per line')
    parser.add_argument('-o', '--output', type=str, help='file to store predictions')
    args = parser.parse_args()
    main(args)
