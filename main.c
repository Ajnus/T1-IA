#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
	int c;
	FILE* file;
	if ((file = fopen("resources/gr24.txt", "r")) == NULL) 
	{   
		printf("falhou vacilao.\n"); 
	}
	else
	{
		/*bool esp = false;
		bool zero = false;*/
		while ((c = getc(file)) != EOF)
		{
			putchar(c);
			/*if (c == 32)
				esp = true;

			else if (esp == true)
				if (c == 48)
					zero = true;

			else if (zero == true)
			{
				printf("\n");
				esp = false;
				zero = false;
			}*/			
		}
		printf("\n");
		fclose(file);
	}
	return 0;
}