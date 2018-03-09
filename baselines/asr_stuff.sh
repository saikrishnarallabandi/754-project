
# Build an LM
ngram-count -order 3 -text cheating.txt  -lm data/local/lm.arpa

# Update the lexicon
cat cheating.txt | tr ' ' '\n' > words.txt
cat words.txt | while read line; do pron=`flite -ps -t $line none`; echo $line $pron; done > t
cat t | sed 's/pau/ /' | sed 's/ pau//' | sort | uniq > data/local/dict/lexicon.txt
echo -e "<UNK> SPN" >> data/local/dict/lexicon.txt
rm -r data/local/dict/lexiconp.txt

# Non silence  phones
grep -v -w SIL data/local/dict/lexicon.txt | awk '{for(n=2;n<=NF;n++) { p[$n]=1; }} END{for(x in p) {print x}}'  | sort > data/local/dict/nonsilence_phones.txt

# Update  lang
./utils/prepare_lang.sh data/local/dict '<UNK>' data/local/lang data/lang

# FST
test=data/lang_test
mkdir -p $test
for f in phones.txt words.txt phones.txt L.fst L_disambig.fst phones; do     cp -r data/lang/$f $test; done

# Make G.fst
cat data/local/lm.arpa | arpa2fst --disambig-symbol=#0 --read-symbol-table=data/lang_test/words.txt - data/lang_test/G.fst
fstisstochastic data/lang_test/G.fst 

# Rebuild graph
./utils/mkgraph.sh data/lang_test/ ~/Downloads/tri2a_librispeech/ ~/Downloads/tri2a_librispeech/graph_tgsmall/

# Copy stuff
cp graph_tgsmall/HCLG.fst final.mdl graph_tgsmall/phones.txt graph_tgsmall/words.txt tree /home/saikrishnalticmu/tools/kaldi/egs/voxforge/online_demo/online-data/models/tri2a_cities


