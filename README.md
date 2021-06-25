# gec-improvements

## Installation

Use the following commands to install from source:
```
conda create -n gec python=3.7
conda activate gec
git clone https://github.com/jacqle/gec-improvements.git
cd gec-improvements
pip3 install -r requirements.txt
cd src/errant
pip3 install -e .
python3 -m spacy download en
```
Errant has to be installed from source as its source code has been modified to solve dependency conflicts. 

Note that Python 3.7 is required. 

## Evaluation

The reference test set is located at `data/conll14st-test-data/noalt/official-2014.combined.{m2|txt}`

### Using ERRANT for evaluation
1. `errant_parallel -orig <orig_file> -cor <cor_file1> [<cor_file2> ...] -out <out_m2>`
2. `errant_compare -hyp <hyp_m2> -ref <ref_m2>`

### Baselines
- GECToR (XLNet, Confidence bias=0.35, Min error prob=0.66):
   ``` 
    =========== Span-Based Correction ============
    TP      FP      FN      Prec    Rec     F0.5
    1001    369     1609    0.7307  0.3835  0.6187
    ============================================== 
    ``` 
- Language Tools:
    ```
    =========== Span-Based Correction ============
    TP      FP      FN      Prec    Rec     F0.5
    243     453     1985    0.3501  0.1095  0.2432
    ==============================================
    ```
- Writify:
    ```
    =========== Span-Based Correction ============
    TP      FP      FN      Prec    Rec     F0.5
    338     621     1907    0.3525  0.1506  0.2779
    ==============================================
    ```
## Tweaking GECToR's parameters
- Confidence bias=0.4, Min error prob=0.7
   ``` 
   =========== Span-Based Correction ============
   TP      FP      FN      Prec    Rec     F0.5
   935     306     1652    0.7534  0.3614  0.6191
   ==============================================  
   ``` 
- Confidence bias=0.4, Min error prob=0.75
   ``` 
   =========== Span-Based Correction ============
   TP      FP      FN      Prec    Rec     F0.5
   832     245     1685    0.7725  0.3306  0.6095
   ==============================================
   ``` 
- Confidence bias=0.3, Min error prob=0.77
   ``` 
   =========== Span-Based Correction ============
   TP      FP      FN      Prec    Rec     F0.5
   792     220     1690    0.7826  0.3191  0.6064
   ==============================================   
   ``` 
