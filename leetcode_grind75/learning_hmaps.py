s = "anagram"
t = "nagaram"
hmap = {}
for i, c in enumerate(s):
    if c not in hmap:
        hmap[c] = 1
    else:
        hmap[c] = hmap[c] + 1 

print(hmap)
print("hello world")
