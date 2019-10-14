#include "leitura.h"
#include <stdio.h>
#include <string.h>

void le_arquivo(int *dimension, char *EDGE_WEIGHT_TYPE, char *EDGE_WEIGHT_FORMAT, char *DISPLAY_DATA_TYPE) {
	FILE* file;
	char line[30];
	char name[30], type[30], comment[30];
	int ini = 1; // variavel de controle para leitura do cabeçalho


	if ((file = fopen("gr24.tsp", "r")) == NULL)
	{
		printf("Falha ao ler o arquivo\n");
	}
	else
	{
		while (fscanf(file, "%s", line) != EOF)
		{

			if (strcmp(line, "NAME:") == 0) {
				char value[30];
				if (fscanf(file, "%s", value) != EOF) {
					strcpy(name, value);
				}
			}
			else if (strcmp(line, "TYPE:") == 0) {
				char value[30];
				if (fscanf(file, "%s", value) != EOF) {
					strcpy(type, value);
				}
			}
			else if (strcmp(line, "COMMENT:") == 0) {
				char value[30];
				if (fscanf(file, "%s", value) != EOF) {
					strcpy(comment, value);
				}
			}
			else if (strcmp(line, "DIMENSION:") == 0) {
				int value;
				if (fscanf(file, "%d", &value) != EOF) {
					*dimension = value;
				}
			}
			else if (strcmp(line, "EDGE_WEIGHT_TYPE:") == 0) {
				char value[30];
				if (fscanf(file, "%s", value) != EOF) {
					strcpy(EDGE_WEIGHT_TYPE, value);
				}
			}
			else if (strcmp(line, "EDGE_WEIGHT_FORMAT:") == 0) {
				char value[30];
				if (fscanf(file, "%s", value) != EOF) {
					strcpy(EDGE_WEIGHT_FORMAT, value);
				}
			}
			else if (strcmp(line, "DISPLAY_DATA_TYPE:") == 0) {
				char value[30];
				if (fscanf(file, "%s", value) != EOF) {
					strcpy(DISPLAY_DATA_TYPE, value);
				}
			}
			else if (strcmp(line, "EDGE_WEIGHT_SECTION") == 0) {
				//pensar
			}
		}
	}

	fclose(file);
}