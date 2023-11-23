#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void shuffle(){
  char* deck[3] = {"jack", "queen", "king"};
  int i = 0;
  while (deck[i]){
    size_t n = sizeof deck / sizeof *deck;
    while (n > 0){
      srand(time(NULL));
      int j = rand()/(RAND_MAX/n);
      printf("%s\n", deck[j]);
      deck[j] = deck[--n];
      i++;
    }
  }
}

int main (void){
  shuffle();
}
