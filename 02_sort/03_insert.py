#coding=utf-8

def insert_sort(alist):
    for i in range(1, len(alist)):
	while i > 0:
	    if alist[i] < alist[i-1]:
		alist[i-1], alist[i] = alist[i], alist[i-1]
	    	i -= 1
	    else:
		break
    return alist
	
if __name__ == '__main__':
    alist = [3, 2, 1, 4, 5, 4, 2, 1]
    print("alist is:  %s  " %(alist))
    print("sorted is: %s" %insert_sort(alist))
    alist2 = [10, 100, 2, 5, 9, 21, 49, 300, 41]
    print(alist2)
    print(insert_sort(alist2))


