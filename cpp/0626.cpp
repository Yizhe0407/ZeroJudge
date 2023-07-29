#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    int figure_1, figure_2;

    printf("請輸入兩數值\n ==> ");
    scanf("%d %d", &figure_1, &figure_2);
    if (figure_1 > figure_2)
    {
        printf("較小值是 %d\n", figure_2);
    }
    else if (figure_1 == figure_2)
    {
        printf("兩數值相等\n");
    }
    else
    {
        printf("較小值是 %d\n", figure_1);
    }
    system("pause");
    return 0;
}