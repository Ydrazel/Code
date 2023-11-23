#include <stdio.h>
int get_number(void){
  while (1>0){
    int n;
    printf("What's n?: ");
    scanf("%d", &n);
    if (n>0){
      return n;
    }
  }
}
int meow(int n){
  int i;
  for (i=0;i<n;i++){
    printf("meow\n");
  }
  return 0;
}
int main(){
  int number;
  number = get_number();
  meow(number);
  return 0;
}
