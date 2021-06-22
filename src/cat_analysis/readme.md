# Analysis of the coverage of GECtoR and LT per error category


The gold M2 file is located at `gec-improvements/data/conll14st-test-data/noalt/official-2014.combined.m2`. It can be converted in the errant standard by running `errant_m2 -gold gec-improvements/data/conll14st-test-data/noalt/official-2014.combined.m2 -out gec-improvements/src/cat_analysis/gold_m2.m2`.

From there, the source errorful text can be obtained by executing `python src/m2scorer/err_from_m2.py -in src/cat_analysis/gold_m2.m2 -out src/cat_analysis/origin_corpus.txt`

## GECtoR
The predictions of GECtoR are located at `gec-improvements/data/preds_gector_conll`. We can obtain the M2 file comparing the errorful corpus with GECtoR's corrections : `errant_parallel -orig src/cat_analysis/origin_corpus.txt -cor data/preds_gector_conll_030_077 -out src/cat_analysis/gector_m2.m2`. 

Now, we have two M2 files: 
- `src/cat_analysis/gold_m2.m2`: the golden annotations between the errorful and the manually corrected corpus.
- `src/cat_analysis/gector_m2.m2`: the annotations of what gector has been able to correct between the errorful corpus.

Finally, one can run `errant_compare -cat 2 -hyp src/cat_analysis/gector_m2.m2 -ref src/cat_analysis/gold_m2.m2` to compare the GECtoR's and golden corrections.  The level of granularity is controled with the parameter `-cat`. 

```py
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
ADJ            3        5        30       0.375    0.0909   0.2308
ADJ:FORM       3        0        6        1.0      0.3333   0.7143
ADV            4        4        33       0.5      0.1081   0.2899
CONJ           1        0        12       1.0      0.0769   0.2941
CONTR          0        0        1        1.0      0.0      0.0
DET            161      44       218      0.7854   0.4248   0.6714
MORPH          20       13       62       0.6061   0.2439   0.4673
NOUN           11       3        94       0.7857   0.1048   0.3416
NOUN:INFL      6        2        0        0.75     1.0      0.7895
NOUN:NUM       113      16       86       0.876    0.5678   0.7902
NOUN:POSS      4        2        18       0.6667   0.1818   0.4348
ORTH           9        3        22       0.75     0.2903   0.5696
OTHER          15       17       348      0.4688   0.0413   0.1527
PART           15       7        17       0.6818   0.4688   0.625
PREP           95       21       155      0.819    0.38     0.6653
PRON           7        3        50       0.7      0.1228   0.3608
PUNCT          75       27       107      0.7353   0.4121   0.6356
SPELL          48       6        38       0.8889   0.5581   0.7947
VERB           26       14       137      0.65     0.1595   0.4025
VERB:FORM      61       13       40       0.8243   0.604    0.7683
VERB:INFL      1        0        1        1.0      0.5      0.8333
VERB:SVA       65       10       46       0.8667   0.5856   0.7908
VERB:TENSE     44       12       127      0.7857   0.2573   0.557
WO             4        1        16       0.8      0.2      0.5

=========== Span-Based Correction ============
TP	FP	FN	Prec	Rec	F0.5
791	223	1664	0.7801	0.3222	0.6074
==============================================
```

One can go even more fine-grained : 
```py
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
M:ADJ          0        0        3        1.0      0.0      0.0
M:ADV          1        1        5        0.5      0.1667   0.3571
M:CONJ         0        0        7        1.0      0.0      0.0
M:DET          54       17       79       0.7606   0.406    0.6475
M:NOUN         0        0        15       1.0      0.0      0.0
M:NOUN:POSS    3        1        6        0.75     0.3333   0.6
M:OTHER        1        2        17       0.3333   0.0556   0.1667
M:PART         0        1        5        0.0      0.0      0.0
M:PREP         12       6        41       0.6667   0.2264   0.48
M:PRON         1        1        9        0.5      0.1      0.2778
M:PUNCT        62       22       59       0.7381   0.5124   0.6783
M:VERB         11       3        12       0.7857   0.4783   0.6962
M:VERB:FORM    1        0        2        1.0      0.3333   0.7143
M:VERB:TENSE   5        5        17       0.5      0.2273   0.4032
R:ADJ          3        1        20       0.75     0.1304   0.3846
R:ADJ:FORM     3        0        6        1.0      0.3333   0.7143
R:ADV          0        3        12       0.0      0.0      0.0
R:CONJ         0        0        2        1.0      0.0      0.0
R:CONTR        0        0        1        1.0      0.0      0.0
R:DET          23       3        43       0.8846   0.3485   0.6765
R:MORPH        20       13       62       0.6061   0.2439   0.4673
R:NOUN         11       3        67       0.7857   0.141    0.4104
R:NOUN:INFL    6        2        0        0.75     1.0      0.7895
R:NOUN:NUM     113      16       86       0.876    0.5678   0.7902
R:NOUN:POSS    0        0        10       1.0      0.0      0.0
R:ORTH         9        3        22       0.75     0.2903   0.5696
R:OTHER        12       12       284      0.5      0.0405   0.1531
R:PART         14       5        9        0.7368   0.6087   0.7071
R:PREP         59       13       81       0.8194   0.4214   0.6893
R:PRON         5        2        32       0.7143   0.1351   0.3846
R:PUNCT        9        3        37       0.75     0.1957   0.4787
R:SPELL        48       6        38       0.8889   0.5581   0.7947
R:VERB         8        6        106      0.5714   0.0702   0.2353
R:VERB:FORM    60       13       31       0.8219   0.6593   0.7833
R:VERB:INFL    1        0        1        1.0      0.5      0.8333
R:VERB:SVA     65       10       46       0.8667   0.5856   0.7908
R:VERB:TENSE   33       3        92       0.9167   0.264    0.6134
R:WO           4        1        16       0.8      0.2      0.5
U:ADJ          0        4        7        0.0      0.0      0.0
U:ADV          3        0        16       1.0      0.1579   0.4839
U:CONJ         1        0        3        1.0      0.25     0.625
U:DET          84       24       96       0.7778   0.4667   0.6863
U:NOUN         0        0        12       1.0      0.0      0.0
U:NOUN:POSS    1        1        2        0.5      0.3333   0.4545
U:OTHER        2        3        47       0.4      0.0408   0.1449
U:PART         1        1        3        0.5      0.25     0.4167
U:PREP         24       2        33       0.9231   0.4211   0.7453
U:PRON         1        0        9        1.0      0.1      0.3571
U:PUNCT        4        2        11       0.6667   0.2667   0.5128
U:VERB         7        5        19       0.5833   0.2692   0.473
U:VERB:FORM    0        0        7        1.0      0.0      0.0
U:VERB:TENSE   6        4        18       0.6      0.25     0.4688

=========== Span-Based Correction ============
TP	FP	FN	Prec	Rec	F0.5
791	223	1664	0.7801	0.3222	0.6074
==============================================
```

## Language tool

Same process. The M2 file of LT is obtained executing `errant_parallel -orig src/cat_analysis/origin_corpus.txt -cor data/preds_lt_conll -out src/cat_analysis/lt_m2.m2`

The two M2 files are compared with `errant_compare -cat 2 -hyp src/cat_analysis/lt_m2.m2 -ref src/cat_analysis/gold_m2.m2`


Level-2 fine-grained
```py
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
ADJ            3        3        22       0.5      0.12     0.3061
ADJ:FORM       2        0        5        1.0      0.2857   0.6667
ADV            1        1        31       0.5      0.0312   0.125
CONJ           0        0        10       1.0      0.0      0.0
CONTR          0        1        1        0.0      0.0      0.0
DET            14       3        326      0.8235   0.0412   0.1716
MORPH          7        21       74       0.25     0.0864   0.1813
NOUN           1        8        90       0.1111   0.011    0.0394
NOUN:INFL      5        0        3        1.0      0.625    0.8929
NOUN:NUM       4        5        155      0.4444   0.0252   0.1026
NOUN:POSS      1        3        16       0.25     0.0588   0.1515
ORTH           46       197      18       0.1893   0.7188   0.222
OTHER          6        26       358      0.1875   0.0165   0.061
PART           0        0        17       1.0      0.0      0.0
PREP           10       7        195      0.5882   0.0488   0.1832
PRON           1        1        49       0.5      0.02     0.0862
PUNCT          27       100      107      0.2126   0.2015   0.2103
SPELL          84       48       17       0.6364   0.8317   0.6677
VERB           2        3        141      0.4      0.014    0.0613
VERB:FORM      17       6        66       0.7391   0.2048   0.4857
VERB:INFL      1        1        1        0.5      0.5      0.5
VERB:SVA       8        6        82       0.5714   0.0889   0.274
VERB:TENSE     2        2        163      0.5      0.0121   0.0552
WO             0        0        11       1.0      0.0      0.0

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
242     442     1958    0.3538  0.11    0.2451
==============================================
```

Level-3 fine-grained

```py
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
M:ADV          0        0        5        1.0      0.0      0.0
M:CONJ         0        0        4        1.0      0.0      0.0
M:CONTR        0        1        0        0.0      1.0      0.0
M:DET          5        0        110      1.0      0.0435   0.1852
M:NOUN         0        0        15       1.0      0.0      0.0
M:NOUN:POSS    1        1        5        0.5      0.1667   0.3571
M:OTHER        0        3        16       0.0      0.0      0.0
M:PART         0        0        3        1.0      0.0      0.0
M:PREP         2        1        47       0.6667   0.0408   0.1639
M:PRON         0        0        9        1.0      0.0      0.0
M:PUNCT        27       55       61       0.3293   0.3068   0.3245
M:VERB         1        1        21       0.5      0.0455   0.1667
M:VERB:FORM    0        0        6        1.0      0.0      0.0
M:VERB:TENSE   1        2        22       0.3333   0.0435   0.1429
R:ADJ          2        3        14       0.4      0.125    0.2778
R:ADJ:FORM     2        0        5        1.0      0.2857   0.6667
R:ADV          0        0        8        1.0      0.0      0.0
R:CONJ         0        0        3        1.0      0.0      0.0
R:CONTR        0        0        1        1.0      0.0      0.0
R:DET          4        0        57       1.0      0.0656   0.2597
R:MORPH        7        21       74       0.25     0.0864   0.1813
R:NOUN         1        7        65       0.125    0.0152   0.051
R:NOUN:INFL    5        0        3        1.0      0.625    0.8929
R:NOUN:NUM     4        5        155      0.4444   0.0252   0.1026
R:NOUN:POSS    0        2        8        0.0      0.0      0.0
R:ORTH         46       197      18       0.1893   0.7188   0.222
R:OTHER        4        12       298      0.25     0.0132   0.0546
R:PART         0        0        9        1.0      0.0      0.0
R:PREP         1        4        104      0.2      0.0095   0.04
R:PRON         1        0        31       1.0      0.0312   0.1389
R:PUNCT        0        14       40       0.0      0.0      0.0
R:SPELL        84       48       17       0.6364   0.8317   0.6677
R:VERB         1        1        97       0.5      0.0102   0.0472
R:VERB:FORM    17       6        56       0.7391   0.2329   0.5152
R:VERB:INFL    1        1        1        0.5      0.5      0.5
R:VERB:SVA     8        6        82       0.5714   0.0889   0.274
R:VERB:TENSE   1        0        119      1.0      0.0083   0.0403
R:WO           0        0        11       1.0      0.0      0.0
U:ADJ          1        0        8        1.0      0.1111   0.3846
U:ADV          1        1        18       0.5      0.0526   0.1852
U:CONJ         0        0        3        1.0      0.0      0.0
U:DET          5        3        159      0.625    0.0305   0.1276
U:NOUN         0        1        10       0.0      0.0      0.0
U:NOUN:POSS    0        0        3        1.0      0.0      0.0
U:OTHER        2        11       44       0.1538   0.0435   0.102
U:PART         0        0        5        1.0      0.0      0.0
U:PREP         7        2        44       0.7778   0.1373   0.4023
U:PRON         0        1        9        0.0      0.0      0.0
U:PUNCT        0        31       6        0.0      0.0      0.0
U:VERB         0        1        23       0.0      0.0      0.0
U:VERB:FORM    0        0        4        1.0      0.0      0.0
U:VERB:TENSE   0        0        22       1.0      0.0      0.0

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
242     442     1958    0.3538  0.11    0.2451
==============================================
```