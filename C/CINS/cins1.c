#include <stdio.h>
#include <limits.h>

int main (int argc, char *argv[])
{
  char ch = 'A';    // A variable with type char.
  printf("The character %c has the character code %d.\n", ch, ch);
  for ( ; ch <= 'Z'; ++ch)
    printf("%2c\n", ch);

  printf("Storage sizes and value ranges of the types char and int\n\n" );
  printf("The ytpe char is %s.\n\n", CHAR_MIN < 0 ? "signed" : "unsigned");

  printf(" Type  Size (in bytes)  Minimum       Maximum\n"
         "-----------------------------------------------\n");
  printf(" char %8d %20d %15d\n", sizeof(char), CHAR_MIN, CHAR_MAX );
  printf(" int  %8d %20d %15d\n", sizeof(int), INT_MIN, INT_MAX );
  return 0;
}
