# Étude about feeling

Era uma noite normal, estava cansado, mas não queria dormir. Decidi abrir o *youtube* e descobri um vídeo sobre a melhor forma de selecionar um ponto dentro de um **círculo** <sup>[1]</sup>.

Então comecei a pensar em qual seria a melhor forma de **preencher um círculo**, e aqui mostro o resultado.

* **Language**: *JavaScript*
* **Libraries**: *P5.js* <sup>[2]</sup>

<br></br>

-----
## Linhas
A primeira tentativa foi escolher dois pontos aleatórios na circunferência e unir os mesmos através de uma linha reta. Os pontos são selecionados através dos ângulos, tal que *a ∈ [0,2π]*, ou seja, o ângulo está em *radianos* <sup>[3]</sup>, e as coordenadas finais serão obtidas através da utilização de *coordenadas polares*<sup>[4]</sup>

```js
function lines(){
  let a = random(2*PI)
  let b = random(2*PI)
  
  line(r*cos(a),r*sin(a), r*cos(b), r*sin(b))
}
```

![Lines 1](/assets/etude/lines.png)

<br></br>

A segunda tentativa consistiu em escolher pontos, desta vez não necessáriamente pertencentes à circunferência, e unir
os mesmo através de retas. Para escolher cada ponto, selecionei um ângulo tal que  *a ∈ [0,2π]* e um raio tal que *r₂ ∈ [0,r]*

```js
function lines2(){  
  let a = random(2*PI)
  let b = random(2*PI)
  
  let r1 = random(r)
  let r2 = random(r)
  
  line(r1*cos(a), r1*sin(a), r2*cos(b), r2*sin(b))
}
```

![Lines 2](/assets/etude/lines2.png)

<br></br>

De seguida, apenas alterei a forma como os raios dos pontos são selecionados, utilizando uma função random diferente **rand** <sup>[5]</sup>.

```js
function lines3(){
  let a = random(2*PI)
  let b = random(2*PI)
  
  let r1 = rand(r)
  let r2 = rand(r)
  
  line(r1*cos(a), r1*sin(a), r2*cos(b), r2*sin(b))
}
```

![Lines 3](/assets/etude/lines3.png)

<br></br>

## Círculos

Para os antigos, Círculos eram perfeitos, então, porque não tentar preencher um círculo com outros círculos?

A primeira versão, começa por rodar a tela num ângulo aleatório a, tal que *a ∈ [0,2π]*. De seguida, escolhe um raio rr tal que *rr ∈ [0,r]* e desenha um círculo tangente à circunferência original ou seja, com centro nas coordenadas *(r-rr, 0)* e raio *rr*, mas devemos nos lembrar que aplicamos previamente um raotação de ângulo *a*.

```js
function circs(){
    push()
      rotate(random(2*PI))
      let rr = random(r)
  
      circle(r-rr,0,rr)
    pop()
}
```

![Circles 1](/assets/etude/circs.png)

<br></br>

A segunda versão, segue o mesmo princípio da primeira, apenas alterando a forma como escolhe o raio<sup>[5]</sup>.

```js
function circs2(){
    push()
      rotate(random(2*PI))
      let rr = rand(r)
  
      circle(r-rr,0,rr)
    pop()
}
```

![Circles 2](/assets/etude/circs2.png)

<br></br>

## Pontos
O terceiro método baseia-se em desenhar pontos dentro do círculo.

A primeira versão escolhe um **ângulo a** e um **raio rr**, e através de coordenadas polares desenha esse ponto.

```js
function dots(n){
    let a = random(2*PI)
    let rr = random(r)
    
    point(rr*cos(a),rr*sin(a))
}
```

![Dots 1](/assets/etude/dots.png)

<br></br>

A segunda versão escolhe um **ângulo a**, mas a função que seleciona o raio é **rand** <sup>[5]</sup>.

```js
function dots2(n){
    let a = random(2*PI)
    let rr = rand(r)
    point(rr*cos(a),rr*sin(a))
}
```

![Dots 2](/assets/etude/dots3.png)

<br></br>

Por fim, são selecionadas *duas coordenadas, x e y*, tal que *x, y ∈ [-r,r]*.
Este método tem o problema de alguns dos possíveis pontos não estarem contidos no círculo, pelo que utilizei o *teorema de pitágoras*, para saber se a distância entre este ponto e o centro era menor ou igual que o raio *(x² + y² ≤ r²)*. No caso do ponto não estar contido, a função seria repetida, até que o ponto selecionado estivesse contido no círculo.

```js
function dots3(){
  while(true){
    let x = random(-r,r)
    let y = random(-r,r)
    
    if (x*x + y*y <= r*r){
      point(x,y)
      return
    }
  }
}
```

![Dots 3](/assets/etude/dots2.png)

<br></br>

-----
*[1]*: [Vídeo](https://www.youtube.com/watch?v=4y_nmpv-9lI&t=166s)

*[2]*: [P5.js](https://p5js.org/)

*[3]*: [Radianos](https://upchieve.org/blog/2021/4/18/what-are-radians)

*[4]*: [Coordenadas polares](https://tutorial.math.lamar.edu/Classes/CalcII/PolarCoordinates.aspx) são um sistema de coordenadas, onde, em vez de duas coordenadas *x* e *y* temos uma coordenada *r (distância à origem)* e uma coordenada *φ (ângulo feito com o semi-eixo positivo Ox)*. Este tipo de coordenadas facilida o estudo de movimentos circulares por exemplo e a conversão entre coordenadas polares e cartezianas pode ser feita da seguinte forma:

* Polares → Cartezianas:
    * *x = r · cos(φ)*
    * *y = r · sin(φ)*

* Cartezianas → Polares:
    * *r = √(x² + y²)*
    * *φ =*
        * *arctan(y/x) if x > 0*
        * *arctan(π + y/x) if x < 0*

*[5]*: a função rand foi definida por mim da seguinte forma:

```js
function rand(m){
  return sqrt(random(m) * random(m))
}
```

Ou seja, utilizando **√(m₁+m₂)**, onde m₁ e m₂ são números aleatórios tal que: **m₁,m₂ ∈ [0,m]**