#include <stdio.h>
int main (){
  int x;
  int y;
  printf("What's x?: ");
  scanf("%d", &x);
  printf("What's y?: ");
  scanf("%d", &y);

  if (x != y){
    printf("X is not equal to Y\n");
  }
  else {
    printf("X is equal to Y\n");
  }
}
