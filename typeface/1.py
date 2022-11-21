n  = int(input())
res = ""
sign='-' if n< 0 else ''
n=abs(n)
while n>=3:
    res+=str(n%3)
    n = n//3
res = res[::-1]
res =  str(n)+res
print(res)