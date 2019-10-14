#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "leitura.h"

int main(void)
{
	char ewt[30], ewf[30], ddt[30];
	int dimension;

	le_arquivo(&dimension, ewt, ewf, ddt);
	
	printf("%s\n", ewt);

	return 0;
}