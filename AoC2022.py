import os as os
import numpy as np
from itertools import *
from math import floor
from math import prod
from math import ceil
import re as re
from copy import deepcopy
from string import ascii_lowercase

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


#day 7
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
len(ans)

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


#day 12 
# z = [x.strip() for x in open("mini_mountain.txt")]
z = [x.strip() for x in open("mountain.txt")]
z = [[ord(i) for i in x] for x in z]
for i in range(len(z)):
    for j in range(len(z[0])):
        # print("%s - %s", [i, j])
        if z[i][j] == ord("S"):
            z[i][j] = ord('a') - 1
        if z[i][j] == ord("E"):
            z[i][j] = ord('z') + 1
            
#where is the starting point?
for i in range(len(z)):
    for j in range(len(z[0])):
        # print("%s - %s", [i, j])
        if z[i][j] == (ord("a") - 1):
            x = i
            y = j
            break

pts0 = [[x, y]]

#where is the end point? 
for i in range(len(z)):
    for j in range(len(z[0])):
        # print("%s - %s", [i, j])
        if z[i][j] == (ord("z") + 1):
            xn = i
            yn = j
            break

def flatlist(l):
    x = []
    for sublist in l:
        if type(sublist) is list:
            for item in sublist:
                x.append(item)
        else:
            x.append(sublist)
    return x

#12.1
#pts = list of current points; l = length of the paths; paths = paths of walks; z = data
def find_summit(pts, l, paths, z):
    pts_new, l_new, paths_new = [], [], []
    xlim, ylim = len(z) - 1, len(z[0]) - 1
    # unique visited points; keep track of visited points
    p_unique = flatlist(paths)
    for i in range(len(pts)):
        E = ord("z") + 1
        
        x = pts[i][0]
        y = pts[i][1]
        w0 = z[x][y]
        if w0 == E:
            print(l[i])
            return(l[i])
        else:
            p = "%s.%s" %(x - 1, y)
            if ((x > 0) & (p not in p_unique)):
                w = z[x - 1][y]
                if w - w0 <= 1: 
                    l_new.append(l[i] + 1)
                    pts_new.append([x - 1, y])
                    p_unique.append(p)
                    tmp = deepcopy(paths[i])
                    tmp.append(p)
                    paths_new.append(tmp)
                        
            p = "%s.%s" %(x + 1, y)
            if ((x < xlim) & (p not in p_unique)):
                w = z[x + 1][y]
                if w - w0 <= 1: 
                    l_new.append(l[i] + 1)
                    pts_new.append([x + 1, y])
                    p_unique.append(p)
                    tmp = deepcopy(paths[i])
                    tmp.append(p)
                    paths_new.append(tmp)
                        
            p = "%s.%s" %(x, y - 1)
            if ((y > 0) & (p not in p_unique)):
                w = z[x][y - 1]
                if w - w0 <= 1: 
                    l_new.append(l[i] + 1)
                    pts_new.append([x, y - 1])
                    p_unique.append(p)
                    tmp = deepcopy(paths[i])
                    tmp.append(p)
                    paths_new.append(tmp)
                        
            p = "%s.%s" %(x, y + 1)
            if ((y < ylim) & (p not in p_unique)):
                w = z[x][y + 1]
                if w - w0 <= 1: 
                    l_new.append(l[i] + 1)
                    pts_new.append([x, y + 1])
                    p_unique.append(p)
                    tmp = deepcopy(paths[i])
                    tmp.append(p)
                    paths_new.append(tmp)
                   
    return(find_summit(pts_new, l_new, paths_new, z))

                        
find_summit(pts0, [0], [["0.0"]], z)          

#12.2
z[pts0[0][0]][pts0[0][1]] = ord("a")

#only viable starts are in the first column
pts0 = [[i, 0] for i in range(len(z))]
out = []
for u in pts0:
    v = ("%s.%s" %(u[0], u[1]))
    out.append(find_summit([u], [0], [[v]], z))

min(out)


#day 13
# z = [x.strip() for x in open("distress_test.txt")]
z = [x.strip() for x in open("distress.txt")]
z = [[eval(z[3*i]), eval(z[3 * i + 1])] for i in range(floor(len(z)/3) + 1)]

#returns: False (not in the right order), True (in the right order)
def parse_distress(l, r):
    for i in range(max(len(l), len(r))):
        if i > (len(r) - 1):
            #right side run out of items
            return(False)
        if i > (len(l) - 1):
            #left side run out of items
            return(True)
        ll = l[i]
        rr = r[i]
        ind = isinstance(ll, int) + (isinstance(rr, int))
        if ind == 2:
            #both entries are integers
            if ll < rr:
                return(True)
            elif ll > rr:
                return(False)
            else:
                if ((len(l) == len(r)) & (len(l) == (i + 1))):
                    return(None)
        else:
            #only one entry is a list
            if not isinstance(ll, list):
                ll = [ll]
            if not isinstance(rr, list):
                rr = [rr]
            tmp = parse_distress(ll, rr)
            if tmp is not None:
                return(tmp)

#13.1
w = []
for i in range(len(z)):
    l = z[i][0]
    r = z[i][1]
    w.append(parse_distress(l, r))

sum([i + 1 for i in range(len(w)) if w[i]])

#13.2        
z.append([[[2]], [[6]]])
z = flatlist(z)

comps = [[0 for i in range(len(z))] for j in range(len(z))]

for i in range(len(z)):
    for j in range(i, len(z)):
        tmp = parse_distress(z[i], z[j])
        if tmp is None:
            comps[i][j] = 0
        else:
            comps[i][j] = 1 * tmp
            comps[j][i] = 1 * (not tmp) 

ind = [sum(x) for x in comps]
z_ord = []
for i in reversed(range(len(z))):
    j = [j for j in range(len(ind)) if ind[j] == i][0]
    z_ord.append(z[j])

ii = [k + 1 for k in range(len(z_ord)) if (z_ord[k] == [[6]] or z_ord[k] == [[2]])]
ii[0] * ii[1]


#day 14
z = [x.strip().split(" -> ") for x in open("sand_test.txt")]
z = [x.strip().split(" -> ") for x in open("sand.txt")]
z = [[[int(v) for v in x.split(",")] for x in w] for w in z]

occupied = []
for w in z:
    for i in range(len(w) - 1):
        a = w[i]
        b = w[i + 1]
        ix = b[0] - a[0]
        iy = b[1] - a[1]
        if ix != 0:
            if ix > 0:
                tmp = range(a[0], b[0] + 1)
            else: 
                tmp = range(b[0], a[0] + 1)
            occupied += [[w, a[1]] for w in tmp]
        else:
            if iy > 0:
                tmp = range(a[1], b[1] + 1)
            else: 
                tmp = range(b[1], a[1] + 1)
            occupied += [[b[0], w] for w in tmp]
 
ymax0 = max([x[1] for x in occupied])
xmin0 = min([x[0] for x in occupied])
xmax0 = max([x[0] for x in occupied])
#rescale co-ordinates in order to represent the system as a matrix (list of lists)
origin = [500 - xmin0, 0]
occupied = [[w[0] - xmin0, w[1]] for w in occupied]
occ = [[0 for i in range(xmax0 - xmin0 + 1)] for j in range(ymax0 + 1)]
for w in occupied:
    occ[w[1]][w[0]] = 1

xmin = min([x[0] for x in occupied])
xmax = max([x[0] for x in occupied])

#14.1
k = 0
not_chasm = True
while not_chasm:
    flag = True
    x = origin[0]
    y = origin[1]
    while flag:
        if (y == ymax0):
            flag = False
            not_chasm = False
            break
        if ((x == xmax) & (occ[y + 1][x - 1] == 1)):
            flag = False
            not_chasm = False
            break
        if (x == xmin):
            flag = False
            not_chasm = False
            break
        if occ[y + 1][x] == 0:
            y += 1
        elif occ[y + 1][x - 1] == 0:
            x -= 1
            y += 1
        elif occ[y + 1][x + 1] == 0:
            x += 1
            y += 1
        else: 
            occ[y][x] = 2
            k += 1
            flag = False

#14.2
ymax = ymax0 + 2
ym = ceil(ymax/2)
origin = [500 - xmin0 + ymax , 0]
occupied2 = [[w[0] + ymax, w[1]] for w in occupied]
occ2 = [[0 for i in range(xmax + 2 * ymax + 1)] for j in range(ymax )]
#floor
occ2.append([1 for i in range(xmax + 2 * ymax + 1)])
for w in occupied2:
    occ2[w[1]][w[0]] = 1

k = 0
not_full = True
while not_full:
    flag = True
    x = origin[0]
    y = origin[1]
    while flag:
        if occ2[origin[1]][origin[0]] == 2:
            flag = False
            not_full = False
            break        
        if occ2[y + 1][x] == 0:
            y += 1
        elif occ2[y + 1][x - 1] == 0:
            x -= 1
            y += 1
        elif occ2[y + 1][x + 1] == 0:
            x += 1
            y += 1
        else: 
            occ2[y][x] = 2
            k += 1
            flag = False


#day 15































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
    
    
