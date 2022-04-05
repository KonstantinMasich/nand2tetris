%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #define SYMBOL     1
    #define KEYWORD    2
    #define CONST_INT  3
    #define CONST_STR  4
    #define IDENTIFIER 5
    #define UNKNOWN    6
%}


%%


    /* Single line and multi-line comments: */
"//".*\n           ;
"/*"[^*/]*"*/"     ;

    /* Subroutines, methods, statements: */
class                           return KEYWORD;  
constructor|function|method     return KEYWORD;  
do|let|if|else|while|return     return KEYWORD;  

    /* Types and kinds: */
static|field|var                return KEYWORD;  
int|char|boolean|void           return KEYWORD;  
true|false|null|this            return KEYWORD;  

    /* Whitespaces: */
[ \t\n]                     ;

    /* String constants: */
\".*\"                          return CONST_STR;

    /* Integer constants: */
[1-9][0-9]*                     return CONST_INT;

    /* Identifiers: */
[a-zA-Z][_a-zA-Z0-9]*           return IDENTIFIER;

    /* Symbols: should be the rest. */
.                               return SYMBOL;


%%

int 
yywrap(void) { return 1; }

/** Removes a given char from a string; works INPLACE. */
void 
remchar(char* s, char c)
{
    int j;
    for (int i = j = 0; i < strlen(s); i++)
    {
        if (s[i] != c)
        {
            s[j++] = s[i];
        }
    }
}

int 
main(int argc, char **argv)
{
    if (argc < 2) 
    {
        printf("Please specify the input file name (without extension)!\n");
        return 1;
    }
    char infile[80], outfile[80];
    strcpy(infile , argv[1]);
    strcpy(outfile, argv[1]);
    printf("Processing %s...\n\tInput file  : %s.jack\n\tOutput file : %sT__my.xml\n",
           argv[1], infile, outfile);

    /* 1. Define types and open input/output files: */
    const char* TYPES[] = 
    { 
        NULL, "symbol", "keyword", "integerConstant",
        "stringConstant", "identifier", "unknown"
    };  
    yyin  = fopen(strcat(infile , ".jack")    , "r");
    yyout = fopen(strcat(outfile, "T__my.xml"), "w");

    /* 2. Run lexical analysis and write the result into a file: */
    fprintf(yyout, "<tokens>\n");
    int token = yylex();
    while (token)
    {
        if      (strcmp("<" , yytext) == 0) { yytext = "&lt;" ; }
        else if (strcmp(">" , yytext) == 0) { yytext = "&gt;" ; }
        else if (strcmp("&" , yytext) == 0) { yytext = "&amp;"; }
        else    { remchar(yytext, '"'); }
        fprintf(yyout, "<%s> %s </%s>\n", TYPES[token], yytext, TYPES[token]);
        token = yylex();
    }   
    fprintf(yyout, "</tokens>\n");

    /* 3. Cleanup: */
    printf("OK\n");
    fclose(yyin);
    fclose(yyout);
    return 0;
}
