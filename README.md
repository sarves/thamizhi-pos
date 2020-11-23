# ThamizhiPOSt - a neural based POS tagger for Tamil
### Website - http://nlp-tools.uom.lk/thamizhi-pos/

ThamizhiPOSt is a deep learning based POS tagger which is developed using Stanza framework, and trained using 11K POS tagged sentences along with fasttext model of Facebook. ThamizhiPOSt uses the Universal Dependency [POS tagset](https://universaldependencies.org/u/pos/) for the annotation. 

ThamizhiPOSt shows an accuracy of 95.20 (as of today 02.09.2020) for the TTB (https://github.com/UniversalDependencies/UD_Tamil-TTB/blob/master/ta_ttb-ud-test.conllu). This is the current state of the art for the Tamil POS taggers which are implemented/reported as of today.

We trained this POS tagger using the AMRITA POS tagged data. Before we do this, we did a harmonisation of BIS, AMRITA and UPOS tagsets, which are the primary POS tagsets available as of today. 
The harmonisation [Universal Dependency POS (UPOS)](https://universaldependencies.org/u/pos/) , [BIS](http://nlp-tools.uom.lk/thamizhi-pos/documents/BIS-Standard.df) , and [AMRITA](https://www.amrita.edu/publication/tamil-pos-tagging-using-linear-programming) can be be found in [this sheet](https://docs.google.com/spreadsheets/u/1/d/1J7UbY1D_gOIL6EXMxrszMsBhuX-Ad6Mm3qt1xE5qdpY/edit?usp=drive_web&ouid=107409815654517250986). 

However, we found that the Amrita POS tagged data are more clean, therefore, we used it to train the POS tagger. We used Stanza, a neural based framework developed by Stanford University - a sccuessor of their CoreNLP framework, to train the POS tagger.

The trained models can be [found here](http://nlp-tools.uom.lk/thamizhi-pos/models/models) in a compressed format. This file is in tgz format, you can extract it using tar.

### How to use ThamizhiPOSt

1. Download and install *Stanza*, as outlined here: https://stanfordnlp.github.io/stanza/installation_usage.html
2. Donwload [trained models](http://nlp-tools.uom.lk/thamizhi-pos/models/models), and place them in a folder called *models*
3. Insert your data to be POS tagged in a file called *sentence.txt*, and place it in the same level as the models folder
4. Download and place *print_upos.py*, along with *sentence.txt*
5. Execute the python script -  print_upos.py, output will be written to a file called *pos-tagged-sentence.txt*

Note: In this version of tagger, it is compulsory to include a symbol (can be a period/exclamation mark / question mark) at the end of each line/sentence. Otherwise, the very last token will be considered as a punctuation. 

An output will look like the following for the data "தமிழ் எங்கள் உயிருக்கு நேர் ."
```
1	தமிழ்	PROPN
2	எங்கள்	PRON
3	உயிருக்கு	NOUN
4	நேர்	NOUN
5	.	PUNCT
```

### Tagged data

The following datasets are tagged using ThamizhiPOSt, available for research :
- [Official data](https://github.com/sarves/thamizhi-pos/tree/main/tagged-data) (consists of Annual reports, Audit reports, Letters - anonymised) - 8,932 tokens/1,100 sentences
- [Sri Lankan Tamil news data](https://github.com/sarves/thamizhi-pos/tree/main/tagged-data) - 124,203 tokens / 10,000 sentences

### Acknowledgment
This research was supported by the Accelerating Higher Education Expansion and Development (AHEAD) Operation of the Ministry of Higher Education, Sri Lanka funded by the World Bank.
