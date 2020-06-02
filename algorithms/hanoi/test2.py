#coding=utf-8
def hanoi(n,f,buffer,to):
    if n==1:
        print(f,'-->',to)
    else:
        #将前n-1个盘子从a移动到b上
        hanoi(n-1,f,to,buffer)
        #将最底下的最后一个盘子从a移动到c上
        hanoi(1,f,buffer,to)
        #将b上的n-1个盘子移动到c上
        hanoi(n-1,buffer,f,to)

n=int(input('请输入汉诺塔的层数：'))
hanoi(n,'A','B','C')
