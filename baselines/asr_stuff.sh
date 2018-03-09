
# Build an LM
ngram-count -order 4 -text cheating.txt  -lm data/local/lm.arpa

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
