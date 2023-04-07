 # %%
#Definition for singly-linked list.
 class Node:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n0 = Node(4,None)
n1 = Node(3,n0)
n2 = Node(2,n1)
n3 = Node(1,n2)
# %%
print(n0)
# %%
# %%
currlist = 0;
numlist=[]
while True:
   if currlist == 0:
      currlist = n3;
   if currlist == None:
      break
   currentnum=currlist.val
   numlist.append(currentnum)
   currlist = currlist.next
print("".join(str(x) for x in numlist))

