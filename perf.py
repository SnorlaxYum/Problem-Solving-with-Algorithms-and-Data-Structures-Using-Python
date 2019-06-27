import time

def perf_wrapper(method,num):
    start = time.time()
    theSum = method(*num)
    end = time.time()
    return theSum, end-start

def sumOfN(n):
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    return theSum

def sumOfN_op(n):
    theSum = n * (n + 1) / 2
    return theSum

def sum_perf_check(method, num):
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % perf_wrapper(method,num))

print("Before the algorithm is optimized:")
check_set=[10**n for n in range(2,8)]
for num in check_set:
    sum_perf_check(sumOfN,[num])

print("After the algorithm is optimized:")
for num in check_set:
    sum_perf_check(sumOfN_op,[num])
