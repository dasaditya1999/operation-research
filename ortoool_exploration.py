import ortools

from ortools.linear_solver import pywraplp

#Define which solver you want to use for ortools
solver = pywraplp.Solver.CreateSolver('GLOP')

#Define variables
x = solver.NumVar(0,10,'x')
y = solver.NumVar(0,10,'y')

#Define Constraints
solver.Add(-x+2*y<=10)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

solver.Maximize(x+y)

results = solver.Solve()

print("x", x.solution_value())
print("y", y.solution_value())

