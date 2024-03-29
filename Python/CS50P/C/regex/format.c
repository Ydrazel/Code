#include <stdio.h>
#include <regex.h>
#include <string.h>

int main() {
  printf("Enter your name: ");
  char *source[20];
  fgets(source, sizeof source, stdin);
  char * regexString = "^(.+), *(.+)$";

  size_t maxGroups = 3;
  regex_t regexCompiled;
  regmatch_t groupArray[maxGroups];

  if ( regcomp(&regexCompiled, regexString, REG_EXTENDED) )
  {
    printf("Could not compile regular expression.\n");
    return 1;
  };

  if ( regexec(&regexCompiled, source, maxGroups, groupArray, 0) == 0 )
  {
    unsigned int g = 0;
    for ( g = 0; g < maxGroups; g++ )
    {
      if ( groupArray[g].rm_so == (size_t)-1 )
        break;

      char sourceCopy[strlen(source) + 1];
      strcpy(sourceCopy, source);
      sourceCopy[groupArray[g].rm_eo] = 0;
      printf("Group %u: [%2u-%2u]: %s\n",
          g, groupArray[g].rm_so, groupArray[g].rm_eo,
          sourceCopy + groupArray[g].rm_so);
    }
  }

  regfree(&regexCompiled);

  return 0;
}
