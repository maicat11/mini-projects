---
duration: 60
date: w7d2
tags:
maintainer: artificialsoph
title:
---

#### Pair Problem #1

You are given the following three documents:

```python
text = ["wookie stormtrooper",
        "wookie wookie wookie stormtrooper stormtrooper stormtrooper",
        "harry potter"]
```

 * Transform this data into a bag of words representation, with simple counts. How informative is this format? How much information do you have about individual words?
 * Calculate Euclidean and cosine distances between each pair of documents. How do these distances relate to your intuition for the documents' similarities?
 * Calculate one minus the cosine distance between each pair of de-meaned documents, and the Pearson correlation coefficient between each pair of documents. How are they related? Is this a coincidence? Find a counterexample or prove that there isn't one.



#### Pair Problem #2

Imagine a data matrix with three rows and two columns. Each row represents an observation, and each column represents a feature. (This is our usual convention.)

Imagine subtracting out the column means.

Imagine multiplying the transpose of this matrix by itself.

Don't just imagine it—write this out!

What familiar calculation is this? What result have you produced?
