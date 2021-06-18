import argparse
from tqdm import tqdm

from src.gector.utils.helpers import read_lines
from src.gector.gector.gec_model import GecBERTModel


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