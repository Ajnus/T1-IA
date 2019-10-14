#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "leitura.h"

int** cria(int n)
{
	int i;
	int** mat = (int**)malloc(n * sizeof(int*));
	if (mat == NULL)
	{
		printf("Mem%cria insuficiente!", 162);
		exit(1);
	}

	for (i = 0; i < n; i++)
	{
		mat[i] = (int*)malloc((i + 1) * sizeof(int));
		if (mat[i] == NULL)
		{
			printf("Mem%cria insuficiente!", 162);
			exit(1);
		}
	}
	return mat;
}

void imprime_low_diag_row(int n, int** mat)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			if (i >= j)
				printf("|%d", mat[i][j]);
			/*else
				printf("|%d", mat[j][i]);*/
			if (j == (n - 1))
				printf("|\n");
		}
}

/*void preenche_low_diag_row(int n, int** mat)
{
	while ((c = getc(file)) != EOF)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < i + 1; j++)
			{
				if (i == j)
					mat[i][j] = 0;
				else if (j > i)
					mat[i][j] = -1;
				else if (c != 0)
					mat[i][j] = c;
			}		

}*/


int main(void)
{
	char ewt[30], ewf[30], ddt[30];
	int dimension;

	le_arquivo(&dimension, ewt, ewf, ddt);
	
	printf("%s\n", ewt);

	// ler da matriz
	int c;
	int n = 24;
	int** mat = cria(n);
	FILE* file;
	if ((file = fopen("resources/gr24 - Copia.txt", "r")) == NULL) 
		printf("falhou vacilao.\n"); 
	else
	{
		for (int i = 0; i < n; i++)
			for (int j = 0; j < i + 1; j++)
			{
					if (i == j)
						mat[i][j] = 0;
					else if (j > i)
						mat[i][j] = -1;
					else
					{
						/*fscanf(file, "%d", c);
						printf("%d", c);
							if ((c != 32) && (c != 48))*/
								mat[i][j] = c;
					}
			}
		imprime_low_diag_row(n, mat);
		printf("\n");
		fclose(file);
	}
	return 0;
}
