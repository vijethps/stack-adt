class stack:
    def __init__(self):
        self.li=[]
    def isEmpty(self):
        if self.li==[]:
            print(True)
        return False
    def push(self,val):
        self.li.append(val)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            x=self.li[-1]=None
            del(self.li[-1])
            return x
    def peek(self):
        if self.isEmpty():
            return None
        return self.li[-1]
ob=stack()
for i in range(int(input())):
    li=input().split()
    if(li[0])=="push":
        ob.push(int(li[1]))
    elif(li[0])=="pop":
        ob.pop()
    elif(li[0])=="peek":
        print(ob.peek())
    elif(li[0])=="isEmpty":
        print(ob.isEmpty())
    else:
        print("invalid")
