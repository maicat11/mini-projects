---
duration: 60
date: w5d1
tags:
maintainer: artificialsoph
title: Nearest Wookiee Neighbors
---

# Pair Problem: Wookiee neighbors

Your rebel alliance team has been stranded on a remote planet in the Outer Rim. The memory banks of your ship have been wiped. You are the only surviving data scientist on the team.

Your location is near several planets that are largely inhabited by wookiees. Unfortunately, the different tribes of wookiees have different attitudes toward the alliance. It's important that your team know which tribe (represented by the color of the wookiee) will be on a planet or ship before exiting warp nearby. If you end up near a hostile wookiee tribe, you may not have time to reactive your warp drive before things turn sour.

The problem is that your databank is fried. Out of millions of ships and planets, you only know the location and color of a few hundred wookiee tribes.

Your team turns to you, the only one on the team that is capable of harnessing the power of The Force (data science). However, all of your tools were destroyed in the memory bank failure: no neural networks, no support vector machines, no models of any kind.

# Details

You must code, from scratch, a working KNN algorithm. Use the train-test split below to evaluate your model and then generate predictions for each of the observed wookiee ships in the holdout set.

- [train data](http://soph.info/metis/nyc18_ds15/wookiee-train.csv)
- [test data](http://soph.info/metis/nyc18_ds15/wookiee-test.csv)
- [holdout data](http://soph.info/metis/nyc18_ds15/wookiee-ho.csv)


# Possible extensions:

 * Does your solution work for any number of features in the training data sets?
 * Does your solution handle ties?
 * Can you add another parameter, `k`, to your solution so that it uses the `k` nearest Wookiees instead of only the nearest Wookiee?
 * Can you add to your solution so that it has reasonable behavior if `y_train` is numeric?

An extension of another kind:

 * Are you confident that your solution is correct? How can you ensure that it is, and check that it stays correct in the future?
