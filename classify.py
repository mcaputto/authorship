'''Multinomial naive Bayes text classifier.'''

from collections import Counter
from math import log

import util


STOPCHARS = 'P'
EXTENSION = '*.txt'


class Unigram:

    '''Unigram prediction model.'''

    def __init__(self, stopwords, stopchars=STOPCHARS):
        '''
        Initializer method.

        Parameters
        ----------
        stopchars : str
            Categories of Unicode characters to be ignored.
        stopwords : str
            File containing words (separated by whitespace) to be ignored.
        '''
        self.stopchars = util._remove_unicode(stopchars)
        self.stopwords = util._get_words(stopwords)

    def get_values(self, path, extension=EXTENSION, verbose=False):
        '''
        Return dictionary with word frequencies.

        Parameters
        ----------
        path : str
            Directory containing documents.
        extension : str
            File extension for documents. Only these files will be processed.

        Returns
        -------
        value : dict
            Feature values for each document or classification in a directory.
        '''
        D = util._yield_name(path, extension)
        value = {}
        for d in D:
            if verbose:
                print(f'{util._name(d)}')
            text = util._get_features(d, self.stopchars)
            value[d] = Counter(text)
            [value[d].__delitem__(w) for w in self.stopwords]
            if verbose:
                print(f'\t{len(value[d])} features')
            util._percent(value[d])
        return value

    @staticmethod
    def compare_values(C, D, verbose=False):
        '''
        Multiply document and classification feature values.

        Parameters
        ----------
        C : dict
            Feature values for classification samples, obtained from
            Unigram.value().
        D : dict
            Feature values for testing documents obtained from
            Unigram.value().

        Returns
        -------
        compare : dict
            Conditional probabilities for feature values for each document.
        '''
        compare = {}
        for d in D:
            if verbose:
                print(f'{util._name(d)}')
            compare[d] = {}
            for c in C:
                compare[d][c] = {}
                for w in D[d]:
                    # Since probabilities are small, we operate in log space.
                    # We add 1 to prevent computing log(0), which is undefined.
                    compare[d][c][w] = log(D[d][w] + 1) + log(C[c][w] + 1)
                compare[d][c] = sum(compare[d][c].values())
                if verbose:
                    print(f'\t{util._name(c)} ({compare[d][c]})')
        if verbose:
            print('\n')
        return compare

    @staticmethod
    def get_classifications(compare, verbose=False):
        '''
        Return dictionary with predicted classifications.

        Parameters
        ----------
        compare : dict
            Classification likelihoods obtained from Unigram.compare().

        Returns
        -------
        prediction : dict
            Predicted classification for each document.
        '''
        prediction = {}
        for d in compare:
            prediction[d] = util._max(compare[d])
            if verbose:
                print(f'{util._name(d)}: {util._name(prediction[d])}')
        return prediction
