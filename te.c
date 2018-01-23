#include <stdio.h>

int fibo(int n);

int main(void) {
   int i;
   for (i=0;i<20;i=i+1){
      int f = fibo(i);
      printf("fibo(%d)=%d\n",i,f);
   }

   return 0;
}

int fibo(int n){
   if(n ==0) return 1;
   return n+fibo(n-1);
}