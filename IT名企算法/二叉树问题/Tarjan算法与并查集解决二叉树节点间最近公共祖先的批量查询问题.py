class node: #二叉树结构
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
class query: #查询表
    def __init__(self,o1,o2):
        self.o1=o1
        self.o2=o2
        
def createTree(s): #根据广义表构建二叉树
    top=-1
    k=0
    p=b=None
    st=[None]*100
    for ch in s:
        if ch=='(': #有孩子节点,父节点入栈,k=1为左孩子
            top+=1
            st[top]=p
            k=1
        elif ch==')': #当前父节点用完，退栈
            top-=1
        elif ch==',': #k=2为右孩子
            k=2
        else:
            p=node(int(ch))
            if b is None:b=p #头节点
            else:
                if k==1:st[top].left=p
                elif k==2:st[top].right=p
    return b

def midfind(head): #中序遍历
    if head.left is not None:
        midfind(head.left)
    print(head.value,end=' ')
    if head.right is not None:
        midfind(head.right)
      
s='1(2(4,5(7,8)),3(,6(9,)))' #广义表      
head=createTree(s)
print('中序遍历树结构',midfind(head))

#查询表
d={0:[4,7],1:[7,8],2:[8,9],3:[9,3],4:[6,6],5:[None,5],6:[None,None]}
import collections
def query_index(d): #建立query表和index表
    query=collections.defaultdict(list)
    index=collections.defaultdict(list)
    for i,j in d.items():
        if j[0]==j[1] or j[0] is None or j[1] is None:
            continue
        query[j[0]].append(j[1])
        query[j[1]].append(j[0])
        index[j[0]].append(i)
        index[j[1]].append(i)
    return query,index
    
def look(query,index): #查看query表和index表的生成情况
    print('query')
    for i,j in query.items():
        print(i,j)
    print('index')
    for i,j in index.items():
        print(i,j)
        
query,index=query_index(d)
look(query,index)

'''
def father_idx(father,data): #找到字典里对应的索引
    for i,j in father.items():
        if data in j:
            return i
'''

father=[i for i in range(10)] #9个节点，一开始以自身为集合

def find(data): #并查集
    if father[data]!=data:
        father[data]=find(father[data])
    return father[data]
    
def union(x,y): #合并
    xr, yr = find(x), find(y)
    if xr == yr:
        return
    father[yr] = xr

def ask(query,index,father,ans,head,col): #开始tarjan算法
    if head.left is not None: #按照中序遍历顺序
        ask(query,index,father,ans,head.left,col)
        
    col|=set([head.value]) #已查节点
    #father[head.value].append(head.value) #初始化赋予自己,假设为叶子

    if head.left is not None and head.left.value in col:#左孩子合并
        left=head.left.value
        #idx=father_idx(father,left)
        idx=find(left)
        #father[head.value].extend(father[idx])
        #del father[idx]
        union(head.value,idx)
    
    #看是否具有查询任务
    for i in query[head.value]:
        if i in col:
            #第几项任务
            ant=(set(index[head.value])&set(index[i])).pop()
            if ans[ant]!=0:continue #已经完成的任务
            #idx=father_idx(father,i)
            idx=find(i)
            ans[ant]=idx
            
    if head.right is not None:
        ask(query,index,father,ans,head.right,col)
    #回溯时才处理右孩子
    if head.right is not None and head.right.value in col:#右孩子合并
        right=head.right.value
        #idx=father_idx(father,right)
        idx=find(right)
        #father[head.value].extend(father[idx])
        #del father[idx]
        union(head.value,idx)
        
n=0
#father=collections.defaultdict(list) #代表每一个的合集的父节点
for i in d.keys(): #代表要查询的总数
    n+=1
ans=[0]*n #结果集
col=set()
ask(query,index,father,ans,head,col)

def remain(ans,d):#处理那些剩下的可以直接判断的
    for i in range(len(ans)):
        if ans[i]==0:
            k=d[i]
            ans[i]=k[0] if k[0] is not None else k[1]
            
remain(ans,d)
print(ans)