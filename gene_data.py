import numpy as np
import arff

def target_funtion(max,min):
    da=[]
    for j in range(351):
        for i in range(0,34):
            a1=np.random.random_integers(0,1)
            a2=0
            a3=np.random.uniform(min[i], max[i])
            a4=np.random.uniform(min[i],max[i])
            a5=np.random.uniform(min[i],max[i])
            a6=np.random.uniform(min[i],max[i])
            a7=np.random.uniform(min[i],max[i])
            a8=np.random.uniform(min[i],max[i])
            a9=np.random.uniform(min[i], max[i])
            a10=np.random.uniform(min[i],max[i])
            a11=np.random.uniform(min[i],max[i])
            a12=np.random.uniform(min[i],max[i])
            a13=np.random.uniform(min[i],max[i])
            a14=np.random.uniform(min[i], max[i])
            a15=np.random.uniform(min[i],max[i])
            a16=np.random.uniform(min[i],max[i])
            a17=np.random.uniform(min[i],max[i])
            a18=np.random.uniform(min[i],max[i])
            a19=np.random.uniform(min[i],max[i])
            a20=np.random.uniform(min[i],max[i])
            a21=np.random.uniform(min[i],max[i])
            a22=np.random.uniform(min[i],max[i])
            a23=np.random.uniform(min[i],max[i])
            a24=np.random.uniform(min[i],max[i])
            a25=np.random.uniform(min[i],max[i])
            a26=np.random.uniform(min[i],max[i])
            a27=np.random.uniform(min[i],max[i])
            a28=np.random.uniform(min[i],max[i])
            a29=np.random.uniform(min[i],max[i])
            a30=np.random.uniform(min[i],max[i])
            a31=np.random.uniform(min[i],max[i])
            a32=np.random.uniform(min[i],max[i])
            a33=np.random.uniform(min[i],max[i])
            a34=np.random.uniform(min[i],max[i])
            a35=np.random.random_integers(0,1)
        if(a35==1):
            da.append([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,'g'])
        else:
            da.append([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,'b'])

    obj = {
        'description': u'',
        'relation': 'test',
        'attributes': [
            ('a01', 'REAL'),
            ('a02', 'REAL'),
            ('a03', 'REAL'),
            ('a04', 'REAL'),
            ('a05', 'REAL'),
            ('a06', 'REAL'),
            ('a07', 'REAL'),
            ('a08', 'REAL'),
            ('a09', 'REAL'),
            ('a10', 'REAL'),
            ('a11', 'REAL'),
            ('a12', 'REAL'),
            ('a13', 'REAL'),
            ('a14', 'REAL'),
            ('a15', 'REAL'),
            ('a16', 'REAL'),
            ('a17', 'REAL'),
            ('a18', 'REAL'),
            ('a19', 'REAL'),
            ('a20', 'REAL'),
            ('a21', 'REAL'),
            ('a22', 'REAL'),
            ('a23', 'REAL'),
            ('a24', 'REAL'),
            ('a25', 'REAL'),
            ('a26', 'REAL'),
            ('a27', 'REAL'),
            ('a28', 'REAL'),
            ('a29', 'REAL'),
            ('a30', 'REAL'),
            ('a31', 'REAL'),
            ('a32', 'REAL'),
            ('a33', 'REAL'),
            ('a34', 'REAL'),
            ('class', ['b','g']),
        ],
        'data': da,
    }
    arff.dump(obj,open('test.arff','w'))




dir_name = 'data/'
fname='ionosphere.arff'
dataset = arff.load(open(dir_name + fname),'r')
data = np.array(dataset['data'])
data_t = np.array(dataset['data']).T
col_min =[]
col_max =[]
man_table=[]
euc_table=[]
for i in range(0,data_t.shape[0]):
    col_min.append(min(data_t[i]))
    col_max.append(max(data_t[i]))
target_funtion(col_max,col_min)