#include <stdio.h>

int main(void){
  printf("Score: ");
  int score;
  scanf("%d", &score);

  if (90 <= score){ printf("Grade: A\n"); }
  else if (80 <= score){ printf("Grade: B\n"); }
  else if (70 <= score){ printf("Grade: C\n"); }
  else if (60 <= score){ printf("Grade: D\n"); }
  else { printf("Grade: F\n"); }
}
