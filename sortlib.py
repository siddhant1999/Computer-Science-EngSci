
def selection_sort(u):
   for i in range(len(u)):
    min_idx = i
    for j in range(i+1, len(u)):
        if u[min_idx] > u[j]:
            min_idx = j
             
    # Swap the found minimum element with 
    # the first element        
    u[i], u[min_idx] = u[min_idx], u[i]
   return True

def heapify(u):
   
   return True

def reheapify(u,end):
      return True

def heap_sort(u):
  n = len(u)
 
  for i in range(n, -1, -1):
    heapify(u, n, i)

  # One by one extract elements
  for i in range(n-1, 0, -1):
    u[i], u[0] = u[0], u[i]   # swap
    heapify(u, i, 0)
   #reheapify(u,end)
  return True

def merge_sort(u):
   return True

def quick_sort(u,ini,fin):
   #pIndex = partition(u,ini,fin)
   return True

def partition(u,ini,fin):
   return pIndex


v1=[10,9,8,7,6,5,4,3,2,1,0]
v2=[100,1,1000,9,8,7,2,2000,10]
v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

for i in [ v1,v2,v3 ]:
   x=list(i)
   selection_sort(x)
   print x

   x=list(i)
   heapify(x)
   print x

   x=list(i)
   heap_sort(x)
   print x

   x=list(i)
   merge_sort(x)
   print x

   x=list(i)
   quick_sort(x,0,len(x)-1)
   print x