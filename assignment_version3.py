import arff
import numpy as np
import heapq
def cal_label(data,real,k):
    sum_1=[]
    sum_0=[]
    for i in range(0,len(data)):
            if(real[i][-1]==1):
                sum_1.append(data[i])
            else:
                sum_0.append(data[i])
    #print(sum_1)
    #print(sum_0)
    if(sum(sum_1)>sum(sum_0)):
        return 1
    else:
        return 0
def cal_real_valued(weight,size):
    all=0

    for i in range(size):
        all = all + (weight[i]*data[i][-2])
    return all/sum(weight)
def cal_weight(data):
    wi=[]
    for i in range(0, len(data)):
        if (data[i] == 0):
            wi.append(0)
        else:
            wi.append(1 / (data[i] ** 2))
    return wi
def man_distance(a1,a2,min,max):
    sum=0
    for att in range(0,len(need)):
        ar = (a1[need[att]]-min[att])/(max[att]-min[att])
        dis = abs(a2[need[att]]-ar)
        #dis  = abs(a2[need[att]]-a1[need[att]])
        sum = sum+dis
    return sum
def man_distance_label(a1,a2,min,max):
    sum=0
    for att in range(0,len(a2)):
            #ar = (a1[att]-min[att])/(max[att]-min[att])
            #dis = abs(a2[att]-ar)
            dis  = abs(a2[att]-a1[att])

            sum =dis+sum
    return sum
def euclidean_distance(a1,a2,min,max):
    sum=0
    for att in range(0,len(need)):
        ar = (a1[need[att]] - min[att]) / (max[att] - min[att])
        dis = (a2[att]-ar)**2
        sum = sum+dis
    return sum**0.5
def euclidean_distance_label(a1,a2,min,max):
    sum=0.0
    for att in range(0,len(a1)):
            #ar = (a1[att] - min[att]) / (max[att] - min[att])
            #dis = (a2[att]-ar)**2
            dis = (a2[att]-a1[att])**2
            sum = sum+dis
    return sum**0.5
def show(num):
    if num==0:
        print("b")
    else:
        print("g")

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)
dir_name = 'data/'
filename = 'autos.arff'
dataset =arff.load(open(dir_name+filename),'r')
data = np.array(dataset['data'])
data_t= np.array(dataset['data']).T
dele_table=[]

for col in range(0,data.shape[0]):
    for row in range(0,data_t.shape[0]):
        if((data[col][row])==None):
            dele_table.append(col)

dele_table=list(set(dele_table))

data = np.delete(data,dele_table,0)
data_t=np.array(data).T
col_min =[]
col_max =[]
man_table=[]
euc_table=[]
price_acc=[]
price_acc1=[]
weight_man=[]
weight_euc=[]
need = [0,8,9,10,11,12,15,17,18,19,20,21,22,23,25]
for i in need:
    col_min.append(min(data_t[i]))
    col_max.append(max(data_t[i]))

#for m in range(0,data.shape[0]):
m=154
test=data[m]
for j in range(0,data.shape[0]):
    man_table.append(man_distance_label(test,data[j],col_min,col_max))
    euc_table.append(euclidean_distance_label(test,data[j],col_min,col_max))
weight_man=cal_weight(man_table)
weight_euc=cal_weight(euc_table)
print(cal_real_valued(weight_man,data.shape[0]),data[m][-2])
print(cal_real_valued(weight_euc,data.shape[0]),data[m][-2])
    #min_rr=[]
    #k=4
    #min_rr1 = list(map(man_table.index, heapq.nsmallest(k, man_table)))
    #min_rr2 = list(map(euc_table.index, heapq.nsmallest(k, euc_table)))
    #sum1=0
    #sum2=0
    #for c in min_rr1:
    #    sum1 =sum1+data[i][-2]
    #    if (sum1/k-data[m][-2]<100):
    #        price_acc.append(1)
    #    else:
    #        price_acc.append(0)
    #for l in min_rr2:
    #    sum2 =sum2+data[i][-2]
    #    if (sum2/k-data[m][-2]<100):
    #        price_acc1.append(1)
    #    else:
    #        price_acc1.append(0)
#print(price_acc.count(1)/len(price_acc))
#print(price_acc1.count(1)/len(price_acc1))