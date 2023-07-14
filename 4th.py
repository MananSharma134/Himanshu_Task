
string = "a3b4c5"
for i in range(0, len(string),2):
    a = string[i]
    b = int(string[i+1])
    print(a*b,end="")