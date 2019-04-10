#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float **populacao,*notas;
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

void imprimemat(int individuos, int num_weights){
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

void inicializar(int individuos, int num_weights){
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

    }
}

void avalia(int individuos, int num_weights){
    int i,j,k;
    for(i=0;i<individuos;i++){
        for(k=0;k<11;k++){
            for(j=0;j<num_weights;j++){
                printf("%d esse é o k\n",k);
                if(k<5) {
                    notas[i]+=(populacao[i][j] * equation_inputs[k][j] * -1) ;
                }
                else{
                    notas[i]+=(populacao[i][j] * equation_inputs[k][j]);
                }
                printf("%f * %f = %f",populacao[i][j],equation_inputs[k][j],notas[i]);
                printf("\n");
            }
        }
    }
    for (i = 0; i < individuos; i++){
        printf("[");
        printf("%.3f , ",notas[i]);
        printf("]");
        printf("\n");
    }
}

int main()
{
    int i,j;
    int num_weights=7, individuos=1;

    populacao = (int**) malloc(individuos*sizeof(int*));
    for(i=0;i<individuos;i++){
        populacao[i]=(int*) malloc(num_weights*sizeof(int));
        for(j=0;j<num_weights;j++){
            populacao[i][j]=0;
        }
    }
    notas = (float*) malloc(individuos*sizeof(float));
    for(i=0;i<individuos;i++){
        notas[i]=0;
    }
    inicializar(individuos,num_weights);
    imprimemat(individuos, num_weights);
    avalia(individuos, num_weights);

    //population = AGnovo.new_population(sol_per_pop)
    //print(population)

    return 0;
}
