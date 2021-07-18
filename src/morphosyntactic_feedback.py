import argparse 
import json
from typing import List, Tuple
import errant
from utils.glossary import POS_GLOSSARY, COMPOUND_VERBS_GLOSSARY

annotator = errant.load('en')

def get_feedback(input_sent: str, output_sent: str, messages_glossary) -> List[Tuple]:
    """Provide morphosyntactic feedback based on the predicted corrections.

    Arguments: tokenized original and corrected sentences
    Returns: a list of tuples containing pairs of (tokens offset in original (x, y), custom message)
    """
    messages = []
    orig = annotator.parse(input_sent, tokenise=False)
    cor = annotator.parse(output_sent, tokenise=False)
    edits = annotator.annotate(orig, cor)
    for e in edits:
        o_span = orig[e.o_start:e.o_end]
        c_span = cor[e.c_start:e.c_end]
        o_offset = (e.o_start, e.o_end)
        c_offset = (e.c_start, e.c_end)
        if 'OTHER' not in e.type:
            try:
                msg = get_message(o_span, c_span, e.type, messages_glossary)
                if msg:
                    messages.append((o_offset, msg))
            except:
                continue
    return messages


def get_message(o_span, c_span, type_, messages_glossary):
    msg = messages_glossary[type_]
    o_str = o_span.text
    c_str = c_span.text

    type_ = type_.split(':')
    if len(type_) == 3:
        operation, pos, category = type_
    else:
        operation, pos = type_
        if operation == 'M':
            c_str = c_str.replace(o_str.lower(), '').strip()
        elif operation == 'U':
            o_str = o_str.replace(c_str.lower(), '').strip()

    o_tag = get_pos_tag(o_span, pos)
    c_tag = get_pos_tag(c_span, pos)

    replacements = [
        ('o_span', o_str),
        ('c_span', c_str),
        ('o_tag', o_tag),
        ('c_tag', c_tag),
    ]
    for tup in replacements:
        msg = msg.replace(*tup)

    if 'UNKNOWN' in msg:
        return None
    else:
        return msg


def get_pos_tag(span, pos):
    if len(span) > 1:
        tag = 'UNKNOWN'
        tags = '_'.join([tok.tag_ for tok in span])
        if pos == 'VERB':
            if 'MD' in tags:
                print(tags)
                tag = 'modal verb'
            elif span[0].text == 'to':
                tag = 'to-infinitive'
            elif span[0].lemma_ == 'be' and span[1].tag_ == 'VBN':
                tag = 'passive voice'
            else:
                if tags in COMPOUND_VERBS_GLOSSARY:
                    tag = COMPOUND_VERBS_GLOSSARY[tags] 
    else:
        tag = POS_GLOSSARY[span[0].tag_]
    return tag


def load_data(input_file):
    input_sentences = []
    with open(input_file) as istr:
        for l in istr.readlines():
            input_sentences.append(l.strip())
    return input_sentences

def load_messages_glossary(msg_file):
    with open(msg_file, 'r') as istr:
        messages_glossary = json.load(istr)
    return messages_glossary

def main(args):
    input_sentences = load_data(args.input_file)
    output_sentences = load_data(args.output_file)
    messages_glossary = load_messages_glossary('src/utils/messages.txt')
    with open('feedback_v2.txt', 'w') as ostr:
        for input_sent, output_sent in zip(input_sentences, output_sentences):
            messages = get_feedback(input_sent, output_sent, messages_glossary)
            if messages:
                print('input: ', input_sent, file=ostr)
                print('output:', output_sent, file=ostr)
                for offset, msg in messages:
                    print(offset, msg, file=ostr)
                print('', file=ostr)


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GEC using gector')
    parser.add_argument('-i', '--input_file', type=str, help='file containting one sentence per line')
    parser.add_argument('-o', '--output_file', type=str, help='corrected lines')
    args = parser.parse_args()
    main(args)
