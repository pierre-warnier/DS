INPUT='/Users/snape/Documents/bazaar/DS/data/wd/total/dumps/wikipedia_PREDICATES : V - OBJ - N and N - COMP_OF - N and V_PASS - SUBJ - N.count'
OUTPUT='/Users/snape/Documents/bazaar/DS/data/wd/total/dumps/wikipedia_PREDICATES : V - OBJ - N and N - COMP_OF - N and V_PASS - SUBJ - N.sim'

all:
	sed "s#XXX#$(INPUT)#g; s#YYY#$(OUTPUT)#g" main.tpl > main.m 
	#matlab -nojvm -nodisplay < main.m
	mkdir -p logs && mv main.m logs/main.m.`date "+%Y-%m-%d@%H:%M:%S"`
