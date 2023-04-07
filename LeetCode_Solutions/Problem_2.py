 # %%
#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
     def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"
#This is how the inputs are provided
#l1=[2,4,3]
#l2=[5,6,4]
l1=ListNode( 2, ListNode( 4, ListNode(3, None)))
l2=ListNode( 5, ListNode( 6, ListNode(4, None)))
print(l1)
print(l2)
#Demostrating linked list work and are being build
# %%
# The numbers are stored backwards so we can add them in sequence
counter=0
num1=[]
num2=[]
l1=ListNode( 2, ListNode( 4, ListNode(3, None)))
l2=ListNode( 5, ListNode( 6, ListNode(4, None)))
while (l1 or l2 ):
   num1t = str(l1.val) if l1.val else 0
   num2t = str(l2.val) if l2.val else 0
   num1.append(num1t)
   num2.append(num2t)
   l1 = l1.next
   l2 = l2.next

result=int(''.join(num1[::-1])) +int(''.join(num2[::-1]))
#807
print(result)
result=list(map(int,list(str(result))))
resultln=ListNode(0)
for digit in result:
   if resultln.val == 0:
      resultln.val = digit
   else:
      resultln.next = ListNode(digit,resultln)
print(resultln)
# %%
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

