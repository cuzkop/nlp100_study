# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

# https://docs.oracle.com/cd/E16338_01/text.112/b61357/astopsup.htm
# oracleの英語のデフォルトストップリストより

stop_words = ("a	did	in	only	then	where	"
"all	do	into	onto	there	whether	"
"almost	does	is	therefore	which	"
"also	either	it	our	these	while	"
"although	for	its	ours	they	who	"
"an	from	just	s	this	whose	"
"had	ll	shall	those	why	"
"any	has	me	she	though	will	"
"are	have	might	should	through	with	"
"as	having	Mr	since	thus	would	"
"at	he	Mrs	so	to	yet	"
"be	her	Ms	some	too	you	"
"because	here	my	still	until	your	"
"been	hers	no	such	ve	yours	"
"both	him	non	t	very	"
"but	his	nor	than	was	"
"by	how	not	that	we	"
"could	i	on	their	what	"
"d	if	one	them	when").lower().split("\t")

def is_stopword(word: str) -> bool:
    return word.lower() in stop_words

assert is_stopword("a")
assert not is_stopword("b")
