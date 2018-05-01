

def bubble_sort(alist):
    for i in range(len(alist)-1):
	for j in range(i+1, len(alist)):
	    if alist[i] > alist[j]:
		a = alist[j]
		alist[j] = alist[i]
		alist[i] = a
    return alist
	
if __name__ == '__main__':
    alist = [3, 2, 1, 4, 5, 4, 2, 1]
    print("alist is:  %s  " %(alist))
    print("sorted is: %s" %bubble_sort(alist))
    alist2 = [10, 100, 2, 5, 9, 21, 49, 300, 41]
    print(alist2)
    print(bubble_sort(alist2))
