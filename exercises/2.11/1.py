from timeit import Timer

the_list = list(range(10000))

for ind in range(10000):
    t = Timer("the_list[%d]" % ind,
        "from __main__ import the_list")
    time = t.timeit(number=1000)
    print("the_list[%d]: %f" % (ind, time))
