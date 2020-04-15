from __future__ import print_function
from ortools.linear_solver import pywraplp

def solve_coexistence():
    t = "Amphibia coexistence"
    #sets
    s = pywraplp.Solver(t,pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    #one dimesional array of decision varibles (can be between 0 and 1000)
    x = [s.NumVar(0,1000, 'x[%i]'  % i) for i in range(3)]
    #used for debugging aux variable
    pop = s.NumVar(0,3000,'pop')
    s.Add(2*x[0] + x[1] + x[2] <= 1500)
    s.Add(x[0] + 3*x[1] + 2*x[2] <= 3000)
    s.Add(x[0] + 2*x[1] + 3*x[2] <= 5000)
    s.Add(pop== x[0] + x[1]+x[2])
    # s.Maximize(pop)
    s.Maximize(x[0]+x[1]+x[2])
    s.Solve()
    return pop.SolutionValue(), [e.SolutionValue() for e in x]

# print(solve_coexistence())
pop,x=solve_coexistence()
T=[['Specie','Count']]
for i in range(3):
    T.append([['Toad',"Salamnders","Caecilians"][i],x[i]])
T.append(['Total',pop])
for e in T:
    print(e[0],e[1])