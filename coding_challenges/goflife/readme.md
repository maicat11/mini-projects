---
duration: 60
date: w6d5
tags:
maintainer: artificialsoph
title: Big Game of Life
---

### Game of life

Let's tie it all together.

1) Move your pair.html from yesterday to this folder and add these code pieces to it. The first goes at the beginning of your "body" block. And the second goes to the end of the "script" block. Alternately, you can use this file: [pair.html](pair.html)

```javascript
      <div>
        <button type="button" onClick="getnextframe()">Evolve!</button>
      </div>
```

```javascript
       function getnextframe(){
         $.ajax({
           type: "POST",
           contentType: "application/json; charset=utf-8",
           url: "/gof",
           dataType: "json",
           async: true,
           data: "{\"grid\": ["+dataset+"]}",
           success: function (d) {

           }
         })
       }
 ```

2) If you pasted into your file, make sure to change the "dataset" variable to your variable that contains the information on which cells are alive.

3) The function "success" is currently empty. This is where the data that python posts will arrive (stored in the variable 'd'). Write out this function so that it updates the board.

4) You have goflife.py in the folder. Just run it and it will serve up the pair.html and you can access it in the browser at http://0.0.0.0:5000/.

5) In goflife.py, add code to do the actual evolution of the board.

6) Use print statements and console.log() to understand what's happening, and to see if the communication is happening the way you'd expect.
