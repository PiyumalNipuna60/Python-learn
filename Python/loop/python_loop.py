# -*- coding: utf-8 -*-
"""python loop

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13qSZLKs8uO_2C4IwMRXyO9B37IOZ2Uep

# loop
- for-loop
-while loop


---
# continue and break
"""

print("nipuna")
print("nipuna")
print("nipuna")
print("nipuna")
print("nipuna")

for i in range(10):
  print("nipuna")

x=("10","20","30","40","50")
for num in x:
  print(num)

x={"name":"kamal", "age":"20", "address":"galle"}
for i in x:
  print(i)

x={"name":"kamal", "age":"20", "address":"galle"}
for i in x.values():
  print(i)

"""---

- while loop

---
"""

x=5
while(x>0):
  print("piyumal")
  x=x-1
print("=====")

x=1
while(x<20):
  y=x%2
  if(y==0):
    print(x,"is even number.")
  x+=1
print("========")

for i in range(5):
  if(i==3):
    continue  # 3 is not print
  print(i)
  i+=1
print("--------")

for i in range(5):
  if(i==3):
    break  # loop ekama break vela yanava
  print(i)
  i+=1
print("--------")
