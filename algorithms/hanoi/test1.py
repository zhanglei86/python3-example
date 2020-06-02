#coding=utf-8

#def move(n,a,b,c): if n == 1: print(a, '-->', c) else:
# 如果把参数名称该变一下更便于理解
# 参数：f代表from, buffer代表缓冲区，to代表目标区
#
def move(n,f,buffer,to):
    if n == 1:
        #print('Move',n,'from',f,'to',to)
        print(f, '-->', to)
    else:
        # 1.移动n-1个圆盘到B,C为缓冲区
        # 所以参数是(a,c,b)a移动到b  a是需要移动的圆盘，b是目标位置，c是缓冲区
        move(n-1,f,to,buffer)

        # 2.移动1个圆盘到目标区(最大的圆盘)
        # a移动到c
        move(1,f,buffer,to)

        # 3.移动缓冲区的圆盘到目标区(剩下的圆盘)
        # b移动到c
        move(n-1,buffer,f,to)

#
if __name__ == '__main__':
    print '--1pcs---------------------------------'
    move(1,'A','B','C')
    print '\n','--2pcs---------------------------------'
    move(2,'A','B','C')
    print '\n','--3pcs---------------------------------'
    move(3,'A','B','C')
    print '\n','--4pcs---------------------------------'
    move(4,'A','B','C')
    print '\n','--5pcs---------------------------------'
    move(5,'A','B','C')
