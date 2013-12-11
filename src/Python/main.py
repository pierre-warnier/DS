#!/usr/bin/env python
"""
Where it all happens.
"""
import config
import file_io
import language

import sys
import glob
import pickle

def load(to_open):
    try:
        with open(to_open, 'rb') as fd:
            file_list = pickle.load(fd)
            language.LEMMA = file_io.read_lemma(pickle.load(fd), file_list)
            my_dict = pickle.load(fd)
    except:
        print >> sys.stderr, 'Could not load %s. Starting from scratch!' % to_open
        file_list = set()
        language.LEMMA = file_io.read_lemma()
        my_dict = dict()
    return file_list, my_dict

def save(to_open, file_list, my_dict):
    print >> sys.stderr, 'Saving results in %s' % to_open
    with open(to_open, 'wb') as fd:
        pickle.dump(file_list, fd)
        pickle.dump(language.LEMMA, fd)
        pickle.dump(my_dict, fd)


def run():
    """Pre-processing"""
########################################################################################
    wd_total = '%s/total' % config.WORK_DIR
    file_io.mk_path('%s/dumps' % wd_total)
    file_io.mk_path('%s/pickles' % wd_total)
    to_open = "%s/pickles/%s.pkl" % (wd_total, config.CONF)

    file_list, my_dict = load(to_open)
    import reader
    import dict_utils
    import matrix
    cpt = 1
    for f in glob.glob(config.RELP_FILES):
        if f in file_list:
            print >> sys.stderr, 'READER (%d): File already read: %s' % (cpt, f) 
            continue
        print >> sys.stderr, 'READER (%d): Starting file: %s' % (cpt, f) 
        cpt += 1
        my_dict = reader.reader(f, my_dict)
        file_list.add(f)
        if len(file_list) % config.SAVE_FREQ == 0:
            wd = "%s/%d/" % (config.WORK_DIR, len(file_list))
            file_io.mk_path('%s/dumps' %wd)
            file_io.mk_path('%s/pickles' %wd)

            save("%s/pickles/%s.pkl" % (wd, config.CONF), file_list, my_dict)
            # Filter lines
            dd = my_dict.copy()
            if config.WORD1:
                dict_utils.filter_words(dd, config.WORD1, (2,3))
            dd = dict_utils.popular(dd, config.POPULAR)
            m_rows, m_columns, my_matrix = dict_utils.dict_to_matrix(dd)
            my_matrix = matrix.Matrix(rows=m_rows, columns=m_columns, count=my_matrix)
            my_matrix.save('%s/dumps/%s_%s' % (wd, config.OUTPUT_FILE, config.CONF))
    save(to_open, file_list, my_dict)
    # Filter lines
    if config.WORD1:
        dict_utils.filter_words(my_dict, config.WORD1, (2,3))
    my_dict = dict_utils.popular(my_dict, config.POPULAR)
    m_rows, m_columns, my_matrix = dict_utils.dict_to_matrix(my_dict)
    my_matrix = matrix.Matrix(rows=m_rows, columns=m_columns, count=my_matrix)
    my_matrix.save('%s/dumps/%s_%s' % (wd_total, config.OUTPUT_FILE, config.CONF))


if __name__ == "__main__":
    run()
