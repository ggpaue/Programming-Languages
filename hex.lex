/*
 * Description: A scanner for recognizing 32-bit hexadecimal numbers.
 * Hexadecimal numbers is combined with digits(0~9) and letters(A~F).
 * Hexadecimal numbers is presented begin with 0x.
 * Others are not counted as hexadecimal numbers.
 */

digit     [0-9]
alpha     [a-fA-F]
hextail   ({digit}|{alpha}){1,8}
hex       0[xX]{hextail}

%%
{hex}   printf("Found a HEX num %s !", yytext);
.       printf("");
%%

main()
{
 printf("Given me your input:\n");
 yylex();
}
