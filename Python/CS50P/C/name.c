#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
  
  if (argc < 2){
    printf("\aToo few arguments!\n");
    exit(EXIT_FAILURE);
  }

  for (int i = 1; i < argc; i++){
    printf("\aHello, my name is %s\n", argv[i]);
  }
  return 0;
}
