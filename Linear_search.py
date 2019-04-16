import time
from matplotlib import pyplot as plt

test_case = [ y for y in range(1000)]
result = []

def search(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i] > e:
            return False
    return False

def test(L):
    for j in range(0,len(L)):
        start = time.time()
        flg = search(L,j)
        end = time.time()
        if flg:
            result.append(end-start)
    return result

def show_it(L,res):
    plt.plot(L,res,color='green',marker='o',linestyle='solid')
    plt.title("Linear Search")
    plt.ylabel('time')
    plt.show()

test(test_case)
show_it(test_case,result)
