import re 
s = "three big apple trees"
p = "Apple tree"
if(len(p)>len(s)):print("Invalid Input")

for i in range(len(p)):
    if i == 0 and p[i+1:] in s:
        print(s.find(p[i+1])-1)
        break
    if p[:i] in s and p[i+1:] in s:
        print(s.find(p[:i]))
        break
else:
    print("No match found")
print()
