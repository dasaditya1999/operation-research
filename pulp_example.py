import pulp as pl

model = pl.LpProblem(name='Demo', sense=pl.LpMaximize)

#Initialize the variables
x = pl.LpVariable('x', 0, 10)
y = pl.LpVariable('y', 0, 10)

#define constraints
model += -x+2*y<=8
model += 2*x+y<=14
model += 2*x-y<=10

#define objective function
model += x+y

#invoke solve function
status = model.solve() #CBC is the default solver in PuLP

#get the values of x & y
x_value = pl.value(x) 
y_value = pl.value(y)

print('x=', x_value)
print('y=', y_value)