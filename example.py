'''Example script.'''

import authorship


def main():
    '''Example usage.'''
    example = authorship.Unigram(stopwords='example/stopwords')
    classifications = example.get_values('example/foo/classifications')
    documents = example.get_values('example/foo/documents')
    likelihoods = example.compare_values(classifications, documents)
    example.get_classifications(likelihoods, verbose=True)


if __name__ == '__main__':
    main()
