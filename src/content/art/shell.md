# 🐚 Shell

**Shell**, uma tentativa falhada de *sizecoding* <sup>[1]</sup> que acabou por ficar bonito e caber num tweet.

* **Linguagem**: *JavaScript*
* **Bibliotecas**: *P5.js* <sup>[2]</sup>

-----

![Shell 1](/assets/shell/1.png)

![Shell 2](/assets/shell/2.png)

![Shell 3](/assets/shell/3.png)

![Shell 4](/assets/shell/4.png)

![Shell 5](/assets/shell/5.png)

![Shell 6](/assets/shell/6.png)

![Shell 7](/assets/shell/7.png)

![Shell 8](/assets/shell/8.png)

![Shell Code 1](/assets/shell/carbon.png)

![Shell Code 2](/assets/shell/c2.png)

-----

Code:
```js
function setup() {
  let w = 700
  createCanvas(w, w)
  background(0)

  let r = random

  push()
  translate(w / 2, w / 2)

  let s = r(50, 250)
  let p = r(8, 13)

  for (let i = p; i < w * 2; i += p) {
    stroke(i % s, 240)
    fill(0, 2)
    ellipse(0, 0, i, i * 2)
    rotate(0.1)
  }
  pop()

  fill(r(30, 250), r(30, 250), r(30, 250), r(50, 80))
  rect(0, 0, w, w)
}

// Minified
function setup(){

    for(w=700,createCanvas(w,w),push(),translate(w/2,w/2),background(0),r=random,s=r(50,250),p=r(8,13),i=p;i<2*w;i+=p)stroke(i%s,240),fill(0,2),ellipse(0,0,i,2*i),rotate(.1);pop(),fill(r(30,250),r(30,250),r(30,250),r(50,80)),rect(0,0,w,w)

} // 234 bytes 
```

<br>
-----
<br>

*[1]*: [Size Coding](http://www.sizecoding.org/wiki/Main_Page)

*[3]*: [P5.js](https://p5js.org/)
