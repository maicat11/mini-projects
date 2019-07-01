---
duration: 60
date: w6d1
tags:
maintainer: artificialsoph
title: Conway's Game of Life
---

### Pair Problem

Can you build a game of life in Python: http://www.bitstorm.org/gameoflife/

Feel free to hardcode the boardsize, speed and starting configuration into your program. And you can make the board out of anything: ones and zeros or pluses and dots. I just want to see the evolution of the board.

To update the board, this function is handy:

    from IPython import display
    display.clear_output(wait=True)
