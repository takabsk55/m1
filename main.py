#審査結果
#順番は、ミルクボーイ、かまいたち、ぺこぱ、和牛、見取り図、
# からし蓮根、オズワルド、すえひろがりず、インディアンズ、ニューヨーク

kyojinn=[1,3,3,6,2,3,9,6,6,10]
hanawa=[1,3,4,2,5,9,8,6,9,6]
siraku=[1,3,6,2,4,8,8,5,10,7]
tomi=[1,3,2,4,4,7,4,7,7,10]
reiji=[1,2,7,4,4,4,2,9,7,10]
matumoto=[1,2,3,4,5,6,7,8,9,10]
kami=[1,3,2,8,4,4,4,8,4,10]

judgelist=[kyojinn,hanawa,siraku,tomi,reiji,matumoto,kami]
judgename=["巨人","塙","志らく","富澤","礼二","松本","上沼"]
n=10

def spearman(list1,list2):
    sigma=0
    for i in range(n):
        sigma+=(list1[i]-list2[i])**2
    r=1-6*sigma/(n*(n**2-1))
    return r

import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import japanize_matplotlib

p_list=list(itertools.permutations(judgelist,2))

m=len(judgelist)

result=[[0 for i in range(m)] for j in range(m)]
for i in range(len(p_list)):
    r=spearman(p_list[i][0],p_list[i][1])

    result[judgelist.index(p_list[i][0])][judgelist.index(p_list[i][1])]=r

for i in range(m):
    print(result[i])

fig, ax = plt.subplots()
sns.heatmap(data=result, cmap=sns.color_palette("Blues", 24), annot=True, fmt=".2f", vmax=1, vmin=0, square=True,linewidths=1)

ax.set_xticks(np.arange(m) + 0.5, minor=False)
ax.set_yticks(np.arange(m) + 0.5, minor=False)

ax.xaxis.tick_top()


ax.set_xticklabels(judgename, minor=False)
ax.set_yticklabels(judgename, minor=False)

plt.setp(ax.get_yticklabels(), rotation=0, ha='right')

plt.show()
plt.savefig('image.png')