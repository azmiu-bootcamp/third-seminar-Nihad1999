print("=========================================")
print("Matrisin elementlerini daxil edin. Aralarinda bosluq qoyun. Vergule ehtiyac yoxdu")
print("=========================================")
matrix = [int(x) for x in input().split()]

enboyuk = max(matrix)

enkicik = min(matrix)

print(enboyuk + enkicik)
