#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp;
    fp = fopen("paragraph.txt", "r");

    if (fp == NULL)
        return 1;

    char line[201];
    char longest[201];
    int max_len = 0;

    while (fgets(line, 200, fp) != NULL)
    {
        int len = strlen(line);
        if (len > max_len)
        {
            max_len = len;
            strcpy(longest, line);
        }
    }

    fclose(fp);

    printf("%d\n", max_len);
    printf("%s\n", longest);

    return 0;
}