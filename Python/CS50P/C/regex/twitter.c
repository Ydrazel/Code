#include <stdio.h>
#include <regex.h>
#include <string.h>

#define MAXLENGTH 1000

int main()
{
  char input[MAXLENGTH];
  char * pattern = "^.+/(.+)$";
  printf("\nURL: ");
  fgets(input, MAXLENGTH, stdin);

  size_t maxGroups = 2;
  regex_t regexCompiled;
  regmatch_t groupArray[maxGroups];

  if ( regcomp(&regexCompiled, pattern, REG_EXTENDED) )
  {
    printf("Could not compile regular expression.\n");
    return 1;
  };

  if ( regexec(&regexCompiled, input, maxGroups, groupArray, 0) == 0 )
  {
    char inputCopy[strlen(input) + 1];
    strcpy(inputCopy, input);

    printf("Username: %s\n", inputCopy + groupArray[1].rm_so);
  } else {
    printf("Username: NULL\n");
  };

  regfree(&regexCompiled);

  return 0;
}
