import arff
import numpy as np
import heapq


def man_distance_normalized(a1,a2,mmin,mmax):
    sum=0
    for att in range(0,len(a2)-1):
        if mmax[att]!=mmin[att]:
            ar1 = (a1[att]-mmin[att])/(mmax[att]-mmin[att])
            ar2 = (a2[att]-mmin[att])/(mmax[att]-mmin[att])
            dis = abs(ar1-ar2)
            sum = sum+dis
    return sum
def man_distance(a1,a2):
    sum=0
    for att in range(0,len(a2)-1):
            dis  = abs(a2[att]-a1[att])
            sum =dis+sum
    return sum
def euclidean_distance_normalized(a1,a2,mmin,mmax):
    sum=0
    for att in range(0,len(a2)-1):
        if mmax[att]!=mmin[att]:
            ar1 = (a1[att]-mmin[att])/(mmax[att]-mmin[att])
            ar2 = (a2[att]-mmin[att])/(mmax[att]-mmin[att])
            dis = (ar1-ar2)**2
            sum = sum+dis
    return sum**(0.5)
def euclidean_distance(a1,a2):
    sum=0.0
    for att in range(0,len(a2)-1):
            dis = (a2[att]-a1[att])**2
            sum = sum+dis
    return sum**0.5







dir_name = 'data/'
filename = 'ionosphere.arff'
dataset =arff.load(open(dir_name+filename),'r')
data = np.array(dataset['data'])
data_t= np.array(dataset['data']).T

print("num of data is: "+str(data.shape[0]))
kmin=5
kmax=7
## data is the orginal data and only access it when use testdata
## tempdata is train data that delete data[m]



print("start for KNN Manhattan and Euclidean")

bestEM=1
bestEE=1
bestKsofarM=0
bestKsofarE=0
for k in range(kmin,kmax):
    totalbadM=0
    totalbadE=0
    for m in range(0,data.shape[0]):
        col_min =[]
        col_max =[]
        man_table=[]
        euc_table=[]
        weight_man=[]
        weight_euc=[]
        tempdata = data
        tempdata_t=data_t
        dele_table=[]
        dele_table.append(m)
        dele_table=list(set(dele_table))
        tempdata = np.delete(data,dele_table,0)
        tempdata_t=np.array(data).T


        test=data[m]
        for j in range(0,tempdata.shape[0]):
            man_table.append(man_distance(test,tempdata[j]))
            euc_table.append(euclidean_distance(test,tempdata[j]))

        min_rr1 = list(map(man_table.index, heapq.nsmallest(k, man_table)))
        min_rr2 = list(map(euc_table.index, heapq.nsmallest(k, euc_table)))
        g1=0
        b1=0
        ans1=-1
        g2=0
        b2=0
        ans2=-1


        for c in min_rr1:
            if tempdata[c][-1]==1:
                g1=g1+1
            else:
                b1=b1+1
        if g1>b1:
            ans1=1
        else:
            ans1=0


        for l in min_rr2:
            if tempdata[l][-1]==1:
                g2=g2+1
            else:
                b2=b2+1
        if g2>b2:
            ans2=1
        else:
            ans2=0
        if ans1!=data[m][-1]:
            totalbadM=totalbadM+1
        if ans2!=data[m][-1]:
            totalbadE=totalbadE+1        


    errorm=totalbadM/(data.shape[0]-1)

    if bestEM > errorm:
        bestKsofarM=k
        bestEM=errorm
    errore=totalbadE/(data.shape[0]-1)

    if bestEE > errore:
        bestKsofarE=k
        bestEE=errore
print(bestEM)
print(bestKsofarM)
print(bestEE)
print(bestKsofarE)








print("start for KNN Manhattan and Euclidean with Normalized")
bestEM=1
bestEE=1
bestKsofarM=0
bestKsofarE=0
for k in range(kmin,kmax):
    totalbadM=0
    totalbadE=0
    for m in range(0,data.shape[0]):
        col_min =[]
        col_max =[]
        man_table=[]
        euc_table=[]
        tempdata = data
        tempdata_t=data_t
        dele_table=[]
        dele_table.append(m)
        dele_table=list(set(dele_table))
        tempdata = np.delete(data,dele_table,0)
        tempdata_t=np.array(data).T

        for i in range(0,tempdata_t.shape[0]-1):
            col_min.append(min(tempdata_t[i]))
            col_max.append(max(tempdata_t[i]))

        test=data[m]
        for j in range(0,tempdata.shape[0]):
            man_table.append(man_distance_normalized(test,tempdata[j],col_min,col_max))
            euc_table.append(euclidean_distance_normalized(test,tempdata[j],col_min,col_max))

        min_rr1 = list(map(man_table.index, heapq.nsmallest(k, man_table)))
        min_rr2 = list(map(euc_table.index, heapq.nsmallest(k, euc_table)))
        g1=0
        b1=0
        ans1=-1
        g2=0
        b2=0
        ans2=-1

        for c in min_rr1:
            if tempdata[c][-1]==1:
                g1=g1+1
            else:
                b1=b1+1
        if g1>b1:
            ans1=1
        else:
            ans1=0


        for l in min_rr2:
            if tempdata[l][-1]==1:
                g2=g2+1
            else:
                b2=b2+1
        if g2>b2:
            ans2=1
        else:
            ans2=0
        if ans1!=data[m][-1]:
            totalbadM=totalbadM+1
        if ans2!=data[m][-1]:
            totalbadE=totalbadE+1        


    errorm=totalbadM/(data.shape[0]-1)

    if bestEM > errorm:
        bestKsofarM=k
        bestEM=errorm
    errore=totalbadE/(data.shape[0]-1)

    if bestEE > errore:
        bestKsofarE=k
        bestEE=errore
print(bestEM)
print(bestKsofarM)
print(bestEE)
print(bestKsofarE)




print("start for WNN Manhattan and Euclidean")

bestEM=1
bestEE=1
bestKsofarM=0
bestKsofarE=0
for k in range(kmin,kmax):
    totalbadM=0
    totalbadE=0
    for m in range(0,data.shape[0]):
        col_min =[]
        col_max =[]
        man_table=[]
        euc_table=[]
        tempdata = data
        tempdata_t=data_t
        dele_table=[]
        dele_table.append(m)
        dele_table=list(set(dele_table))
        tempdata = np.delete(data,dele_table,0)
        tempdata_t=np.array(data).T

        test=data[m]
        for j in range(0,tempdata.shape[0]):
            man_table.append(man_distance(test,tempdata[j]))
            euc_table.append(euclidean_distance(test,tempdata[j]))

        min_rr1 = list(map(man_table.index, heapq.nsmallest(k, man_table)))
        min_rr2 = list(map(euc_table.index, heapq.nsmallest(k, euc_table)))


        g1=0
        b1=0
        ans1=-1
        g2=0
        b2=0
        ans2=-1

        for ii in min_rr1:
            if man_table[ii]!=0:
                if tempdata[ii][-1]==1:
                    g1=g1+1/(man_table[ii]**2)
                else:
                    b1=b1+1/(man_table[ii]**2)

        for iii in min_rr2:
            if euc_table[iii]!=0:
                if tempdata[iii][-1]==1:
                    g2=g2+1/(euc_table[iii]**2)
                else:
                    b2=b2+1/(euc_table[iii]**2)


        if g1>b1:
            ans1=1
        else:
            ans1=0
        if g2>b2:
            ans2=1
        else:
            ans2=0
            
        if ans1!=data[m][-1]:
            totalbadM=totalbadM+1
        if ans2!=data[m][-1]:
            totalbadE=totalbadE+1        


    errorm=totalbadM/(data.shape[0]-1)

    if bestEM > errorm:
        bestKsofarM=k
        bestEM=errorm
    errore=totalbadE/(data.shape[0]-1)

    if bestEE > errore:
        bestKsofarE=k
        bestEE=errore
print(bestEM)
print(bestKsofarM)
print(bestEE)
print(bestKsofarE)





print("start for WNN Manhattan and Euclidean with Normalized")
bestEM=1
bestEE=1
bestKsofarM=0
bestKsofarE=0
for k in range(kmin,kmax):
    totalbadM=0
    totalbadE=0
    for m in range(0,data.shape[0]):
        col_min =[]
        col_max =[]
        man_table=[]
        euc_table=[]
        tempdata = data
        tempdata_t=data_t
        dele_table=[]
        dele_table.append(m)
        dele_table=list(set(dele_table))
        tempdata = np.delete(data,dele_table,0)
        tempdata_t=np.array(data).T

        for i in range(0,tempdata_t.shape[0]-1):
            col_min.append(min(tempdata_t[i]))
            col_max.append(max(tempdata_t[i]))

        test=data[m]
        for j in range(0,tempdata.shape[0]):
            man_table.append(man_distance_normalized(test,tempdata[j],col_min,col_max))
            euc_table.append(euclidean_distance_normalized(test,tempdata[j],col_min,col_max))

        min_rr1 = list(map(man_table.index, heapq.nsmallest(k, man_table)))
        min_rr2 = list(map(euc_table.index, heapq.nsmallest(k, euc_table)))


        g1=0
        b1=0
        ans1=-1
        g2=0
        b2=0
        ans2=-1

        for ii in min_rr1:
            if man_table[ii]!=0:
                if tempdata[ii][-1]==1:
                    g1=g1+1/(man_table[ii]**2)
                else:
                    b1=b1+1/(man_table[ii]**2)

        for iii in min_rr2:
            if euc_table[iii]!=0:
                if tempdata[iii][-1]==1:
                    g2=g2+1/(euc_table[iii]**2)
                else:
                    b2=b2+1/(euc_table[iii]**2)



        if g1>b1:
            ans1=1
        else:
            ans1=0
        if g2>b2:
            ans2=1
        else:
            ans2=0
            
        if ans1!=data[m][-1]:
            totalbadM=totalbadM+1
        if ans2!=data[m][-1]:
            totalbadE=totalbadE+1        


    errorm=totalbadM/(data.shape[0]-1)

    if bestEM > errorm:
        bestKsofarM=k
        bestEM=errorm
    errore=totalbadE/(data.shape[0]-1)

    if bestEE > errore:
        bestKsofarE=k
        bestEE=errore
print(bestEM)
print(bestKsofarM)
print(bestEE)
print(bestKsofarE)



