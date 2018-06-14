from collections import deque
def value(chars,i):
    deq=deque()
    pre=0
    while i<len(chars) and chars[i]!=')':
        if chars[i].isdigit():
            pre=pre*10+int(chars[i])
            i+=1
        elif chars[i]!='(':
            addnum(deq,pre)
            deq.append(chars[i])
            i+=1
            pre=0
        else:#从左括号开始递归
            bra=value(chars,i+1)
            pre=bra[0]
            i=bra[1]+1
    addnum(deq,pre)
    return getnum(deq),i
    
def addnum(deq,num):
    if deq!=deque([]):
        cur=0
        top=deq.pop()
        if top=='+' or top=='-':#稍后处理，放入队尾
            deq.append(top)
        else:
            cur=int(deq.pop())
            num=cur*num if top=='*' else cur//num
    deq.append(str(num))
    
def getnum(deq):#获取数值
    res=0
    add=True
    cur=None
    num=0
    while deq!=deque([]):
        cur=deq.popleft()
        if cur=='+':
            add=True
        elif cur=='-':
            add=False
        else:
            num=int(cur)
            res+=num if add else (-num)
    return res
    
chars='48*((70-65)-43)+8*1'
print(value(chars,0)[0])