#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float equation_inputs[11][7] = {1,	1,	0.848,	1,	0.625,	0.7492,	0.99999976,
    1,	1,	0.844,	0.9999997052,	0.5	,0.53,	0.981091184,
    1,	1,	0.822,	0.9999970515,	0.625,	0.4392,	0.814492386,
    1,	1,	0.759,	0.9999702206,	0.375,	0.579666667,	0.99976281,
    1,	1,	0.677,	0.9995450534,	0.375,	0.617666667,	0.999613813,
    0	,1	,0.562	,0.9738645008	,0	,0	,0,
    1	,1	,0.365	,0	,0	,0	,0,
    0	,1	,0.389	,0.3239490232	,0.125	,0.319	,0.9910872883,
    0,	1	,0.371	,0.1259884696	,0.25	,0.43395	,0.89561359,
    0	,1	,0.521	,0.9468545881	,0.25	,0.559	,0.999988614,
    1	,1	,0.617	,0.9930844968	,0	,0	,0};

void imprimemat(int individuos, int num_weights, float populacao[individuos][num_weights]){//imprime as matrizes
    int i, j;
    for (i = 0; i < individuos; i++){
        printf("[");
        for(j=0;j<num_weights;j++){
            printf("%.3f , ",populacao[i][j]);
        }
        printf("]");
        printf("\n");
    }
}

void inicializar(int individuos, int num_weights, float populacao[individuos][num_weights], float notas[individuos]){
    srand(time(NULL));
    int i, j;
    float soma[individuos];
    for (i = 0; i < individuos; i++){
        soma[i]=0;
        for(j=0;j<num_weights;j++){
            populacao[i][j]=(float)rand()/RAND_MAX;
            soma[i]+=populacao[i][j];
        }
        for(j=0;j<num_weights;j++){
            populacao[i][j]/=soma[i];
        }
        notas[i] = 0;
    }
}

void avalia(int individuos, int num_weights, float populacao[individuos][num_weights], float notas[individuos]){
    int i,j,k;
    for(i=0;i<individuos;i++){//for individuos
        for(k=0;k<11;k++){//for input
            for(j=0;j<num_weights;j++){//for pesos
                if(k<5) {
                    notas[i]+=(populacao[i][j] * equation_inputs[k][j] * -1) ;//para noticias verdadeiras
                }
                else{
                    notas[i]+=(populacao[i][j] * equation_inputs[k][j]);//para noticias falsas
                }
            }
        }
    }
    for (i = 0; i < individuos; i++){//print das notas da população
        printf("[");
        printf("%.3f , ",notas[i]);
        printf("]");
        printf("\n");
    }
}

void evolucao_diferencial(int individuos, int num_weights, float populacao[individuos][num_weights],float populacao_intermediaria[individuos][num_weights], float f){
    int i,k,j;
    for(i=0;i<individuos;i++){
        int pai1=rand()%individuos, pai2=rand()%individuos, pai3=rand()%individuos;//gerando 3 pais
        while(pai1==pai2||pai2==pai3||pai1==pai3){//verificando se os 3 pais são iguais
            pai2=rand()%individuos;
            pai3=rand()%individuos;
        }//x1+f*(x2-x3)
        for(j=0;j<num_weights;j++){//gerando população intermediária
            populacao_intermediaria[i][j]= populacao[pai1][j] + f * (populacao[pai2][j] - populacao[pai3][j]);
        }
    }
}

int main()
{
    int i,j;

    //número_de_pesos , individuos
    int num_weights=7, individuos=10;


    //float pesos[individuos[pesos], fitness[individuos], populaçao_intermediaria[individuos][pesos];
    float populacao[individuos][num_weights],notas[individuos],trial[individuos][num_weights];

    inicializar(individuos,num_weights,populacao, notas);
    imprimemat(individuos, num_weights,populacao);
    avalia(individuos, num_weights,populacao,notas);
    evolucao_diferencial(individuos,num_weights,populacao,trial,1.2);
    imprimemat(individuos,num_weights,trial);

    return 0;
}
