#coding=utf-8

def shell_sort(alist):
    gap = len(alist)/2
    print("gap: %s" %gap)
    for i in range(gap, len(alist)):
	while i > 0:
	    if alist[i] < alist[i-gap]:
	    	alist[i], alist[i-gap] = alist[i-gap], alist[i]
	        i -= gap	
	    else:
		break
    return alist
	
if __name__ == '__main__':
    alist = [3, 2, 1, 4, 5, 4, 2, 1]
    print("alist is:  %s  " %(alist))
    print("sorted is: %s" %shell_sort(alist))
    alist2 = [10, 100, 2, 5, 9, 21, 49, 300, 41]
    print(alist2)
    print(shell_sort(alist2))


