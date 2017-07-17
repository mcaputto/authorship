# authorship

![](http://imgur.com/HZXlFqf.jpg)

Classify text files using a multinomial naive Bayes probabilistic model.

## Features

* Easy installation
* No third party dependencies
* Reusable data objects
* Sensible default parameters
* Optional stopwords
* Verbose mode

## Basic usage

Import the module:

```py
>>> import authorship
```

Instantiate the class:

```py
>>> example = authorship.Unigram(stopwords='example/stopwords')
```

Learn classifications from a sample of documents:

```py
>>> classifications = example.get_values('example/foo/classifications')
```

Analyze the documents you want to classify:

```py
>>> documents = example.get_values('example/foo/documents')
```

Compare the analyzed documents to the learned samples:

```py
>>> likelihoods = example.compare_values(classifications, documents)
```

Print the predictions:

```py
>>> example.get_classifications(likelihoods, verbose=True)
Moby Dick: Herman Melville
The Trial: Franz Kafka
```
