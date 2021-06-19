# gec-improvements


## Evaluation

- The reference test set is located at `data/conll14st-test-data/noalt/official-2014.combined.{m2|txt}`
- Using ERRANT for evaluation:
    1. errant_parallel -orig <orig_file> -cor <cor_file1> [<cor_file2> ...] -out <out_m2>
    2. errant_compare -hyp <hyp_m2> -ref <ref_m2> 

- Baseline GECToR (XLNet, Confidence bias=0.35, Min error prob=0.66):
   ``` 
    =========== Span-Based Correction ============
    TP      FP      FN      Prec    Rec     F0.5
    1001    369     1609    0.7307  0.3835  0.6187
    ==============================================
   ``` 