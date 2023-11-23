#include <stdio.h>

int main(){
  struct student {
    char *name;
    char *house;
    char *patronus;
  };

  struct student harry = {"Harry", "Gryffindor", "Stag"};
  struct student hermione = {"Hermione", "Gryffindor", "Otter"};
  struct student ron = {"Ron", "Gryffindor", "Jack Russel Terrier"};
  struct student draco = {"Draco", "Slytherin", '\0'};

  printf("%s >> %s >> %s\n", harry.name, harry.house, harry.patronus);
  printf("%s >> %s >> %s\n", hermione.name, hermione.house, hermione.patronus);
  printf("%s >> %s >> %s\n", ron.name, ron.house, ron.patronus);
  printf("%s >> %s >> %s\n", draco.name, draco.house, draco.patronus);

  return 0;
}
