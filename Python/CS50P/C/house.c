#include <stdio.h>
#include <string.h>

int main(){
  char* name;
  printf("What's your name?: ");
  fgets(name, sizeof name, stdin);

  if ( strcmp(name, "Harry\n") == 0 || strcmp(name, "Hermione\n") == 0 || strcmp(name, "Ron\n") == 0 ){
    printf("Gryffindor\n");}
  else if (strcmp(name, "Draco\n") == 0){
    printf("Slytherin\n");}
  else {
    printf("Who?\n");
  }

  return 0;
}
