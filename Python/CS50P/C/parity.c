#include <stdio.h>

int even(int n){
  return n % 2 == 0;
}

int main(){
  int x;
  printf("What's x?: ");
  scanf("%d", &x);

  if (even(x)){
    printf("Even\n");
  } else {
    printf("Odd\n");
  }

  return 0;
}
