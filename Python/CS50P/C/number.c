#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){
  char x[10];
  printf("What's x?: ");
  fgets(x, sizeof x, stdin);

  int invalidCount = 0;

  for (int i = 0; i < sizeof x; i++){
    if (isdigit(x[i])){}
    else if (x[i] == '\0'){}
    else {
      invalidCount++;
    }
  }

  if (invalidCount == 1){
    printf("x is %s", x);
  } else {
    printf("x is not an integer!\n");
    exit(EXIT_FAILURE);
  }

  return 0;
}
