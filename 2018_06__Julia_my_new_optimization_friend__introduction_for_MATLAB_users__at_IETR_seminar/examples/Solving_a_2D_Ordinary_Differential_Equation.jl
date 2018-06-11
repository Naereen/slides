#! /usr/bin/env julia

using DifferentialEquations

b, c = 0.25, 5.0
pend2 = @ode_def Pendulum begin
  dθ = ω
  dω = (-b * ω) - (c * sin(θ))
end

prob = ODEProblem(pend, y0, (0.0, 10.0))
sol = solve(prob)   # solve on [0,10]
t, y = sol.t, hcat(sol.u...)'

using Winston
plot(t, y[:, 1], t, y[:, 2])
title("2D Differential Equation")
savefig("figures/Pendulum_solution.png")
