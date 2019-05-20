export ALSADEV="plughw:1,0"

GRAM=meirei
mv $GRAM.dfa $GRAM.dfa.1
mv $GRAM.term $GRAM.term.1
mv $GRAM.dict $GRAM.dict.1
mkdfa.pl $GRAM

DICT=~/src/julius/julius-dict/am-gmm.jconf
julius -C $DICT -gram $GRAM -nostrip -module
