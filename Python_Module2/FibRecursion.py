def fibrecur(n):
    if n<=1:
        return n
    else:
        return(fibrecur(n-1) + fibrecur(n-2))

nterms = 20

print("fibonacci sequence:")
for i in range(nterms):
    print(fibrecur(i))