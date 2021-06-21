# Analysis of the coverage of gector and LT per error category

The gold M2 file is located at `gec-improvements/data/conll14st-test-data/noalt/official-2014.combined.m2`. It can be converted in the errant standard by running `errant_m2 -gold gec-improvements/data/conll14st-test-data/noalt/official-2014.combined.m2 -out gec-improvements/src/cat_analysis/gold_m2.m2`.

From there, the source errorful text can be obtained by executing `python src/m2scorer/err_from_m2.py -in src/cat_analysis/gold_m2.m2 -out src/cat_analysis/origin_corpus.txt`

The predictions of GECtoR are located at `gec-improvements/data/preds_gector_conll`. We can obtain the M2 file comparing the errorful corpus with GECtoR's corrections : `errant_parallel -orig src/cat_analysis/origin_corpus.txt -cor data/preds_gector_conll -out src/cat_analysis/gector_m2.m2`. 

Now, we have two M2 files: 
- `src/cat_analysis/gold_m2.m2`: the golden annotations between the errorful and the manually corrected corpus.
- `src/cat_analysis/gector_m2.m2`: the annotations of what gector has been able to correct from between the errorful corpus.

Finally, one can run `errant_compare -cat 2 -hyp src/cat_analysis/gector_m2.m2 -ref src/cat_analysis/gold_m2.m2` to compare the GECtoR's and golden corrections.  The level of granularity is controled with the parameter `-cat`. 

```py
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
ADJ            3        7        36       0.3      0.0769   0.1899
ADJ:FORM       5        0        4        1.0      0.5556   0.8621
ADV            7        5        30       0.5833   0.1892   0.4118
CONJ           1        0        14       1.0      0.0667   0.2632
CONTR          0        0        1        1.0      0.0      0.0
DET            204      81       194      0.7158   0.5126   0.6632
MORPH          28       15       60       0.6512   0.3182   0.5385
NOUN           16       4        98       0.8      0.1404   0.4124
NOUN:INFL      6        3        0        0.6667   1.0      0.7143
NOUN:NUM       134      25       69       0.8428   0.6601   0.7986
NOUN:POSS      6        4        15       0.6      0.2857   0.4918
ORTH           15       7        24       0.6818   0.3846   0.5906
OTHER          20       30       340      0.4      0.0556   0.1786
PART           21       9        16       0.7      0.5676   0.6688
PREP           110      36       151      0.7534   0.4215   0.6509
PRON           13       7        47       0.65     0.2167   0.4643
PUNCT          102      48       102      0.68     0.5      0.6343
SPELL          50       7        39       0.8772   0.5618   0.7886
VERB           35       17       131      0.6731   0.2108   0.4679
VERB:FORM      70       28       39       0.7143   0.6422   0.6986
VERB:INFL      1        0        1        1.0      0.5      0.8333
VERB:SVA       80       16       37       0.8333   0.6838   0.7984
VERB:TENSE     63       25       114      0.7159   0.3559   0.5955
WO             6        2        15       0.75     0.2857   0.566

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
996     376     1577    0.7259  0.3871  0.6178
==============================================
```

One can go even more fine-grained : 
```py
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
M:ADJ          0        0        3        1.0      0.0      0.0
M:ADV          1        1        5        0.5      0.1667   0.3571
M:CONJ         0        0        8        1.0      0.0      0.0
M:DET          69       35       72       0.6635   0.4894   0.6194
M:NOUN         0        0        14       1.0      0.0      0.0
M:NOUN:POSS    4        2        5        0.6667   0.4444   0.6061
M:OTHER        1        3        20       0.25     0.0476   0.1351
M:PART         1        1        5        0.5      0.1667   0.3571
M:PREP         15       8        41       0.6522   0.2679   0.5068
M:PRON         4        2        8        0.6667   0.3333   0.5556
M:PUNCT        81       41       61       0.6639   0.5704   0.6429
M:VERB         11       3        12       0.7857   0.4783   0.6962
M:VERB:FORM    1        0        4        1.0      0.2      0.5556
M:VERB:TENSE   11       7        13       0.6111   0.4583   0.5729
R:ADJ          3        4        26       0.4286   0.1034   0.2632
R:ADJ:FORM     5        0        4        1.0      0.5556   0.8621
R:ADV          1        3        11       0.25     0.0833   0.1786
R:CONJ         0        0        3        1.0      0.0      0.0
R:CONTR        0        0        1        1.0      0.0      0.0
R:DET          33       10       41       0.7674   0.4459   0.6707
R:MORPH        28       15       60       0.6512   0.3182   0.5385
R:NOUN         15       3        69       0.8333   0.1786   0.4808
R:NOUN:INFL    6        3        0        0.6667   1.0      0.7143
R:NOUN:NUM     134      25       69       0.8428   0.6601   0.7986
R:NOUN:POSS    1        1        8        0.5      0.1111   0.2941
R:ORTH         15       7        24       0.6818   0.3846   0.5906
R:OTHER        17       21       276      0.4474   0.058    0.191
R:PART         18       7        8        0.72     0.6923   0.7143
R:PREP         67       22       80       0.7528   0.4558   0.666
R:PRON         8        5        30       0.6154   0.2105   0.4444
R:PUNCT        16       4        30       0.8      0.3478   0.6349
R:SPELL        50       7        39       0.8772   0.5618   0.7886
R:VERB         17       9        99       0.6538   0.1466   0.3864
R:VERB:FORM    69       27       28       0.7188   0.7113   0.7173
R:VERB:INFL    1        0        1        1.0      0.5      0.8333
R:VERB:SVA     80       16       37       0.8333   0.6838   0.7984
R:VERB:TENSE   45       9        87       0.8333   0.3409   0.6466
R:WO           6        2        15       0.75     0.2857   0.566
U:ADJ          0        3        7        0.0      0.0      0.0
U:ADV          5        1        14       0.8333   0.2632   0.5814
U:CONJ         1        0        3        1.0      0.25     0.625
U:DET          102      36       81       0.7391   0.5574   0.6939
U:NOUN         1        1        15       0.5      0.0625   0.2083
U:NOUN:POSS    1        1        2        0.5      0.3333   0.4545
U:OTHER        2        6        44       0.25     0.0435   0.1282
U:PART         2        1        3        0.6667   0.4      0.5882
U:PREP         28       6        30       0.8235   0.4828   0.7216
U:PRON         1        0        9        1.0      0.1      0.3571
U:PUNCT        5        3        11       0.625    0.3125   0.5208
U:VERB         7        5        20       0.5833   0.2593   0.4667
U:VERB:FORM    0        1        7        0.0      0.0      0.0
U:VERB:TENSE   7        9        14       0.4375   0.3333   0.4118

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
996     376     1577    0.7259  0.3871  0.6178
==============================================
```