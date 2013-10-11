#include <stdio.h>

int main(void)
{
	short a = 4;	
	int b = 1;
	long c = 3246;
	float d = 3.14159;
	double e = 4.0984235423546;
	char s = 'f';
	int* p = &b;
	struct student {
		int id[10];		
		char name[30];
		int grade;			
	};
	struct student Jim, Louis;
	struct player {
		char name[20];
		long gpa;
	} Bobo;
	Jim.grade = Louis.id[1];
	Jim.name[2] = Louis.grade;
	
	Jim = Louis;
	Jim = Bobo;
	
	a = m;
	b = s;
	a = d;
	e = c;
	d = p;
	
	printf("%c\n", b);
	printf("%d\n", a);
	printf("%f\n", e);
	printf("%d\n", s + 3);
	printf("%f\n", e);
	
	return 0;

}
