##Code which calculates forward kinematics
## 6.123234e-17 or a similar number of that kind is very small number so is close to 0(you may get this in the output matrix)
import math
import numpy as np

# angle = math.radians(angle)
# return np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math

def transformation_matrix(dh_table,i):
    ##c==cos,s==sin,cs==variation of cos and sine,cal=c_alpha
    c=math.cos(dh_table[i][3])
    s= math.sin(dh_table[i][3])
    a=dh_table[i][1]
    cs=math.cos(dh_table[i][0])*s
    cc=math.cos(dh_table[i][0])*c
    sal=math.sin(dh_table[i][0])
    ds=dh_table[i][2]*math.sin(dh_table[i][0])
    ss = math.sin(dh_table[i][0]) * s
    sc = math.sin(dh_table[i][0]) * c
    cal=math.cos(dh_table[i][0])
    dc = dh_table[i][2] * math.cos(dh_table[i][0])

    return np.array([[c,-s,0,a],[cs,cc,-sal,-ds],[ss,sc,cal,dc],[0,0,0,1]])

print("Transformation matrix and Position of end effector of a gripper\nRows==dof==6,Columns==4")
print("Enter dh_table[alpha,a,d,theta]-represents column(jth parameter)")
dh_table=np.zeros(shape=(6,4))
for i in range(6):
    for j in range(4):
       val=int(input("Enter parameter of "+str(i+1)+" th row and "+str(j+1)+" th column: "))
       if(j==0 or j==3):
           val=math.radians(val)
       dh_table[i][j]=val

matrices=[]
for i in range(6):
    matrices.append(transformation_matrix(dh_table,i))

##transformathon matrix t(superscript 0,subscript 1)::(for verification)
print(matrices[1])

m=matrices[0]
for i in range(6):
    if(i+1<=5):
        m=np.dot(m,matrices[i+1])

print("Final transformation matrix is: \n",m)
end_effector=m[0:4,3]
print("Final coordinates of end effector: ",end_effector)




