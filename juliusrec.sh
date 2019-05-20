export ALSADEV="plughw:1,0"

DICT=~/src/julius/julius-dict/main.jconf
GRAM=~/src/julius/julius-dict/am-gmm.jconf
julius -C $DICT -C $GRAM -nostrip

