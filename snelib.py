import numpy as np
import math as m

def dir_cosine(a ,b, c):
    s1=np.arccos(a/m.sqrt(a**2+b**2+c**2))
    s2=np.arccos(b/m.sqrt(a**2+b**2+c**2))
    s3=np.arccos(c/m.sqrt(a**2+b**2+c**2))
    return s1,s2,s3


def cross_product(a,b):
    s=0
    for i in range(0,3):
        s=s+(a[i]*b[i])
    return s


def dist_points(a,b):
    s1=0
    for i in range(0,3):
        s1=s1+((a[i]-b[i])**2)
        s2=m.sqrt(s1)
    return s2


def angle_lines(a,b):
    s=0
    s2=0
    s1=0
    for i in range(3):
        s=cross_product(a,b)
        s1=s1+((a[i]-b[i])**2)
        s2=m.sqrt(s1)
    return np.arccos(s/s2)


def section(m,n,arr1,arr2,internal):
        arr3=[]
        i=0
        if internal==True:
                while i<3:
                        p=(m*arr2[i]+n*arr1[i])/(m+n)
                        arr3.append(p)
                        i=i+1
        elif internal==False:
                while i<3:
                        p=(m*arr2[i]-n*arr1[i])/(m+n)
                        arr3.append(p)
                        i=i+1
        return arr3
        
                  
