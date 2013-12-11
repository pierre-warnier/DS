"""
All dictionary related operations.
"""

import collections
import itertools

import scipy as sp
import scipy.sparse as spsp

def fusion(dict1, dict2):
    """dict1,dict2: dict"""
    for key2, value2 in dict2.items():
        if key2 in dict1:
            if type(dict1[key2]) == type(value2) == type(0):
                dict1[key2] += value2
            elif isinstance(dict1[key2], collections.Set) and isinstance(value2, collections.Set):
                dict1[key2] = dict1[key2].union(value2)
            elif isinstance(dict1[key2], collections.Mapping):
                dict1[key2] = fusion(dict1[key2], value2)
            else:
                print 'Error'
                break
        else:
            dict1[key2] = value2
    return dict1

def popular(dict1, int1):
    """head, tail or cat"""
    if int1 == 0:
        return dict1
    reverse = True if int1 > 0 else False
    list1 = sorted(((sum(value1.itervalues()), key1) for key1, value1 
                                                 in dict1.iteritems()), 
                                                 reverse=reverse)
    return dict((key1, dict1[key1]) for value1, key1 in list1[:int1])

def filter_words(d, words, index):
    s = set(tuple(line.strip().split('\t')) for line in open(words))
    for k in d.keys():
        l = list()
        for i in index:
            l.append(k[i])
        if tuple(l) not in s:
            d.pop(k)

def reverse_dict(dict1):
    """k:v => v:set(k1, key2...)"""
    result = dict()
    for key1, value1 in dict1.iteritems():
        result.setdefault(value1[1], set()).add((value1[0], key1))
    return result

def ddict(iter1):
    """ k: string, v:tuple(string, int) => k:{v[0]:v[1],...}"""
    result = dict()
    for key1, value1 in iter1:
        result.setdefault(key1, dict()).update({value1[0]:value1[1]})
    return result

def redundant_dict(iter1):
    """ k,v => k:(v1,value2...)"""
    result = dict()
    for key1, value1 in iter1:
        result.setdefault(key1, set()).add(value1)
    return result

#def dict_to_matrix(d):
#    rows = sorted(set(k for k,v in d))
#    cols = sorted(set(v for k,v in d))
#    i_rows = dict(itertools.izip(rows, range(len(rows))))
#    i_cols = dict(itertools.izip(cols, range(len(cols))))
#    ri = sp.array([i_rows[k] for k,v in d], dtype=sp.int32) 
#    ci = sp.array([i_cols[v] for k,v in d], dtype=sp.int32) 
#    dv = sp.array([d[(k,v)]  for k,v in d], dtype=sp.int32)
#    return rows, cols, spsp.coo_matrix((dv, (ri, ci)), shape=(len(rows), len(cols)), dtype=sp.float16)

def dict_to_matrix(d):
    rows = sorted(' - '.join(k) for k in d.keys())
    cols = set()
    for v in d.itervalues():
        cols.update(set(v.iterkeys()))
    cols = sorted(' - '.join(c) for c in cols)
    i_rows = dict(itertools.izip(rows, range(len(rows))))
    i_cols = dict(itertools.izip(cols, range(len(cols))))
    m = spsp.dok_matrix((len(rows), len(cols)), dtype=sp.float64)
    for k,v in d.iteritems():
        for kk,vv in v.iteritems():
            m[i_rows[' - '.join(k)], i_cols[' - '.join(kk)]] += vv
    return rows, cols, m

if __name__ == '__main__':
    pass
