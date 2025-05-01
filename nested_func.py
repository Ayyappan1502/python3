def passed_a(a):
    
    def addr(b):
        return a+b

    def product(b,c):
        return a*b*c
    
    return  addr , product
addr,product = passed_a(10)

print(addr(9))
print(product(6,2))