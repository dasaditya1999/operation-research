import pulp as pl
import time
from datetime import datetime

start_time = time.time()
# start_time = datetime.now()
model = pl.LpProblem(name='exercise', sense=pl.LpMinimize)

x = pl.LpVariable('x', 0, 10)
y = pl.LpVariable('y', 0, 10)

model += x+y<=8
model += 8*x+3*y>=-24
model += -6*x+8*y <=48
model += 3*x+5*y<=15
model += x<=3
model += y>=0

model += -4*x-2*y

status = model.solve()

x_value = pl.value(x)
y_value = pl.value(y)

end_time = time.time()
# end_time = datetime.now()

print("x=",x_value)
print("y=",y_value)
print("time taken", end_time-start_time)