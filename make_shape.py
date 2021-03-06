import numpy as np
import math  as ma
import time  as ti
#initialize calculation time
print('Now, making shape...')
start_time=ti.time()
###############################################################################
#define function###############################################################
###############################################################################
def init_1d_list(num):
    var=[]
    for i in range(num):
        var.append(0)
    return var
def write_list(var1,var2):
    var2=map(str,var2)
    var2=' '.join(var2)
    var1.write(var2); var1.write('\n');
    return var1
def rotate_x(x_tmp,y_tmp,z_tmp,rot_s):
    x_o=ma.cos(rot_s[2]) \
        *( ma.cos(rot_s[1])*x_tmp-ma.sin(rot_s[1]) \
        *(ma.cos(rot_s[0])*z_tmp-ma.sin(rot_s[0])*y_tmp) ) \
        +ma.sin(rot_s[2]) \
        *(ma.sin(rot_s[0])*z_tmp+ma.cos(rot_s[0])*y_tmp) 
    return x_o
def rotate_y(x_tmp,y_tmp,z_tmp,rot_s):
    y_o=-ma.sin(rot_s[2]) \
        *( ma.cos(rot_s[1])*x_tmp-ma.sin(rot_s[1]) \
        *(ma.cos(rot_s[0])*z_tmp-ma.sin(rot_s[0])*y_tmp) ) \
        +ma.cos(rot_s[2]) \
        *(ma.sin(rot_s[0])*z_tmp+ma.cos(rot_s[0])*y_tmp) 
    return y_o
def rotate_z(x_tmp,y_tmp,z_tmp,rot_s):
    z_o=ma.sin(rot_s[1])*x_tmp \
        +ma.cos(rot_s[1]) \
        *(ma.cos(rot_s[0])*z_tmp-ma.sin(rot_s[0])*y_tmp)
    return z_o
###############################################################################
#load input file###############################################################
###############################################################################
#set maximum and initialize variables
n_s_max=200+1 #+1 is introduced to ensure consistency with the input.
al=0, 0, 0; dl=0, 0, 0; n_s=0; yn_periodic='n';
yn_copy_x='n'; yn_copy_y='n'; yn_copy_z='n';
output='cube'; rot_type='radian';
typ_s=init_1d_list(n_s_max)
id_s=init_1d_list(n_s_max)
inf_s=np.zeros((n_s_max,10+1)) #+1 is introduced to ensure consistency with the input.
ori_s=np.zeros((n_s_max,3))
rot_s=np.zeros((n_s_max,3))
adj_err=1e-6
#load input file
f = open('shape.inp')
tmp_inp = f.readlines()
f.close()
tmp_inp = [s.replace('d', 'e') for s in tmp_inp]
tmp_inp = [s.replace('al_em','al') for s in tmp_inp]
tmp_inp = [s.replace('el_em','dl') for s in tmp_inp]
tmp_inp = [s.replace('yn_perioeic','yn_periodic') for s in tmp_inp]
tmp_inp = [s.replace('ie_s','id_s') for s in tmp_inp]
tmp_inp = [s.replace('eegree','degree') for s in tmp_inp]
tmp_inp = [s.replace('raeian','radian') for s in tmp_inp]
tmp_inp = [s.replace('ellipsoie','ellipsoid') for s in tmp_inp]
tmp_inp = [s.replace('cylineer','cylinder') for s in tmp_inp]
tmp_inp = [s.replace('(','[') for s in tmp_inp]
tmp_inp = [s.replace(')',']') for s in tmp_inp]
tmp_inp = [s.replace('\n','') for s in tmp_inp]
tmp_inp = [s.replace('\r','') for s in tmp_inp]
for i in range(len(tmp_inp)):
    exec(tmp_inp[i])
del tmp_inp, i
al=list(al); dl=list(dl);
###############################################################################
#set coordinate################################################################
###############################################################################
#dtermine odd or even and set g_num
g_num=init_1d_list(3); g_type=init_1d_list(3);
for i in range(3):
    g_num[i]=int(al[i]/dl[i]+1e-12)
    if int(al[i]/dl[i]+1e-12)%2==1:
        g_type[i]='odd'
    else:
        g_type[i]='even'
del i
#set coo
coo=np.zeros((3,max(g_num)))
for i in range(3):
    for j in range(g_num[i]):
        if yn_periodic=='n':
            if g_type[i]=='odd':
                coo[i,j]=(j-(g_num[i]-1)/2)*dl[i]
            elif g_type[i]=='even':
                coo[i,j]=(j-g_num[i]/2+0.5)*dl[i]
        elif yn_periodic=='y':
            coo[i,j]=j*dl[i]
del i, j
#translate to radian
if rot_type=='degree':
    rot_s[:,:]=rot_s[:,:]/360*2*ma.pi
###############################################################################
#make move matrix##############################################################
###############################################################################
#dtermine copy number
copy_num=init_1d_list(3);
if yn_copy_x=='y': copy_num[0]=3;
else             : copy_num[0]=1;
if yn_copy_y=='y': copy_num[1]=3;
else             : copy_num[1]=1;
if yn_copy_z=='y': copy_num[2]=3;
else             : copy_num[2]=1;
l_max=copy_num[0]*copy_num[1]*copy_num[2]
#make move matrix
move_x=np.zeros((n_s_max,l_max))
move_y=np.zeros((n_s_max,l_max))
move_z=np.zeros((n_s_max,l_max))
for n in range(1,n_s+1): #+1 is introduced to ensure consistency with the input.
    l=0;
    for i in range(copy_num[0]):
        for j in range(copy_num[1]):
            for k in range(copy_num[2]):
                ip_x=i; ip_y=j; ip_z=k;
                if yn_copy_x=='y': ip_x=ip_x-1;
                if yn_copy_y=='y': ip_y=ip_y-1;
                if yn_copy_z=='y': ip_z=ip_z-1;
                x_tmp=al[0]*ip_x
                y_tmp=al[1]*ip_y
                z_tmp=al[2]*ip_z
                move_x[n,l]=rotate_x(x_tmp,y_tmp,z_tmp,rot_s[n,:])
                move_y[n,l]=rotate_y(x_tmp,y_tmp,z_tmp,rot_s[n,:])
                move_z[n,l]=rotate_z(x_tmp,y_tmp,z_tmp,rot_s[n,:])
                l=l+1
del n, i, j, k, l, ip_x, ip_y, ip_z, x_tmp, y_tmp, z_tmp
###############################################################################
#make shape####################################################################
###############################################################################
shape=np.zeros((g_num[0],g_num[1],g_num[2]))
cal_tmp=0
for n in range(1,n_s+1): #+1 is introduced to ensure consistency with the input.
    for i in range(g_num[0]):
        for j in range(g_num[1]):
            for k in range(g_num[2]):
                #move origin
                x_tmp=coo[0,i]-ori_s[n,0]
                y_tmp=coo[1,j]-ori_s[n,1]
                z_tmp=coo[2,k]-ori_s[n,2]
                #rotation
                x_o=rotate_x(x_tmp,y_tmp,z_tmp,rot_s[n,:])
                y_o=rotate_y(x_tmp,y_tmp,z_tmp,rot_s[n,:])
                z_o=rotate_z(x_tmp,y_tmp,z_tmp,rot_s[n,:])
                for l in range(l_max): #this loop is used for copy
                    #determine point
                    x=x_o+move_x[n,l]
                    y=y_o+move_y[n,l]
                    z=z_o+move_z[n,l]
                    #determine shape
                    if typ_s[n]=='ellipsoid':
                        cal_tmp=(x/(inf_s[n,1]/2))**2 \
                                + (y/(inf_s[n,2]/2))**2 \
                                + (z/(inf_s[n,3]/2))**2
                        if cal_tmp<=1:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='half-ellipsoid':
                        cal_tmp=(x/(inf_s[n,1]/2))**2 \
                                + (y/(inf_s[n,2]/2))**2 \
                                + (z/inf_s[n,3])**2
                        if cal_tmp<=1 and z>=-adj_err:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='elliptic-cylinder':
                        cal_tmp=(x/(inf_s[n,1]/2))**2 \
                                + (y/(inf_s[n,2]/2))**2
                        if cal_tmp<=1 and z>=-inf_s[n,3]/2 and z<=inf_s[n,3]/2:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='triangular-cylinder':
                        if x>=-inf_s[n,1]/2 and x<=inf_s[n,1]/2 \
                        and y>=-inf_s[n,2]/3  \
                        and y<= inf_s[n,2]/(inf_s[n,1]/2)*x + inf_s[n,2]*2/3 \
                        and y<=-inf_s[n,2]/(inf_s[n,1]/2)*x + inf_s[n,2]*2/3 \
                        and z>=-inf_s[n,3]/2 and z<=inf_s[n,3]/2:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='rectangular-cylinder':
                        if x>=-inf_s[n,1]/2 and x<=inf_s[n,1]/2 \
                        and y>=-inf_s[n,2]/2 and y<=inf_s[n,2]/2 \
                        and z>=-inf_s[n,3]/2 and z<=inf_s[n,3]/2:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='elliptic-cone':
                        if inf_s[n,3]-z!=0:
                            cal_tmp=(x/( inf_s[n,1]/2*(inf_s[n,3]-z)/inf_s[n,3] ))**2 \
                                    + (y/( inf_s[n,2]/2*(inf_s[n,3]-z)/inf_s[n,3] ))**2
                        else:
                            cal_tmp=10
                        if cal_tmp<=1 and z>=-adj_err and z<=inf_s[n,3]:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='triangular-cone':
                        if x>=-inf_s[n,1]/2*(inf_s[n,3]-z)/inf_s[n,3] \
                        and x<=inf_s[n,1]/2*(inf_s[n,3]-z)/inf_s[n,3] \
                        and y>=-inf_s[n,2]/3*(inf_s[n,3]-z)/inf_s[n,3] \
                        and y<= inf_s[n,2]/(inf_s[n,1]/2)*x \
                                +inf_s[n,2]*2/3*(inf_s[n,3]-z)/inf_s[n,3] \
                        and y<=-inf_s[n,2]/(inf_s[n,1]/2)*x \
                                +inf_s[n,2]*2/3*(inf_s[n,3]-z)/inf_s[n,3] \
                        and z>=-adj_err and z<=inf_s[n,3]:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='rectangular-cone':
                        if x>= -inf_s[n,1]/2*(inf_s[n,3]-z)/inf_s[n,3] \
                        and x<= inf_s[n,1]/2*(inf_s[n,3]-z)/inf_s[n,3] \
                        and y>=-inf_s[n,2]/2*(inf_s[n,3]-z)/inf_s[n,3] \
                        and y<= inf_s[n,2]/2*(inf_s[n,3]-z)/inf_s[n,3] \
                        and z>=-adj_err and z<=inf_s[n,3]:
                            shape[i,j,k]=id_s[n]
                    elif typ_s[n]=='elliptic-ring':
                        cal_tmp=(x/(inf_s[n,1]/2))**2 \
                                + (y/(inf_s[n,2]/2))**2
                        if cal_tmp<=1 and z>=-inf_s[n,3]/2 and z<=inf_s[n,3]/2:
                            cal_tmp=(x/(inf_s[n,4]/2))**2 \
                                    + (y/(inf_s[n,5]/2))**2
                            if cal_tmp>=1:
                                shape[i,j,k]=id_s[n]
del cal_tmp, n, i, j, k, l, l_max, x_tmp, y_tmp, z_tmp, \
    x_o, y_o, z_o, x, y, z
###############################################################################
#output########################################################################
###############################################################################
if output == 'cube':
    #set basic data
    f = open('./shape.cube', mode='w')
    f.write('An input shape described in a cube file.\n')
    f.write('A hydrogen atom is used to set the origin of the model.\n')
    write_list(f,[1,coo[0,0],coo[1,0],coo[2,0]])
    write_list(f,[g_num[0],dl[0],0,0])
    write_list(f,[g_num[1],0,dl[1],0])
    write_list(f,[g_num[2],0,0,dl[2]])
    write_list(f,[1,1,0,0,0])
    #output shape data
    n_write=0; i=0; j=0; k=0;
    inp_tmp=init_1d_list(6);
    for n in range(g_num[0]*g_num[1]*g_num[2]):
        inp_tmp[n_write]=int(shape[i,j,k])
        #output and update n
        if n_write>0 and (n_write%(6-1))==0:
            write_list(f,inp_tmp);
            n_write=0
        else:
            n_write=n_write+1
        #update k 
        k=k+1
        if k==g_num[2]: k=0
        #update j
        if k==0: j=j+1
        if j==g_num[1]: j=0
        #update i
        if k==0 and j==0: i=i+1
        #final output for special case
        if n==(g_num[0]*g_num[1]*g_num[2]-1) and n_write>0:
            inp_tmp2=init_1d_list(n_write);
            for n2 in range(n_write):
                inp_tmp2[n2]=inp_tmp[n2]
            write_list(f,inp_tmp2);
            del inp_tmp2, n2
    del n, n_write, i, j, k, inp_tmp
    f.close()
elif output == 'mp':
    #set basic data
    f = open('./shape.mp', mode='w')
    f.write('&macroscopic_system\n')
    write_list(f,['  lg_numx =',g_num[0]])
    write_list(f,['  lg_numy =',g_num[1]])
    write_list(f,['  lg_numz =',g_num[2]])
    inp_tmp=init_1d_list(n_s+1)
    for i in range(g_num[0]):
        for j in range(g_num[1]):
            for k in range(g_num[2]):
                if shape[i,j,k] != 0:
                    for n in range(1,n_s+1):
                        if shape[i,j,k] == n:
                            inp_tmp[n]=inp_tmp[n]+1
    for n in range(1,n_s+1):
        write_list(f,['  nmacro('+str(n)+') =',inp_tmp[n]])
    del n
    f.write('/\n')
    #output shape data
    del i, j, k
    inp_tmp=0
    for i in range(g_num[0]):
        for j in range(g_num[1]):
            for k in range(g_num[2]):
                if shape[i,j,k] != 0:
                    inp_tmp=inp_tmp+1
                    write_list(f,[inp_tmp,i+1,j+1,k+1,int(shape[i,j,k])])
                    #+1 is introduced to ensure consistency with the output.
    del inp_tmp, i, j, k 
    f.close()
###############################################################################
#fin###########################################################################
###############################################################################
#output calculation time
elapsed_time = ti.time() - start_time
print ("elapsed time:{0}".format(elapsed_time) + "[sec]")
#delete all variables
del al, dl, n_s, yn_periodic, yn_copy_x, yn_copy_y, yn_copy_z, \
    output, rot_type, typ_s, id_s, inf_s, ori_s, rot_s, \
    adj_err, n_s_max, g_num, g_type, coo, \
    copy_num, move_x, move_y, move_z, \
    shape, start_time, elapsed_time
del f, init_1d_list, write_list, rotate_x, rotate_y, rotate_z
print('Finish!')





































