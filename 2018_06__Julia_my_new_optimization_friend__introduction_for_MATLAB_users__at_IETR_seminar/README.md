---
title: Julia, my new optimization friend
subtitle: Julia introduction for MATLAB users
author: Lilian Besson
institute: SCEE Team, IETR, CentraleSupélec, Rennes
date: Thursday 14th of June, 2018
lang: english
---

# Julia, my new optimization friend

- *About:* **the Julia programming language, an introduction for MATLAB users**

- *Date:* 14th of June 2018

- *Who:* Lilian Besson

---

# Agenda for today [15 min]

1. What is Julia [3 min]
2. Main differences in syntax and concepts [5 min]
3. Examples of problems solved Julia [5 min]
4. Where can you find more information ?  [2 min]:snake:
:snake:

---

# 1. What is Julia :snake: ?

- Developed and popular from the last 5 years
- Open-source and free programming language
- Interpreted *and* compiled, multi-platform, imperative and object-oriented
- Designed and acknowledged as *simple to learn and use*
- Used worldwide: research, data science, web applications etc

### Ressources
- **Website**: [JuliaLang.org](https://julialang.org/) for the language & [Pkg.JuliaLang.org](https://pkg.julialang.org/) for packages
- Documentation : [docs.JuliaLang.org](https://docs.julialang.org/en/latest/)
:snake:
:snake:
---

# Comparison with MATLAB

|  | Julia :smiley: | MATLAB :cry:
|:-|:-:|:-:|
| **Cost** | Free :v: | Hundreds of euros / year
| **License** | Open-source | 1 year user license (no longer after your PhD!)
| **Comes from** | A non-profit foundation, and the community | MathWorks company
| **Scope** | Generic | Numeric only
| **Usage** | Generic, worldwide :earth_americas: | Research in academia and industry

---

|  | Julia :smiley: | MATLAB :cry:
|:-|:-:|:-:|
| **Packaging** | `Pkg` manager included | Toolboxes already included
| **IDE** | [*Jupyter*](https://jupyter.org/) by default ([*Juno*](http://junolab.org/)) | Good IDE already included
| **Support?** | Community (StackOverflow, IRC, mailing lists etc). JuliaPro with paid license, if professional support is needed | By MathWorks ?
| **Performances** | Best performance ever | Faster than Python, slower than Julia
| **Documentation** | OK and growing | OK and inline

---

# How to install Julia :arrow_down:
- You can try online *for free* on [JuliaBox.com](https://www.juliabox.com/)
- On Linux and Mac OS and On Windows:
  + You can use the default installer from [python.org/downloads/windows](https://julialang.org/downloads/) :package:
- Takes about 10 minutes... and it's free !

> You also need Python 3 to use Jupyter, I suggest to use:snake:
:snake:
> [Anaconda.com/download](https://www.anaconda.com/download/) (:sparkles:)

---

# My suggestions for Julia
- Use `julia` for the command line for fast experimentations
- Use **Jupyter notebooks** to write or share your experiments
  (jupyter.org, eg. github.com/Naereen/notebooks)
- Use the *Juno* IDE to edit large projects

---

## :package: How to install modules in Julia
- Installing is **easy** !
```julia
julia> Pkd.add("IJulia")  # installs IJulia
```

- Updating also!
```julia
julia> Pkg.update()
```

## :mag: How to find the module you need ?
- Ask your colleagues :smile: !
- Complete list on [pkg.JuliaLang.org](https://pkg.julialang.org)

---

# :package: Overview of famous Julia modules

- [Gadfly.jl](http://gadflyjl.org/) for plotting (default)
- [Winston.jl](https://github.com/nolta/Winston.jl) for easy plotting like MATLAB
- [JuliaDiffEq.org](http://juliadiffeq.org) collection
- [JuliaOpt](https://www.juliaopt.org/) collection
- [JuliaStats](http://juliastats.github.io) collection

> Find more specific packages on [GitHub.com/svaksha/Julia.jl/](https://github.com/svaksha/Julia.jl/)

---

# Many packages, and a fastly growing community

[![bg](figures/pulse_julia_allver.png)](https://pkg.julialang.org/pulse.html)

---

# 2. Main differences in syntax between Julia and MATLAB
> Ref: mathesaurus.sourceforge.net/matlab-python-xref.pdf

|  | Julia | MATLAB
|:-|:-:|:-:|
| **File ext.** | `.jl` | `.m`
| **Comment** | `# blabla...` | `% blabla...`
| **Indexing** | `a[1]` to `a[ed]` | `a(1)` to `a(end)`
| **Slicing** | `a[1:100]` (view) | `a(1:100)` (:warning: copy)
| **Operations** | Linear algebra by default | Linear algebra by default
| **Block** | Use `end` | Use `endif` `endfor` etc

---

|  | Julia | MATLAB
|:-|:-:|:-:|
| **Help** | `?func` | `help func`
| **And** | `a & b` | `a && b`
| **Or** | `a | b` | `a || b`
| **Datatype** | `Array` of *any* type | multi-dim doubles array
| **Array** | `[1 2; 3 4]` | `[1 2; 3 4]`
| **Size** | `size(a)` | `size(a)`
| **Nb Dim** | `ndims(a)` | `ndims(a)`
| **Last** | `a[end]` | `a(end)`

---

|  | Julia | MATLAB
|:-|:-:|:-:|
| **Tranpose** | `a.'` | `a.'`
| **Conj. transpose** | `a'` | `a'`
| **Matrix** x | `a * b` | `a * b`
| **Element-wise** x | `a .* b` | `a .* b`
| **Element-wise** / | `a ./ b` | `a ./ b`
| **Element-wise** ^ | `a ^ 3` | `a .^ 3`
| **Zeros** | `zeros(2, 3, 5)` | `zeros(2, 3, 5)`
| **Ones** | `ones(2, 3, 5)` | `ones(2, 3, 5)`
| **Identity** | `eye(10)` | `eye(10)`
| **Range** | `range(0, 100, 2)` or `1:2:100` | `1:2:100`

---

|  | Julia | MATLAB
|:-|:-:|:-:|
| **Maximum** | `max(a)` | `max(max(a))` ?
| **Random matrix** | `rand(3, 4)` | `rand(3, 4)`
| L2 **Norm** | `norm(v)` | `norm(v)`
| **Inverse** | `inv(a)` | `inv(a)`
| **Pseudo inv** | `pinv(a)` | `pinv(a)`
| **Solve syst.** | `solve(a, b)` | `a \ b`
| **Eigen vals** | `V, D = eig(a)` | `[V,D]=eig(a)`
| **FFT/IFFT** | `fft(a)`, `ifft(a)` | `fft(a)`,`ifft(a)`


---

# 3. Scientific problems solved with Julia
> Just to give examples of syntax and modules

1. 1D numerical integration and plot
2. Solving a $2^{\text{nd}}$ order Ordinary Differential Equation
3. Solving a constraint optimization problem and plotting solution

---

# 3.1. 1D numerical integration and plot

FIXME convert to Julia !

> Goal : evaluate and plot the function on [-1, 1] :
> $$\mathrm{Ei}(x) := \int_{-\infty}^x \frac{\mathrm{e}^u}{u} \;\mathrm{d}u$$

## How to?
Use modules!

- `numpy` for maths functions and arrays
- `scipy.integrate.quad` function for numerical integration
- `matplotlib.pyplot.plot` for 2D plotting

---

FIXME convert to Julia !

```python
import numpy as np                # standard convention
import matplotlib.pyplot as plt   # standard convention
from scipy.integrate import quad  # need only 1 function

def Ei(x, minfloat=1e-6, maxfloat=1000):
    def f(t):
        return np.exp(-t) / t
    if x > 0:
        return -1.0 * (quad(f, -x, -minfloat)[0]
                     + quad(f, minfloat, maxfloat)[0])
    else:
        return -1.0 * quad(f, -x, maxfloat)[0]


X = np.linspace(-1, 1, 1000) # 1000 points
Y = np.vectorize(Ei)(X)      # or [Ei(x) for x in X]
plt.plot(X, Y)               # MATLAB-like interface
plt.title("The function Ei(x)")
plt.xlabel("x"); plt.ylabel("y")
plt.savefig("figures/Ei_integral.png")
plt.show()
```

---

<center><img width="70%" src="figures/Ei_integral.png"></center>
![bg original 90%](figures/Ei_integral.png)

---

# 3.2. Solving a $2^{\text{nd}}$ order ODE

> Goal : solve and plot the differential equation of a pendulum:
> $$\theta''(t) + b \,\theta'(t) + c \,\sin(\theta(t)) = 0$$
> For $b = 1/4$, $c = 5$, $\theta(0) = \pi - 0.1$, $\theta'(0)=0$, $t\in[0,10]$

## How to?
Use modules!

- `scipy.integrate.odeint` function for ODE integration
- `matplotlib.pyplot.plot` for $2$D plotting

---

FIXME convert to Julia !

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint   # use Runge-Kutta 4

def pend(y, t, b, c):  # function definition
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])

b, c = 0.25, 5.0  # tuple assignment
y0 = np.array([np.pi - 0.1, 0.0])
t = np.linspace(0, 10, 101)  # on [0,10] with 101 points

sol = odeint(pend, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')# blue
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')# green
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("figures/Pendulum_solution.png")
plt.show()
```

---

![bg original 90%](figures/Pendulum_solution.png)

---

# 3.3. Constraint optimization problem

> Goal: minimize a function under linear inequality constraints:
> $$f(x,y) := (x - 1)^2 + (y - 2.5)^2$$
> $$\text{such that } \begin{cases}x \geq 0 \text{ and } y \geq 0 \\ x - 2y + 2 \geq 0 \\ - x - 2y + 6 \geq 0 \\ x + 2y + 2 \geq 0\end{cases}$$

## How to?

- `scipy.optimize.minimize` function for black-box minimization

---

# 3.3. Constraint optimization problem

FIXME convert to Julia !

```python
from scipy.optimize import minimize

def obj(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

x0 = (2, 0)  # first guess

bnds = ((0, None), (0, None))  # [0, +oo) for x and y

cons = ({'type': 'ineq', 'fun': lambda x: x[0]-2*x[1]+2},
        {'type': 'ineq', 'fun': lambda x:-x[0]-2*x[1]+6},
        {'type': 'ineq', 'fun': lambda x:-x[0]+2*x[1]+2})


res = minimize(obj, x0, method='SLSQP', bounds=bnds,
               constraints=cons)
print("Minimum is", res.x)  # Minimum is (1.4, 1.7)
```

---

# Conclusion (1/2)

## Sum-up
- I hope you got a good introduction to Julia
- It's not hard to migrate from MATLAB to Julia
- Good start: [docs.JuliaLang.org/en/stable/manual/getting-started/](https://docs.julialang.org/en/stable/manual/getting-started/)


---

# Conclusion (2/2)

> *Thanks for joining :clap: !*

## Your mission, if you accept it... :boom:
1. *Padawan level:* Train yourself a little bit on Julia
   $\hookrightarrow$ introtopython.org or learnpython.org
   Read [introduction in the Julia manual](https://docs.julialang.org/en/stable/manual/introduction/)
2. *Jedi level:* Try to solve a numerical system, from your research or teaching, in **Julia** instead of MATLAB
3. *Master level:* From now on, try to use open-source tools for your research (Julia, Python and others)
