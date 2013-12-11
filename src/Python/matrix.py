import os
import glob

import scipy as sp
import scipy.io as spio


class Matrix(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def save(self, name):
        for k,v in self.__dict__.items():
            if sp.sparse.issparse(v):
                spio.mmwrite('%s.%s' %(name, k), v, 'integer')
                os.rename('%s.%s.mtx' %(name, k), '%s.%s' %(name, k))

            else:
                open('%s.%s' %(name, k), 'wb').writelines('\n'.join(v) + '\n')

    def load(self, name):
        for p in glob.glob(name):
            try:
                self.__dict__[p.split('.')[-1]] = spio.mmread(p)
            except ValueError:
                self.__dict__[p.split('.')[-1]] = tuple(l.strip() for l in open(p))


if __name__ == '__main__':
    pass
