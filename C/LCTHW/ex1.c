#include <stdio.h>

/* This is a comment */
int main (int argc, char * argv[])
{
  int distance = 100;
  int steps = 25000;

  // this is also a comment
  printf("You are %d miles away.\n", distance);
  printf("The distance is %d miles.\n", distance);
  printf("You'll need %d steps to cover the %d miles.\n", steps, distance);
  return 0;
}
