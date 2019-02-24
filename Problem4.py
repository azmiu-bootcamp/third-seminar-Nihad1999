from operator import itemgetter


matris = [(1 , 7),(1 , 3),(3 , 4), (2 , 2, 1)]

print(matris)
print("****************************")


sorted(matris,key=itemgetter(-1))
print(sorted(matris,key=itemgetter(-1)))
