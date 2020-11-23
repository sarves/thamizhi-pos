import stanza
import sys

#State the data file here
f1=open("./sentence.txt","r")
       
config = {
  'processors': 'tokenize,pos', # Comma-separated list of processors to use
  'lang': 'ta', # Language code for the language to build the Pipeline in
  'tokenize_model_path': './models/ta_ttb_tokenizer.pt', 
  'pos_model_path': './models/ta_thamizhi_pos.pt',
  'pos_pretrain_path': './models/ta_pretrain.pt',
}
nlp = stanza.Pipeline(**config)

#State the pos tagged
pos_tagged=open("./pos-tagged-sentence.txt","w")
x=f1.read()

doc = nlp(x)
for sent in doc.sentences :
  counter=1
  for word in sent.words :
          #You can customise the way in which output needs to be printed
          pos_tagged.write(str(counter) + "\t" + word.text + "\t" + word.upos+ "\n")
          counter=counter+1
pos_tagged.close()
f1.close()
