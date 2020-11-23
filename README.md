# ThamizhiPOSt - a neural based POS tagger for Tamil
### Website - http://nlp-tools.uom.lk/thamizhi-pos/

ThamizhiPOSt is a deep learning based POS tagger which is developed using Stanza framework, and trained using 11K POS tagged sentences along with fasttext model of Facebook. ThamizhiPOSt uses the Universal Dependency POS tagset for the annotation. More details information about taggest can be found here (https://universaldependencies.org/u/pos/) . 

ThamizhiPOSt shows an accuracy of 95.20 (as of today 02.09.2020) for the TTB (https://github.com/UniversalDependencies/UD_Tamil-TTB/blob/master/ta_ttb-ud-test.conllu). This is the current state of the art for the Tamil POS taggers which are implemented/reported as of today.

We trained this POS tagger using the AMRITA POS tagged data. Before we do this, we did a harmonisation of BIS, AMRITA and UPOS tagsets, which are the primary POS tagsets available as of today. 
The harmonisation [Universal Dependency POS (UPOS)] (https://universaldependencies.org/u/pos/) , [BIS] (http://nlp-tools.uom.lk/thamizhi-pos/documents/BIS-Standard.df) , and AMRITA (https://www.amrita.edu/publication/tamil-pos-tagging-using-linear-programming) can be be found in [this sheet] (https://docs.google.com/spreadsheets/u/1/d/1J7UbY1D_gOIL6EXMxrszMsBhuX-Ad6Mm3qt1xE5qdpY/edit?usp=drive_web&ouid=107409815654517250986). 

However, we found that the Amrita POS tagged data are more clean, therefore, we used it to train the POS tagger. We used Stanza, a neural based framework developed by Stanford University - a sccuessor of their CoreNLP framework, to train the POS tagger.

The trained models can be found here: http://nlp-tools.uom.lk/thamizhi-pos/models/models This file is in tgz format, you can extracted it using tar.

## How to used this POS tagger

