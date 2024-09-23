points = [[1,3],[-2,2]]
k = 1
kth = []
for point in points:
    if not kth or len(kth) > k:
        kth.append(point)
    
    
print(kth[0][0], kth[0][1])
print(kth[0])