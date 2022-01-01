#include <stdio.h>
#include <stdlib.h>

int contains(int *vec, int bot, int top, int item){
    for(int i = bot; i < top; i++){
        if(*(vec+i) == item){
            return 1;
        }
    }
    return 0;
}

void print(int *vec, int range){
    for(int i=0; i<range-1; i++){
        printf("%d, ", *(vec+i));
    }
    printf("%d\n", *(vec+range-1));
}

int main()
{
    int nTests=0;
    scanf("%d", &nTests);
    for(int n = 0; n<nTests; n++){
        int nCases;
        
        int *flakes = (int*)malloc(sizeof(int)*nCases);
        int *aux = (int*)malloc(sizeof(int)*nCases);
        *aux = -1;
        int max = 0;
        printf("Teste\n\n");
        scanf("%d", &nCases);
        
        for(int i = 0; i < nCases; i++){
            scanf("%d", (flakes+i));
        }

        for(int i = 0; i < nCases; i++){
            int j;
            for(j =0; j < nCases; j++){
                if( !contains( aux, i, j+1, *(j+flakes) ) ){
                    *(j+aux) = *(j+flakes);
                }
                else{
                    break;
                }
            }
            print(aux, j);
            if(j > max){
                max=j;
            }
        }
        printf("%d\n", max);




    }


    return 0;
}
S