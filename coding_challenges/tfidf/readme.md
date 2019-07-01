---
duration: 60
date: w9d4
tags:
maintainer: artificialsoph
title: Spark TFIDF
---

# Let's give Spark a shot!

Your challenge is to calculate TFIDF on the text file in the repo, using Spark.  In that
text file, each line is a document.  You should have 4 total documents.  Don't be
too concerned about getting the formula right; just start by calculating the number
of times each word appears for each document and dividing by the
total amount of times the word appears in the whole corpus.  If you can get to that point,
then try to get the calculation correct according to one of the true formulas for TFIDF.

For this simple TFIDF measure, you should get the following for the word "of":

```
document 0: document count: 0.  Corpus count: 24.  Simple TFIDF: 0/24 = 0
document 1: document count: 6.  Corpus count: 24.  Simple TFIDF: 6/24 = 0.25
document 2: document count: 14. Corpus count: 24.  Simple TFIDF: 14/24 = 0.58333...
document 3: document count: 4.  Corpus count: 24.  Simple TFIDF: 4/24 = 0.166....
```

>Hint: `zipWithIndex()` called on an RDD will zip the elements of an RDD together with an index.
