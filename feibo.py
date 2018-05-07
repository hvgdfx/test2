

def fun(n):
    if n == 1:
	print(1)
    else:
	print(fun(n-1))

if __name__ == '__main__':
    print(fun(10))
