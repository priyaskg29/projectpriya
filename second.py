from unicodedata import digit


print("Hiii Pantaaaaaaa")
print("python program")
num=1234
rev=0

while num!=0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print(rev)