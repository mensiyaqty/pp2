import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()

print ("Task 1")
print (re.findall("a.*b", s))

print ("Task 2")
print (re.findall("a.*bb+|abbb+", s))

print ("Task 3")
print (re.findall("[a-z]_+[a-z]+", s))

print ("Task 4")
print (re.findall(r"[A-Z][a-z]+", s))

print ("Task 5")
print (re.findall(r"a+.b", s))

print ("Task 6")
print (re.sub(r"[., ]",':', s))

print ("Task 7")
print (re.sub(r"_",'', s))

print ("Task 8")
print (re.findall(r"[A-Z][^A-Z]*", s))

print ("Task 9")
print (re.findall(r"[A-Z][a-z]*", s))

print ("Task 10")
print (re.sub(r"[A-Z]",'_', s))