
with open("pi1000000.txt","r") as f:
	data = f.readlines()
print(data[0][:10])
pi = data[0][0] + data[0][2:]
from collections import Counter
pidigits = Counter(pi)
print(pidigits)
print(sum(pidigits.values()))
#isk = []
#after_isk = []
pidigits_afterisk = []
for i in range(10):
    isk = [n for n,x in enumerate(pi) if x == str(i)]
    after_isk = [pi[n+1] for n in isk if n != len(pi) - 1]
    pidigits_afterisk.append(Counter(after_isk))
    print(pidigits_afterisk)



import matplotlib.pyplot as plt

## fig1
pidigits_for_barplot = []
for i in range(0,10):
    pidigits_for_barplot.append(pidigits[str(i)])
plt.figure()
plt.xticks(list(range(10)))
plt.xlabel("digit")
plt.ylabel("count")
plt.title("1000000 digits of pi digit distribution")
plt.bar(list(range(10)),pidigits_for_barplot)
plt.savefig("./plts/pi_distribution.png")

##fig 2
pidigits_afterisk_all_for_barplot = []
for k in range(10):
    pidigits_afterisk_for_barplot = []
    for i in range(0,10):
        pidigits_afterisk_for_barplot.append(pidigits_afterisk[k][str(i)])
    plt.figure()
    plt.xticks(list(range(10)))
    plt.xlabel("digit")
    plt.ylabel("count")
    plt.title(f"1000000 digits of pi digit distribution after sequence : '{str(k)}'")
    plt.bar(list(range(10)),pidigits_afterisk_for_barplot)
    plt.savefig(f"./plts/pi_distribution_after{k}.png")
    pidigits_afterisk_all_for_barplot.append(pidigits_afterisk_for_barplot)

import scipy.stats
res, p = scipy.stats.chisquare(pidigits_for_barplot)
print("Distribution of the first 1000000 digits of pi is an uniform distribution, p value=", p)
for k in range(10):
    res2, p = scipy.stats.chisquare(pidigits_afterisk_all_for_barplot[k])
    print(f"Distribution of the first 1000000 digits of pi trailing '{k}' is an uniform distribution, p value=",p)