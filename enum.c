#include "stdio.h"


enum weekday {sun, mon, tue, wed, thu, fri, sat} x;
enum animal {dog = 1, cat, bear = 4, dear, squirrel = 6};

int main(void)
{
	int result;
	result = sun + dog;
	printf("add: %d\n", result);
	result = bear - wed;
	printf("minus: %d\n", result);
	result = thu * fri;
	printf("multiple: %d\n", result);
	result = sat / bear;
	printf("divide: %d\n", result);
	result = mon & fri;
	printf("and: %d\n", result);
	result = thu | squirrel;
	printf("or: %d\n", result);
	result = ~dear;
	printf("not: %d\n", result);
	result = mon << 1;
	printf("move left: %d\n", result);
	result = bear >> 1;
	printf("move right: %d\n", result);
	result = fri ^ bear;
	printf("XOR: %d\n", result);
	x = fri;
	result = ++x;
	printf("self++: %d\n", result);
    x = fri;
	result = --x;
	printf("self--: %d\n", result);
	return 0;
}
