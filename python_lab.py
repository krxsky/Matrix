## Task 1
minutes_in_week = 7*24*60

## Task 2
remainder_without_mod = 2304811-2304811//47*47

## Task 3
divisible_by_3 = (637 + 909) % 3 == 0

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { _*_ for _ in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**_ for _ in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 5, 6, 7 }
Y1 = { 7, 8, 9 }

## Task 8: enter in the two new sets
X2 = { 2, 4, 8 }
Y2 = { 16, 32, 64 }

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = { x*base*base+y*base+z for x in digits for y in digits for z in digits }

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { x for x in S if x in T }

## Task 11
L_average = sum([20,10,15,75])/len([20,10,15,75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(x) for x in LofL]) # use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [[x,y] for x in ['A','B','C'] for y in [1,2,3]] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [ (i,j,k) for i in S for j in S for k in S if i+j+k == 0 ] 

## Task 15
exclude_zero_list = [ (i,j,k) for i in S for j in S for k in S if i+j+k == 0 and (i,j,k) != (0,0,0) ]

## Task 16
first_of_tuples_list = [ (i,j,k) for i in S for j in S for k in S if i+j+k == 0 and (i,j,k) != (0,0,0) ][0]

## Task 17
L1 = [1,1] # <-- want len(L1) != len(list(set(L1)))
L2 = [3,2] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {x for x in range(100) if x%2 == 1}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [x+y for (x,y) in zip([10,25,40],[1,15,20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [d[k] for d in dlist]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [d[k] if k in d else 'NOT PRESENT' for d in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [d[k] if k in d else 'NOT PRESENT' for d in dlist] # <-- as you do here

## Task 23
square_dict = {k:k*k for k in range(100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {k:k for k in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {x*base*base+y*base+z:[x,y,z] for x in digits for y in digits for z in digits}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { names[x]:d[x] for x in range(len(names)) }

## Task 27
def nextInts(L): return [ x+1 for x in L ]

## Task 28
def cubes(L): return [ x**3 for x in L ] 

## Task 29
def dict2list(dct, keylist): return [ dct[k] for k in keylist ]

## Task 30 
def list2dict(L, keylist): return { k:v for (k,v) in zip(keylist,L) } 

