---
duration: 60
date: w5d4
tags:
maintainer: artificialsoph
title: Scrabble + Javascript
---

# Instructor Notes

This pair should be placed the day after the javascript lesson

# Pair problem: Scrabble and Flask

In the game Scrabble, you try to construct words using tiles. Different letters are worth different amounts; for example a common letter like 'E' is worth 1 point, while a rare letter like 'Q' is worth 10 points. We want to make a flask app that will take the URL `http://127.0.0.1:5000/hand/<letters>` and tell us the sum of all the points in `<letters>`. For example:

* `http://127.0.0.1:5000/hand/EEEEE` would take us to a page that tells us `EEEEE` is worth 5 points (each `E` is worth 1 point).
* `http://127.0.0.1:5000/hand/QQEE` would take us to a page that tells us `QQEE` is worth 22 points (each `E` is worth 1 point, and each `Q` is worth 10 points).

We have included the basic structure for your project in the directory `pair_project_files`. In the starter file `scrabble.py`, we have included a dictionary that maps letters to points:
```python
point_values = {
  'A': 1,
  'B': 3,
  ...
  'E': 1,
  ...
  'Q': 10,
  ...
  'Z': 10
}
```

You have a lot of freedom in how you style the page.

### Bonus:

If you have time, see if you can implement a "Scrabble API" (i.e. something we can make POST requests to). Call the route `http://127.0.0.1:5000/api/hand`. You want it to respond with a score. To check if it is working, you can call `curl` from the command line:

```bash
curl -H "Content-Type: application/json" --request POST -d '{"letters": "EEEEE"}' http://127.0.0.1:5000/api/hand
```
and you should get the response
```bash
{
  "score": 5
}
```
