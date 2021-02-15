---
# for interactive use in VSCode
marp: true

# customize the slides side, 16:9 or 4:3
# size: 16:9
size: 4:3

# allow slide number
paginate: true

# theme
theme: Naereen2

# All/first slides are inverted
# class: invert
# _class: invert

# customize header, basic HTML is supported, but not everywhere
footer: Titre footer en bas à gauche, © 2021 <a class="right" href="https://perso.crans.org/besson/">Lilian Besson </a>, (<a class="right" href="https://GitHub.com/Naereen">GitHub/@Naereen</a>), <a href="https://lbesson.mit-license.org/">sous licence MIT</a>

# customize footer, basic HTML is supported, but not everywhere
header: <img height="30em" src="logo.png"> Titre header en haut à gauche

# new slides start on # h1 or ## h2 titles
headingDivider: 2
---

# Démo de **Marp** slides !

Ces slides peuvent être rédigés dans VSCode et visualisés avec Marp.

> Cf [Marp.app](https://marp.app)

On peut les exporter comme une présentation HTML/js interactive, depuis VSCode, et ensuite convertir cette présentation comme un PDF.

> © This document is © Lilian Besson, 2021
> see <https://github.com/Naereen/slides/>

## Paragraphs :rocket:

> On my theme, paragraphs have justified text by default!

*This is random paragraph:* Et commodo culpa adipisicing culpa irure officia excepteur. Irure exercitation veniam laboris quis elit tempor amet pariatur aute est dolore. Excepteur cillum sint in ea laborum in ex duis laboris nostrud minim.

*This is random paragraph:* Et commodo culpa adipisicing culpa irure officia excepteur. Irure exercitation veniam laboris quis elit tempor amet pariatur aute est dolore. Excepteur cillum sint in ea laborum in ex duis laboris nostrud minim.

*This is random paragraph:* Et commodo culpa adipisicing culpa irure officia excepteur. Irure exercitation veniam laboris quis elit tempor amet pariatur aute est dolore. Excepteur cillum sint in ea laborum in ex duis laboris nostrud minim.

## Paragraphs

1. *This is random paragraph:* Et commodo culpa adipisicing culpa irure officia excepteur. Irure exercitation veniam laboris quis elit tempor amet pariatur aute est dolore. Excepteur cillum sint in ea laborum in ex duis laboris nostrud minim.

2. *This is random paragraph:* Et commodo culpa adipisicing culpa irure officia excepteur. Irure exercitation veniam laboris quis elit tempor amet pariatur aute est dolore. Excepteur cillum sint in ea laborum in ex duis laboris nostrud minim.

3. *This is random paragraph:* Et commodo culpa adipisicing culpa irure officia excepteur. Irure exercitation veniam laboris quis elit tempor amet pariatur aute est dolore. Excepteur cillum sint in ea laborum in ex duis laboris nostrud minim.

<!-- _class: titre -->
# Maths using $\LaTeX$ notations

## Maths, with *MathJax*

Inline equations, as for instance the classic $\Delta = b^2-4ac$ and $x_{1,2} = \frac{-b\pm\sqrt{\Delta}}{2a}$, or display equations as this one:
$$ J_\alpha(x) = \sum\limits_{m=0}^\infty \frac{(-1)^m}{m! \, \Gamma(m + \alpha + 1)}{\left({\frac{x}{2}}\right)}^{2 m + \alpha} $$

## More maths

$$ 4 \sum_{n=1}^{+\infty} \rho_n^2 \sin^2 nh = \frac{1}{2\pi} \int_{-\pi}^{\pi}\lvert f(x+h) - f(x-h)\rvert^2 dx. $$
$$ 4 \sum_{n=1}^{+\infty} \rho_n^2 \sin^2 nh = \frac{1}{2\pi} \int_{-\pi}^{\pi}\lvert f(x+h) - f(x-h)\rvert^2 dx. $$
$$ 4 \sum_{n=1}^{+\infty} \rho_n^2 \sin^2 nh = \frac{1}{2\pi} \int_{-\pi}^{\pi}\lvert f(x+h) - f(x-h)\rvert^2 dx. $$
$$ 4 \sum_{n=1}^{+\infty} \rho_n^2 \sin^2 nh = \frac{1}{2\pi} \int_{-\pi}^{\pi}\lvert f(x+h) - f(x-h)\rvert^2 dx. $$

See <https://naereen.github.io/StrapDown.js/example3.html>

<!-- _class: titre -->
# Images

J'ai essayé de faire de ce slide un "titre" avec :
```markdown
<!-- _class: titre -->
```

## Using images

Image left aligned (default):
![width:250](logo.png)
![width:250](logo.png#left)

Image centered:
![width:250](logo.png#center)

Image right aligned:
![width:250](logo.png#right)

```markdown
![width:250](logo.png)
![width:250](logo.png#left)
![width:250](logo.png#right)
![width:250](logo.png#center)
```

## Change width/height of image

![width:100](logo.png)![width:200](logo.png)![width:300](logo.png)

```markdown
![width:100](logo.png)
![width:200](logo.png)
![width:300](logo.png)
```

## Code listing

In OCaml, for instance:
```ocaml
let rec fact n = n ;;
type 'a Tree = Leaf | Node of ('a Tree, 'a, 'a Tree);;
```

Using this Markdown code:
````markdown
```ocaml
let rec fact n = n ;;
type 'a Tree = Leaf | Node of ('a Tree, 'a, 'a Tree);;
```
````

## Bullet list

- One
- Two
- Three

```markdown
- One
- Two
- Three
```

## Fragmented list

* One
* Two
* Three

Lists using `* ` should appear one at a time, in the produced HTML or PDF.

```markdown
* One
* Two
* Three
```

See <https://github.com/marp-team/marpit/issues/145>

## Hex color (White BG + Black text)

![bg](#fff)
![](#000)

Demo of using
```markdown
![bg](#fff)    <!-- white background: default -->
![](#000)      <!-- black text: default -->
```
to change font color and slide background.
(Marp Markdown's syntax extension)

## Named color (black BG + white text)

![bg](black)
![](white)

Demo of using
```markdown
![bg](black)    <!-- black background: ugly -->
![](white)      <!-- white text: ugly -->
```
to change font color and slide background.
(Marp Markdown's syntax extension)

# RGB values (Orange BG + White text)

![bg](rgb(255,128,0))
![](rgb(255,255,255))

Demo of using
```markdown
![bg](rgb(255,128,0))    <!-- orange background: ugly -->
![](rgb(255,255,255))    <!-- white text: ugly -->
```
to change font color and slide background.
(Marp Markdown's syntax extension)

<!--Left hand side -->
## Slides split in two-columns?

See <https://github.com/marp-team/marpit/issues/137>

- item
- item

Image on left side:
![](logo.png)

<!--Right hand side -->
Image on right background side
<!-- ![bg left](logo.png) -->
<!-- FIXME: don't work -->
<!-- ![bg right](logo.png) -->
<!-- FIXME: don't work -->

## TODO:

- [ ] Titles are NOT top aligned yet, I managed to obtain this on old Marp, I want it again!
- [ ] [fontify](https://github.com/Naereen/fontify/) and [my own handwriting font](https://naereen.github.io/My-Own-HandWriting-Font/) don't work yet!
- [ ] Test de ligature fi if si tl rst rest Naereen
- [ ] How to export slides to PDF? Use [`decktape`](https://github.com/astefanutti/decktape) or [`marp-cli`](https://github.com/marp-team/marp-cli)
- [ ] TODO lines are not correctly converted?

## Test of empty slide
<!-- _class: titre -->

I want this header to be top aligned!

## Test of empty slide <!--fit-->
I want this header to be top aligned!

## Conclusion

### :point_right: *Take home message*

- Pretty OK, but not perfect

<br>

<span class="fontify">Merci de votre attention :+1: !</span>

