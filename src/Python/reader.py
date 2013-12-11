import re

import config
import language

surface = dict()

_relp_rel = re.compile('^([^:]+):(.+)-(.+) \((.+,.+)\) \(\d+,\d+\)')
_relp_rel2 = re.compile('\((.+)\),\((.+)\)|(.+),\((.+)\)|\((.+)\),(.+)|(.+),(.+)')
def _relp(fd):
    """Relp reader."""
    for line in fd:
        try:
            line = line.strip()
            match = _relp_rel.match(line)
            if match:
                relation, nature1, nature2, couple = match.groups()
                word1, word2 = tuple(i for i in _relp_rel2.match(couple).groups() if i)[:2]
                relation, nature1, nature2 = relation.upper(), nature1.upper(), nature2.upper()
                nature1, relation, nature2 = config.EQUIVALENCES_RELATIONS.get((nature1, relation, nature2), (nature1, relation, nature2))

                mem1, mem2 = word1, word2
                for f in (eval('language.' + m) for m in config.MODIFIERS):
                    word1 = f(word1)
                    word2 = f(word2)

                surface.setdefault((word1, nature1), set()).add(mem1)
                surface.setdefault((word2, nature2), set()).add(mem2)

                if word1 and word2 and config.PREDICATES and (nature1, relation, nature2) in config.COMBINATIONS and word2 not in language.STOP_WORDS:
                    yield ('PREDICATE', relation, word1, nature1), (word2, nature2)
                if word1 and word2 and config.ARGUMENTS and (nature2, relation, nature1) in config.COMBINATIONS and word1 not in language.STOP_WORDS:
                    yield ('ARGUMENT', relation, word2, nature2), (word1, nature1)


                #    cache.setdefault(nature1, set()).add(word1)
                #    cache.setdefault(nature2, set()).add(word2)
        except:
            pass

def reader(f, my_dict, method=_relp):
    """Generic reader."""
    for k,v in method(open(f)):
        tmp = my_dict.setdefault(k, dict())
        tmp[v] = tmp.get(v, 0) + 1
    return my_dict
