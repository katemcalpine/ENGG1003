/*
 * Task5.c
 *
 *  Created on: 6 May 2019
 *      Author: Kate McAlpine
 */
#include <stdio.h>
#include <stdlib.h>

int main() {
int arrayData[3][3];
int tmpnum, max = 0;
char tmp[10];
FILE *input;
input = fopen("fileIO", "r");
for (int i=0; !feof(input); i++) {
	for (int ii=0; ii<3; ii++) {
		for (int iii=0; iii<3; iii++) {
			fscanf(input, "%s", tmp);
			tmpnum = atoi(tmp);
			arrayData[ii][iii] = tmpnum;
		}
	}
}
max = arrayData[0][0];
for (int ii=0; ii<3; ii++) {
	for (int iii=0; iii<3; iii++) {
		printf("%d ", arrayData[ii][iii]);
		if (arrayData[ii][iii] > max)
			max = arrayData[ii][iii];
	}
	printf("\n");
}
printf("\nMax: %d\n", max);
return 0;
}
