'''Example script.'''

import argparse

import authorship


def main():
    '''Example usage.'''
    # Build the command line interface
    parser = argparse.ArgumentParser(
        description='Determine authorship using a multinomial naive Bayes classifier.')
    parser.add_argument("classifications",
        help="Directory containing author writing samples.",
        type=str,
        )
    parser.add_argument("documents",
        help="Directory containing documents you wish to classify.",
        type=str,
        )
    args = parser.parse_args()

    example = authorship.Unigram(stopwords='example/stopwords')
    classifications = example.get_values(args.classifications)
    documents = example.get_values(args.documents)
    likelihoods = example.compare_values(classifications, documents)
    example.get_classifications(likelihoods, verbose=True)


if __name__ == '__main__':
    main()
