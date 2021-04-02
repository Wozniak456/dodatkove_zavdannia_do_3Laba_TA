import random
import collections
from pylab import figure, show
from math import log
import numpy as np
import math
def generate_data(n, gen_typ):
    a = [i+1 for i in range(n)]
    random.shuffle(a)
    return a


def insertion_sort(a):
    k = 0
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
            k += 1
        a[j+1] = key
        k += 1
    return [a, k] 

def plot_data(data, logarithmic=False, oneplot=False):
    fig = figure(1)
    num = len(data)
    colors = ['r','b','g']
    markers = ['s','o','x']
    lines = ['-','--',':']
    if oneplot==True:
        ax = fig.add_subplot(111)
        ax.grid(True)
        i = -1
        line_titles = []
        x_max = y_max = 0
        for label, value in data.items():
            i += 1
            j = -1
            for sort_type, points in value.items():
                j += 1
                od_points = collections.OrderedDict(sorted(points.items()))
                if logarithmic:
                    xs = [(x>0 and log(x,10) or 0) for x in od_points.keys()]
                    ys = [(y>0 and log(y,10) or 0) for y in od_points.values()]
                else:
                    xs = od_points.keys()
                    ys = od_points.values()
                xs.insert(0,0)
                x_max = max(x_max, max(xs))
                ys.insert(0,0)
                y_max = max(y_max, max(ys))
                ax.plot(xs, ys, colors[j%num]+markers[j%num]+lines[i%num], label=sort_type )
                line_titles.append(sort_type+' '+label)
        ax.set_xlim( (0, x_max*1.1) )
        ax.set_ylim( (0, y_max*1.1) )
        ax.legend(line_titles, loc=4)
    else:
        i = 0
        for label, value in data.items():
            i += 1
            ax = fig.add_subplot(num,1,i)
            ax.grid(True)
            ax.set_title(label)
            j = -1
            x_max = y_max = 0
            for sort_type, points in value.items():
                j += 1
                od_points = collections.OrderedDict(sorted(points.items()))
                if logarithmic:
                    xs = [log(x,10) for x in od_points.keys()]
                    ys = [log(y,10) for y in od_points.values()]
                else:
                    xs = od_points.keys()
                    ys = od_points.values()
                xs.insert(0,0)
                x_max = max(x_max, max(xs))
                ys.insert(0,0)
                y_max = max(y_max, max(ys))
                ax.plot(xs, ys, colors[j%num]+markers[j%num]+'-', label=sort_type )
            ax.set_xlim( (0, x_max*1.1) )
            ax.set_ylim( (0, y_max*1.1) )
            ax.legend(loc=4)
    show()

def Merge_sort(A):
    n=len(A)
    if n==1:
        return (A,0)
    else:
        (L,x)=Merge_sort(A[:int(n/2)])
        (R,y)=Merge_sort(A[int(n/2):])
        (A, z)=Merge(A, L, R)
        return (A, x+y+z)
def Merge(A, L, R):
    n1=len(L)
    n2=len(R)
    L=np.append(L,math.inf)
    R = np.append(R, math.inf)
    i=0
    j=0
    c=0 # counter
    for k in range(len(A)):
        c+=1
        if L[i] <= R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j+=1
    return(A,c)

def Hybrid_Merge_sort(A):
    n=len(A)
    if n <=10:
        return insertion_sort(A)
    else:
        (L, x) = Hybrid_Merge_sort(A[:int(n / 2)])
        (R, y) = Hybrid_Merge_sort(A[int(n / 2):])
        (A, z) = Merge(A, L, R)
        return (A, x + y + z)







