#include <stdio.h>
#include <string.h>

int main ()
{
  char* name;
  printf("What's your name?: ");
  fgets(name, sizeof name, stdin);

  if (strcmp(name, "\n") == 0){
    name = "World!\n";
  } else {
    name = name;
  }

	printf("Hello, %s", name);
	return 0;
}
