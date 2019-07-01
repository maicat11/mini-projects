---
duration: 60
date: w4d1
tags:
maintainer: artificialsoph
title: Parentheses
---

#### Pair Problem

*A version of this problem was faced at a whiteboard by a Metis student in an interview for a data scientist position on April 16, 2015.*

In programming languages, and especially in Lisps, there can be a lot of parentheses. The parentheses have to be "balanced" to be valid. For example, `()(())` is balanced, but `()())` is not balanced. Also, `)((())` is not balanced.

Write a function that takes a string and returns `True` if the string's parentheses are balanced, `False` if they are not.

**This is fairly easy. Once you are finished, see if you can come up with a second way to solve the problem.**

Here are examples to test your function with:

 * `(()()()())` should return `True`
 * `(((())))` should return `True`
 * `(()((())()))` should return `True`
 * `((((((())` should return `False`
 * `()))` should return `False`
 * `(()()))(()` should return `False`
