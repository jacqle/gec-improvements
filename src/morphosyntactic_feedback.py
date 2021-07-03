import argparse 
import errant
from utils.glossary import GLOSSARY

annotator = errant.load('en')

messages = {
    'M:ADJ': "Missing adjective 'c_str'",
    'M:ADV': "Missing adverb 'c_str'",
    'M:CONJ': "Missing conjunction 'c_str'",
    'M:DET': "Missing determiner 'c_str'",
    'M:NOUN': "Missing noun 'c_str'",
    'M:PART': "Missing particle 'c_str'",
    'M:PREP': "Missing preposition 'c_str'",
    'M:PRON': "Missing pronoun 'c_str'",
    'M:PUNCT': "Missing punctuation marker 'c_str'",
    'M:VERB': "Missing verb 'c_str'",
    'U:ADJ': "Unnecessary adjective 'o_str'",
    'U:ADV': "Unnecessary adverb 'o_str'",
    'U:CONJ': "Unnecessary conjunction 'o_str'",
    'U:DET': "Unnecessary determiner 'o_str'",
    'U:NOUN': "Unnecessary noun 'o_str'",
    'U:PART': "Unnecessary particle 'o_str'",
    'U:PREP': "Unnecessary preposition 'o_str'",
    'U:PRON': "Unnecessary pronoun 'o_str'",
    'U:PUNCT': "Unnecessary punctuation 'o_str'",
    'U:VERB': "Unnecessary verb 'o_str'",
    'R:ADJ': "Adjective 'o_str' replaced by 'c_str'",
    'R:ADV': "Adverb 'o_str' replaced by 'c_str'",
    'R:CONJ': "Conjunction 'o_str' replaced by 'c_str'",
    'R:DET': "Determiner 'o_str' replaced by 'c_str'",
    'R:NOUN': "Noun 'o_str' replaced by 'c_str'",
    'R:PART': "Particle 'o_str' replaced by 'c_str'",
    'R:PREP': "Preposition 'o_str' replaced by 'c_str'",
    'R:PRON': "Pronoun 'o_str' replaced by 'c_str'",
    'R:PUNCT': "Punctuation mark 'o_str' replaced by 'c_str'",
    'R:VERB': "Verb 'o_str' replaced by 'c_str'",
    'M:CONTR': "Missing contraction 'c_str'",
    #'M:OTHER': "",
    'U:CONTR': "Unnecessary contraction 'o_str'",
    #'U:OTHER': "",
    'R:CONTR': "There seems to be a contraction error for word 'o_str'",
    'R:MORPH': "There seems to be a morphological error for word 'o_str'",
    'R:ORTH': "There seems to be an orthography error for word 'o_str'",
    #'R:OTHER': "",
    'R:SPELL': "There seems to be a spelling mistake for word 'o_str'",
    #'R:WO': "",
    'M:NOUN:POSS': "Missing possessive marker for noun 'o_str'",
    'M:VERB:FORM': "Missing 'c_str'", # TODO: send -> to send OK, but missing word in second position not handled
    'M:VERB:TENSE': "Missing c_tag 'c_str'",
    'U:NOUN:POSS': "Unnecessary possessive marker 'o_str'",
    'U:VERB:FORM': "Unnessary 'o_str'",
    'U:VERB:TENSE': "o_tag is unnessary here",
    'R:ADJ:FORM': "The adjective 'o_str' does not have the correct form here, use 'c_str' instead",
    'R:NOUN:INFL': "Noun 'o_str' ending seems to be incorrect",
    'R:NOUN:NUM': "The number of noun 'o_str' should be c_tag instead of o_tag",
    #'R:NOUN:POSS': "",
    'R:VERB:FORM': "The verb 'o_str' does not have the correct form here (o_tag), use 'c_str' in the c_tag instead",
    'R:VERB:INFL': "The verb 'o_str' does not have the correct inflection here, use 'c_str' instead",
    #'R:VERB:SVA': "",
    'R:VERB:TENSE': "Verb 'o_str' (o_tag) should be in the c_tag here"
}


def load_data(input_file):
    input_sentences = []
    with open(input_file) as istr:
        for l in istr.readlines():
            input_sentences.append(l.strip())
    return input_sentences

def get_message(o_str, c_str, type_):
    msg = messages[type_]
    replacements = [
        ('o_str', o_str.text),
        ('c_str', c_str.text),
        ('o_tag', GLOSSARY[o_str.tag_]),
        ('c_tag', GLOSSARY[c_str.tag_]),
        ('o_dep', GLOSSARY[o_str.dep_.lower()]),
        ('c_dep', GLOSSARY[c_str.dep_.lower()]),
    ]
    for tup in replacements:
        msg = msg.replace(*tup)
    return msg


def get_feedback(input_sent, output_sent):
    messages = []
    orig = annotator.parse(input_sent, tokenise=False)
    cor = annotator.parse(output_sent, tokenise=False)
    edits = annotator.annotate(orig, cor)
    if edits:
        #print(input_sent)
        #print(output_sent)
        for e in edits:
            #print(e.o_start, e.o_end, e.o_str, e.c_start, e.c_end, e.c_str, e.type)
            o_span = orig[e.o_start:e.o_end]
            c_span = cor[e.c_start:e.c_end]
            o_str = o_span[0]
            c_str = c_span[0]
            o_offset = (e.o_start, e.o_end)
            c_offset = (e.c_start, e.c_end)
            type_ = e.type.split(':')
            if (len(o_span) > 1 or len(c_span) > 1) and type_[1] != 'OTHER':
                if e.type == 'R:WO':
                    msg = f"Incorrect word order in sequence '{o_span.text}', use '{c_span.text}' instead"
                    messages.append((o_offset, msg))
                    continue
                print(o_span, len(o_span))
                print(c_span, len(c_span))
                print('===='*8)
                #raise ValueError
            if type_[1] == 'OTHER':
                continue
            else:
                try:
                    msg = get_message(o_str, c_str, e.type)
                    messages.append((o_offset, msg))
                except:
                    if e.type == 'R:VERB:SVA': # TODO
                        continue
                    print(o_str.tag_, o_str.dep_, list(o_str.children))
                    print(c_str.tag_, c_str.dep_, list(c_str.children))
                    raise ValueError
    return messages


def main(args):
    input_sentences = load_data(args.input_file)
    output_sentences = load_data(args.output_file)
    with open('feedback_v1.txt', 'w') as ostr:
        for input_sent, output_sent in zip(input_sentences, output_sentences):
            messages = get_feedback(input_sent, output_sent)
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

