#coding=utf-8

def shell_sort(alist):
    for i in range(1, len(alist)):
	if alist[i-1] > alist[i]:
	    pos = i
	    temp = alist[i]
	    while pos>0 and alist[pos-1] > temp:
		alist[pos] = alist[pos-1]
		pos -= 1
	    alist[pos] = temp
    return alist
	
if __name__ == '__main__':
    alist = [3, 2, 1, 4, 5, 4, 2, 1]
    print("alist is:  %s  " %(alist))
    print("sorted is: %s" %shell_sort(alist))
    alist2 = [10, 100, 2, 5, 9, 21, 49, 300, 41]
    print(alist2)
    print(shell_sort(alist2))


