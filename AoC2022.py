import os as os
import numpy as np
from itertools import *
from math import floor
from math import prod
import re as re
from copy import deepcopy

os.chdir("/home/nfg/AoC2022")

#day 5
crane = [x.rstrip("\n").split(" ") for x in open("crane.txt")]
crane = [[int(w[i]) for i in [1, 3, 5]] for w in crane]

#parsing stacks
w = [x.rstrip("\n") for x in open("stacks.txt")]

stacks_tmp = []
for i in range(len(w)):
    z = w[i]
    
    f = range(floor((len(z) - 1)/4) + 1)
    stacks_tmp.append([z[4 * i + 1] for i in f])
 
n = max([len(x) for x in stacks_tmp])    
stacks = []
for i in range(n):
    tmp = []
    for x in reversed(stacks_tmp):
        if (len(x) > i) and (x[i] != ' '):
            tmp.append(x[i])
    print(tmp)
    stacks.append(tmp)
        
#moving shit around 1       
for m in crane:
    for i in range(m[0]):
        stacks[m[2] - 1].append(stacks[m[1] - 1].pop())

''.join([x[len(x) - 1] for x in stacks])

#moving shit around 2   
for m in crane:
    tmp = []
    for i in range(m[0]):
        tmp.append(stacks[m[1] - 1].pop())
    stacks[m[2] - 1] = stacks[m[2] - 1] + [k for k in reversed(tmp)]
        
''.join([x[len(x) - 1] for x in stacks])
        

#day 6
z = [x.rstrip("\n") for x in open("radio.txt")][0]
#6.1
flag = True
i = 0
#moving window and set to check how many different values in each
while (flag and i <= len(z) - 3):
    tmp = set(z[j] for j in range(i, i + 4))
    if len(tmp) < 4:
        i = i + 1
    else:
        flag = False
        ans = i + 4
ans

#6.2
flag = True
i = 0
#moving window and set to check how many different values in each
while (flag and i <= len(z) - 3):
    tmp = set(z[j] for j in range(i, i + 14))
    if len(tmp) < 14:
        i = i + 1
    else:
        flag = False
        ans = i + 14
ans


#day7
z = [x.strip().split(" ") for x in open("file_system.txt")]
# z = [x.rstrip().split(" ") for x in open("file_system_test.txt")]

file_system = {"/": {'tot_size': 0, "children": {}}}

pwd = "/"
cur_dir = file_system["/"]
i = 1
while i < len(z):
    print("%s: dir %s" %(i, pwd))
    w = z[i]
    i = i + 1
    if w[1] == "cd":
        pwd_tmp = w[2]
        if pwd_tmp == "..":
            print("dir %s <- dir %s" %(cur_dir["parent"].keys(), pwd))
            pwd = cur_dir["parent"].keys()   
            cur_dir = cur_dir["parent"]
        else:
            if pwd_tmp not in cur_dir['children'].keys():
                cur_dir['children'][pwd_tmp] = {"parent": cur_dir, "tot_size": 0, "children": {}}
            print("dir %s -> dir %s" %(pwd, pwd_tmp))
            pwd = pwd_tmp
            cur_dir = cur_dir['children'][pwd]
    else:
        w = z[i]
        while (w[0] != "$") & (i < len(z)):
            if w[0] == "dir":
                print("dir %s: contains dir %s" %(pwd, w[1]))
                if w[1] not in cur_dir['children'].keys():
                    cur_dir['children'][w[1]] = {"parent": cur_dir, "tot_size": 0, "children": {}}
            else: 
                cur_dir["tot_size"] = cur_dir["tot_size"] + int(w[0])
            # print(i)
            i = i + 1
            if i < len(z):
                w = z[i]


def calculate_size(d):
    cur_targets = [d]
    dir_size = d["tot_size"]
    while len(cur_targets) > 0:
        chld = []
        for z in cur_targets:
            chld = chld + [w for w in z['children'].values()]
        dir_size = dir_size + sum([z['tot_size'] for z in chld])
        cur_targets = chld
    return(dir_size)
       

#7.1
dir_sizes = []
cur_targets = [file_system['/']]
while len(cur_targets) > 0:
    tmp = [calculate_size(d) for d in cur_targets]
    dir_sizes = dir_sizes + tmp
    cur_tmp = []
    for z in cur_targets:
        cur_tmp = cur_tmp + [w for w in z['children'].values()]
    cur_targets = cur_tmp
        

sum([x for x in dir_sizes if x <= 100000])

#7.2
AVAIL = 70000000 - dir_sizes[0]
TOT_NEEDED = 30000000

min([x for x in dir_sizes if (AVAIL + x >= TOT_NEEDED)])


#day 8
z = [list(x.strip()) for x in open("trees.txt")]
# z = [list(x.strip()) for x in open("trees_test.txt")]
z = [[int(w) for w in x] for x in z]

#8.1
vis = []
m = 0
for i in range(len(z)):
    tmp = []
    for j in range(len(z[i])):
        if ((i in [0, len(z) - 1]) or (j in [0, len(z[i]) - 1])):
            tmp.append(1)
            m += 1
        elif z[i][j] == 0:
            tmp.append(0)
        else:
            zz = z[i][j]
            w = all([z[i][l] < zz for l in range(0, j)])
            e = all([z[i][l] < zz for l in range(j + 1, len(z[i]))])
            n = all([z[k][j] < zz for k in range(0, i)])
            s = all([z[k][j] < zz for k in range(i + 1, len(z))])
            if any([w, e, n, s]):
                tmp.append(1)
                m += 1
            else:
                tmp.append(0)
    vis.append(tmp)

#8.2
sscore = []
for i in range(len(z)):
    tmp = []
    for j in range(len(z[i])):
        if ((i in [0, len(z) - 1]) or (j in [0, len(z[i]) - 1])):
            tmp.append(0)
        elif z[i][j] == 0:
            tmp.append(1)
        else:
            zz = z[i][j]
            f, l, cw = True, j - 1, 0
            while (f & (l >= 0)):
                if z[i][l] >= zz:
                    f = False
                if z[i][l] <= zz:
                    l -= 1
                cw += 1
            
            f, l, ce = True, j + 1, 0
            while (f & (l <= len(z[i]) - 1)):
                if z[i][l] >= zz:
                    f = False
                if z[i][l] <= zz:
                    l += 1
                ce += 1
                    
            f, l, cn = True, i - 1, 0
            while (f & (l >= 0)):
                if z[l][j] >= zz:
                    f = False
                if z[l][j] <= zz:
                    l -= 1
                cn += 1
            
            f, l, cs = True, i + 1, 0
            while (f & (l <= len(z) - 1)):
                if z[l][j] >= zz:
                    f = False
                if z[l][j] <= zz:
                    l += 1
                cs += 1
            tmp.append(cw * ce * cn * cs)
    sscore.append(tmp)

max([max(x) for x in sscore])


#day 9
z = [list(x.strip().split(" ")) for x in open("ropes.txt")]
# z = [list(x.strip().split(" ")) for x in open("ropes_test.txt")]
# z = [list(x.strip().split(" ")) for x in open("ropes_test2.txt")]
for i in range(len(z)):
    z[i][1] = int(z[i][1])

def sign(x):
    if x < 0:
        return(-1)
    elif x > 0: 
        return(1)
    else:
        return(0)
    
DIR = {"L": {"h": -1, "v": 0}, "R": {"h": 1, "v": 0}, "D": {"h": 0, "v": -1}, "U": {"h": 0, "v": 1}}

#9.1
#start at the origin
h_x, h_y = [0], [0]
t_x, t_y = [0], [0]

for i in range(len(z)):
    x = z[i]
    h = DIR[x[0]]["h"]
    v = DIR[x[0]]["v"]

    for i in range(x[1]):
        h_x.append(h_x[-1] + h)
        h_y.append(h_y[-1] + v)
        
        d_x = h_x[-1] - t_x[-1]
        d_y = h_y[-1] - t_y[-1]
        if ((abs(d_x) < 2) & (abs(d_y) < 2)):
            t_x.append(t_x[-1])
            t_y.append(t_y[-1])
        else:
            t_x.append(t_x[-1] + 1 * sign(d_x))
            t_y.append(t_y[-1] + 1 * sign(d_y))

ans = set("%s.%s" %(t_x[i], t_y[i]) for i in range(len(t_x)))

#9.2
r_x, r_y = [], []
for i in range(10):
    r_x.append([0])
    r_y.append([0])

for i in range(len(z)):
    x = z[i]
    h = DIR[x[0]]["h"]
    v = DIR[x[0]]["v"]

    for i in range(x[1]):
        r_x[0].append(r_x[0][-1] + h)
        r_y[0].append(r_y[0][-1] + v)
        
        for j in range(1, len(r_x)):
            d_x = r_x[j - 1][-1] - r_x[j][-1]
            d_y = r_y[j - 1][-1] - r_y[j][-1]
            if ((abs(d_x) < 2) & (abs(d_y) < 2)):
                r_x[j].append(r_x[j][-1])
                r_y[j].append(r_y[j][-1])
            else:
                r_x[j].append(r_x[j][-1] + 1 * sign(d_x))
                r_y[j].append(r_y[j][-1] + 1 * sign(d_y))

ans = set("%s.%s" %(r_x[9][i], r_y[9][i]) for i in range(len(r_x[9])))


#day 10
z = [list(x.strip().split(" ")) for x in open("signal_test.txt")]
z = [list(x.strip().split(" ")) for x in open("signal.txt")]

#10.1    
t = 1
et = []
event = []

for w in z:
    if w[0] == "noop":
        t += 1
    else:
        t += 2
        et.append(t)
        event.append(int(w[1]))
        
check_t = [20, 60, 100, 140, 180, 220]
x_t = []
tt, i, x = 0, 0, 1
for s in check_t:
    while tt <= s:
        x += event[i]
        i += 1
        tt = et[i]
    x_t.append(x)
    
sum([x_t[i] * check_t[i] for i in range(len(x_t))])

#10.2
ett = [t - 1 for t in et]
x = 1
screen = [[],[],[],[],[],[]]
for t in range(1, ett[-1] + 4):
    print(t)
    pos = (t - 1) % 40
    j = floor((t - 1)/40)
    if pos in [x - 1, x, x + 1]:
        screen[j].append("#")
    else:
        screen[j].append(".")
    if t in ett:
        xt = it.compress(event, [t == x for x in ett])
        xt = [x for x in xt][0]
        x += xt
        
 
#day 11       
z = [list(x.strip().split(" ")) for x in open("monkeys_test.txt")]
# z = [list(x.strip().split(" ")) for x in open("monkeys.txt")]
ind = [i for i in range(len(z)) if z[i][0] == "Monkey"]

monkeys0 = []
for i in ind:
    tmp = [z[k] for k in range(i, i + 6)] 
    items = [int(re.sub(",","", k)) for k in tmp[1][2:]]
    op = "".join(tmp[2][3:])
    test = int(tmp[3][3])
    pass_ = int(tmp[4][5])
    fail = int(tmp[5][5])
    monkeys0.append({"items": items, "operation": op, "test": test, "pass": pass_, "fail": fail, "count": 0})

#11.1
counts = [0 for i in range(len(monkeys0))]
monkey_items = [[] for i in range(len(monkeys0))]
monkeys = deepcopy(monkeys0)

for k in range(20):
    for m in monkeys:
        for j in range(len(m["items"])):
            m["count"] += 1
            i = m["items"].pop(0)
            old = i
            i = eval(m["operation"])
            i = floor(i/3)
            if (i % m["test"] == 0):
                monkeys[m["pass"]]["items"].append(i)
            else:
                monkeys[m["fail"]]["items"].append(i)
                
counts = [m["count"] for m in monkeys]
counts.sort()
prod(counts[-2:])

#11.2
monkeys2 = deepcopy(monkeys0)
for k in range(20):
    print(k)
    for m in monkeys2:
        for j in range(len(m["items"])):
            m["count"] += 1
            i = m["items"].pop(0)
            old = i
            i = eval(m["operation"])
            if i > 1500:
                i = i - 1000
            if (i % m["test"] == 0):
                monkeys2[m["pass"]]["items"].append(i)
            else:
                monkeys2[m["fail"]]["items"].append(i)
                
counts = [m["count"] for m in monkeys2]
counts















def factorise(n):
    factors = []
    i = 2
    while n != 1:
        while (n % i == 0):
            factors.append(i)
            n = n/i
        i += 1
    return(factors)
                
    
monkeys2 = deepcopy(monkeys0)
test = [x["test"] for x in monkeys2]
for k in range(20):
    print(k)
    for m in monkeys2:
        for j in range(len(m["items"])):
            m["count"] += 1
            i = m["items"].pop(0)
            old = i
            i = eval(m["operation"])
            if (i % m["test"] == 0):
                i = i/m["test"]
                monkeys2[m["pass"]]["items"].append(i)
            else:
                f = factorise(i)
                tt = max([ff for ff in f if f not in test])
                i = i/tt
                monkeys2[m["fail"]]["items"].append(i)
                
counts = [m["count"] for m in monkeys2]
counts.sort()
prod(counts[-2:])

n = 20 
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1