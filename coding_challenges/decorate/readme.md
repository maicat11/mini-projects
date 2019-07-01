---
duration: 60
date: w5d5
tags:
maintainer: artificialsoph
title:
---

#### Pair Problem

This function is boring:

```python
def square(x):
    return x * x

square(5)
## 25
```

Write a [_decorator_](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/) called `talky` so that when you run this:

```python
@talky
def square(x):
    return x * x

answer = square(5)
```

You get the following output:

```
Oh hi!
The result sure is 25!
```

---

Extension: Write a decorator `talky_with`, so that when you run this:

```python
@talky_with("Aaron")
def square(x):
    return x * x

answer = square(5)
```

You get the following output:

```
Oh hi! I'm Aaron.
The result sure is 25!
```
