#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{

}
char *skip(char *lett)
{
    char first;
    if (lett == NULL)
    {
        return ('');
    }
    first = lis[0];
    if (first == "a")
    {
        return skip(lett++);
    }
    else
        return first + skip(let++)

}
