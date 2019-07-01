import numpy as np

docs = [[0.98, 0.01, 0.01], [0.01, 0.98, 0.01], [0.01, 0.01, 0.98]]
topics = [[0.4, 0.4, 0.01, 0.01, 0.01, 0.01, 0.1, 0.04, 0.01, 0.01],
          [0.01, 0.01, 0.4, 0.4, 0.01, 0.01, 0.1, 0.04, 0.01, 0.01],
          [0.02, 0.02, 0.01, 0.01, 0.4, 0.4, 0.02, 0.1, 0.01, 0.01]]
words = [
    'cat', 'kitten', 'dog', 'puppy', 'deep', 'learning', 'fur', 'image', 'GPU',
    'asparagus'
]


def make_doc(topic_probs=None, n_words=40, verbose=True):
    if topic_probs is None:
        topic_probs = np.random.dirichlet(np.ones(len(topics)))
    if verbose:
        print 'topic_probs:', topic_probs
    results = []
    for _ in range(n_words):
        i_topic = np.random.choice(len(topics), p=topic_probs)
        topic = topics[i_topic]
        word = np.random.choice(words, p=topic)
        results.append(word)
    return ' '.join(results)


for doc in docs:
    print make_doc(topic_probs=doc, n_words=10, verbose=False)
"""
# Example output:
cat learning kitten image kitten cat deep image cat kitten
puppy puppy learning dog puppy dog dog puppy image dog
deep learning deep image deep deep deep deep learning learning
"""
