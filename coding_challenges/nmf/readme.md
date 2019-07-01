---
duration: 60
date: w7d5
tags:
maintainer: artificialsoph
title:
---

#### Clustering and Topic Modeling using NMF

0) Get the pre-processed [BBC dataset here](http://mlg.ucd.ie/files/datasets/bbc.zip)
1) There are articles collected from 5 different topics, and the data pre-processed
2) Use the data to build a sparse matrix (or regular matrix)
3) run NMF to first do clustering on the articles
4) use NMF to attempt Topic Modeling

More details on each step:

0) *bbc.terms* is just a list of words and *bbc.docs* is a list of artcles listed by topic. And *bbc.mtx* is a list: first column is **wordID**, second is **articleID** and the third is the number of times that word appeared in that article.

1) To read a file into a list (each line will be a string in that list), you can do this:

        with open(filename) as f:
            content = f.readlines()

2) To build a matrix, all you need is the bbc.mtx file. Look up coo style sparse matrix. Or just build a regular matrix
( I would use a pivot table)

3) Once you have the matrix, it's just a matter of calling NMF with the number of components equals five (we luckily know that there are 5 types of articles in our dataset). NMF will return a N x 5 matrix. For each articles it says how much of each of the 5 topics it belongs to. Take the max and assign each articles to the cooresponding cluster. Since we have the topics for each of the article (in the bbc.docs file), we can compare and see how well our clustering performed.

4) NMF.components_ is a 5 x M matrix. Each feature (topic) has a long vector of words associated with it. Find the top 5 to 10 words for each topic and print them out and see if we can come up with topics based on the set of words.
