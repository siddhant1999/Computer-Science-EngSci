from tree import *
from binary_tree import *


x=tree(1000)
y=tree(2000)
z=tree(3000)
x.AddSuccessor(y)
x.AddSuccessor(z)
c=tree(5)
z.AddSuccessor(c)
print x.Get_LevelOrder()


q= tree(1)
w=tree(2)
e=tree(3)
r=tree(4)
t=tree(5)
l=tree(6)
s=tree(7)

w.AddSuccessor(t)
w.AddSuccessor(l)
e.AddSuccessor(s)

q.AddSuccessor(w)
q.AddSuccessor(e)
q.AddSuccessor(r)


# p = q.hel(q.store[0], q.store, [])
p=q.ConvertToBinaryTree()
print p.Get_LevelOrder()

#print "Done"
a =binary_tree(1)
b = binary_tree(2)
c = binary_tree(3)
d = binary_tree(4)
e = binary_tree(5)
f = binary_tree(6)
g = binary_tree(7)

e.AddRight(f)
b.AddLeft(e)

c.AddLeft(g)
c.AddRight(d)
b.AddRight(c)
a.AddLeft(b)

#print a.Get_LevelOrder()
#print "Converting to Tree"
h=a.ConvertToTree()

print h.Get_LevelOrder()