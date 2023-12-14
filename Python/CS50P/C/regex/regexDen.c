#include <stdio.h>
#include <string.h>
#include <regex.h>

int main() {
  printf("Enter the string: ");
  char *string[100];
  fgets(string, 100, stdin);
  char * regexString = "^\W?(.+)\W?$";

  size_t maxGroups = 5;
  regex_t regexCompiled;
  regmatch_t groupArray[maxGroups];

  if ( regcomp(&regexCompiled, regexString, REG_EXTENDED) )
  {
    printf("Could not compile regular expression.\n");
    return 1;
  };

  if ( regexec(&regexCompiled, string, maxGroups, groupArray, 0) == 0 )
  {
    unsigned int g = 0;
    for ( g = 0; g < maxGroups; g++ )
    {
      if (groupArray[g].rm_so == (size_t)-1)
      {
        printf("No Regular Expression Match.");
        break;
      }
      char stringCopy[strlen(string) + 1];
      strcpy(stringCopy, string);
      stringCopy[groupArray[g].rm_eo] = 0;
      printf("Group %u: [%2u-%2u]: %s\n",
        g, groupArray[g].rm_so, groupArray[g].rm_eo,
        stringCopy + groupArray[g].rm_so);
    }
  }

  regfree(&regexCompiled);

  return 0;
}
