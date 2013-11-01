#include <stdio.h>

void main() 
{
	int j = 14;
	int k = (j + 13) / 27;
	while(k <= 10){
		k += 1;		
		int i = 3 * k - 1;
		printf("k = %d, i = %d\n",k, i);
	} 
}
