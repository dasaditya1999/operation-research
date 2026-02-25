import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

print("pyomo successfully imported")

model = pyo.ConcreteModel()

# Setting up the variables
model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))

x = model.x
y = model.y

# Setting up the constraint
model.c1 = pyo.Constraint(expr=-x+2*y<=8)
model.c2 = pyo.Constraint(expr=2*x+y<=14)
model.c3 = pyo.Constraint(expr=2*x-y<=10)

#define the objective function
model.obj = pyo.Objective(expr=x+y, sense=maximize)

#Define solver
# opt = SolverFactory('glpk')
opt = SolverFactory('cbc')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print("----------------")
print("x=", x_value)
print("y=", y_value)
