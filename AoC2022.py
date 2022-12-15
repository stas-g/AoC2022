import os as os
import numpy as np
from itertools import *
from math import floor

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













file_system = {"/": {'tot_size': 0, "children": []}}

pwd = "/"
i = 0
while i < len(z):
    print("%s: dir %s" %(i, pwd))
    w = z[i]
    i = i + 1
    if w[1] == "cd":
        pwd_tmp = w[2]
        if pwd_tmp == "..":
            print("dir %s <- dir %s" %(file_system[pwd]["parent"], pwd))
            pwd = file_system[pwd]["parent"]
        else:
            if pwd_tmp not in file_system.keys():
                file_system[pwd_tmp] = {"parent": pwd, "tot_size": 0, "children": []}
            print("dir %s -> dir %s" %(pwd, pwd_tmp))
            pwd = pwd_tmp
    else:
        w = z[i]
        while (w[0] != "$") & (i < len(z)):
            if w[0] == "dir":
                print("dir %s: contains dir %s" %(pwd, w[1]))
                if w[1] not in file_system.keys():
                    file_system[w[1]] = {"parent": pwd, "tot_size": 0, "children": []}
                    file_system[pwd]["children"] = file_system[pwd]["children"] + [w[1]]
            else: 
                file_system[pwd]["tot_size"] = file_system[pwd]["tot_size"] + int(w[0])
            # print(i)
            i = i + 1
            if i < len(z):
                w = z[i]


dir_sizes = {}
for k,v in file_system.items():
    dir_size = v["tot_size"]
    chld, chld_tmp = v['children'], v['children']
    while len(chld_tmp) > 0:
        chld_tmp2 = []
        for a in chld_tmp:
            chld = chld + file_system[a]["children"]
            chld_tmp2 = chld_tmp2 + file_system[a]["children"]
        chld_tmp = chld_tmp2

    dir_size = dir_size + sum([file_system[a]["tot_size"] for a in chld])
    dir_sizes[k] = dir_size

sum([v for v in dir_sizes.values() if v <= 100000])

cur_targets = [file_system["/"]]
while len(cur_targets) > 0:
    for z in cur_targets:
        dir_size = z["tot_size"]
        chld, chld_tmp = z['children'], z['children']
        while len(chld_tmp) > 0:
            chld_tmp2 = []
            for a in chld_tmp:
                chld = chld + file_system[a]["children"]
                chld_tmp2 = chld_tmp2 + file_system[a]["children"]
            chld_tmp = chld_tmp2

        dir_size = dir_size + sum([file_system[a]["tot_size"] for a in chld])
        dir_sizes[k] = dir_size

sum([v for v in dir_sizes.values() if v <= 100000])


def calculate_size(d):
    cur_targets = [d]
    dir_size = d["tot_size"]
    while len(cur_targets) > 0:
        chld = [z['children'] for z in cur_targets][0]
        chld = [x for x in chld.values()]
        dir_size = dir_size + sum([z['tot_size'] for z in chld])
        cur_targets = chld
    return(dir_size)


sum_ = 0
for i in range(len(z)):
    if z[i][0] not in ["$", "dir"]:
        sum_ = sum_ + int(z[i][0])