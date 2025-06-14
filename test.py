l_l=["1","2","3"]
l=["2","3","4"]
res=0
for i in l_l:
    for j in l:
        if i==j:
            res=i
print(l_l.index(res))