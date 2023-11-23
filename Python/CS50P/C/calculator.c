#include <stdio.h>

int square(int x){
  return x * x;
}

int main(){
  int x;
  printf("What's x?: ");
  scanf("%d", &x);
  int xs = square(x);
  printf("x square is: %d\n", xs);
  return 0;
}
