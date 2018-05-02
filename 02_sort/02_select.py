#coding=utf-8

def select_sort(alist):
    for i in range(len(alist)-1):
	index = i
	for j in range(i+1, len(alist)):
	    if alist[index] < alist[i]:
		index = j
	alist[i], alist[index] = alist[index], alist[j]
    return alist
	
if __name__ == '__main__':
    alist = [3, 2, 1, 4, 5, 4, 2, 1]
    print("alist is:  %s  " %(alist))
    print("sorted is: %s" %select_sort(alist))
    alist2 = [10, 100, 2, 5, 9, 21, 49, 300, 41]
    print(alist2)
    print(select_sort(alist2))
