/*
 * Description: A sacnner for replacing the letters.
 * Replaces every letter with three letters after, in alphabetical
 * order
 * wrapping around at Z.
 */

lowerCase   [a-z]
upperCase   [A-Z]

%%
{lowerCase}  {char ch = yytext[0];
              ch += 3;
              if(ch > 'z') ch -= ('z' + 1 - 'a');
              printf("%c", ch);
             }
{upperCase}  {char ch = yytext[0];
              ch += 3;
              if(ch > 'Z') ch -= ('Z' + 1 - 'A');
              printf("%c", ch);
             }
%%
main()
{
 printf("Given me your input:\n");
 yylex();
}


