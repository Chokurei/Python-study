1. System:
# bash
export PATH="/home/kaku/anaconda3/bin:$PATH"   
$PATH
# 
which python
ls -l /usr/bin/python
ln -ls /usr/bin/python2.6       /usr/bin/python



#Make a script both importable and executable, name can be replaced
__name__ =='__main__'



2. python basic
#list
##https://docs.python.org/2/tutorial/datastructures.html
from collections import deque
del popleft
stack and queue in list
index = list.index(element)

indexes=[1,30,40,5]
for file_name in [file_names[x] for x in indexes]:

a = [66.25, 333, 333, 1, 1234.5]
a.count(333)
a.insert(2,-1)
a.index(333)
a.remove(333)
a.sort()
a.pop()
a.reverse()
del a[0]

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

#set
##https://docs.python.org/2/tutorial/datastructures.html
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
a = set('abracadabra')
b = set('alacazam')
a - b      a | b        a & b    a ^ b 

#dictionary
tel = {'jack': 4098, 'sape': 4139}
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)
tel['guido'] = 4127
tel['jack']
del tel['sape']
tel.keys()
'guido' in tel

3. modules
#numpy
##https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
b.cumsum()
a[:6:2] = a[0:6:2] = -1000 
np.vstack((a,b)) np.hstack((a,b))
np.column_stack((a,b)) 
##The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to vstack only for 1D arrays:
np.hsplit(a,3) np. hsplit((3,4)) np.vsplit(a,3)
np.random.random((3,3))
a = np.arange(12).reshape(3,4) b = a > 4   a[b]
## The dots (...) represent as many colons as needed to produce a complete indexing tuple. 
x[1,2,...] = x[1,2,:,:,:],

data=np.transpose(data,(0,3,1,2))
data = data.astype('float32')
template.shape[::-1]

data_value = np.delete(data[idx],19)

4. opencv
＃opencv读和保存图片的时候是bgr的顺序 所以要用opencv的话 就要一起用 不会有问题
cv2.imwrite(name,image)# better to save binary images
resized = cv2.resize(img,(32,32), interpolation = cv2.INTER_LINEAR)
cv2.imread(img,0)

imread()
uint8 : 0~255
float : 0~1

#match templete:
http://www.cnblogs.com/xrwang/archive/2010/02/05/MatchTemplate.html
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
res = cv2.matchTemplate(img,template,method)
	
5. os
os.rename(filename, new_filename)
Script_name=os.path.basename(__file__)

6.matplotlib
#当边长为奇数时候 有bug 改用opencv
cmap = 'gray' or 'Greys' are different

7. random
list = random.sample(range(1000),num)

8. print
print("Accuracy: {0:.4f}".format(train_acc))

9.others
from shutil import copyfile
	copyfile(src,file)
# make and write file
script=open(os.path.join(output_file,'Dodge_'+str(idx)+'.txt'),'a')
script.write('1'+'\n')
script.close()
	
10. glob
path = os.path.join('..','data','train',fld,'*jpg')
files = glob.glob(path)

11. sclearn
#K-Folds cross validation iterator
from sklearn.cross_validation import KFold
	kf = KFold(len(X_train), n_folds=n_fold, shuffle=True, random_state=random_state)
	for train_idx, cv_idx in kf: 

12. keras
callbacks = [EarlyStopping(monitor='val_loss', patience=3, verbose=0)]
model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch,
      shuffle=True, verbose=2, validation_data=(X_valid, Y_valid),
      callbacks=callbacks)


model.add(Convolution2D(12,4,4, border_mode='same',trainable=False))

13. pandas
result1 = pd.DataFrame(predictions, columns=['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT'])
result1.loc[:, 'image'] = pd.Series(test_id, index=result1.index)

s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])
s.iloc[:3]
49   NaN
48   NaN
47   NaN
s.loc[:3]
49   NaN
48   NaN
47   NaN
46   NaN
45   NaN
1    NaN
2    NaN
3    NaN


df = pd.DataFrame(np.arange(25).reshape(5,5), 
                      index=list('abcde'),
                      columns=['x','y','z', 8, 9])
Using ix, we can slice the rows by label and the columns by position (note that for the columns, ix default to position-based slicing since the label 4 is not a column name):
df.ix[:'c', :4]
    x   y   z   8
a   0   1   2   3
b   5   6   7   8
c  10  11  12  13

new_dict.setdefault(address, []).append(data_list[idx])

14. csv
with open('result.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(data)
	
with open(filepath,"r") as f:
        reader = csv.reader(f)
        header = next(reader)
    

