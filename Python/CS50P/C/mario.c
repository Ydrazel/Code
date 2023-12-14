#include <stdio.h>

int assertInput(){
  int inInt;
  printf("Enter the size of the obstacle: ");
  scanf("%d", &inInt);
  return inInt;
}

int printRow(int width){
  while (width > 0){
    printf("*");
    width--;
  }
  return 0;
}

int printSquare(int size){
  int width_ = size;
  while (size > 0){
    printRow(width_);
    printf("\n");
    size--;
  }
  return 0;
}

int main (){
  int size = assertInput();
  printSquare(size);
  return 0;
}
