#include <iostream>
using namespace std;

enum weekday {sun, mon, tue, wed, thu, fri, sat} x;
enum animal {dog = 1, cat, bear = 4, dear, squirrel = 6};

int main()
{
	int result;
	result = sun + dog;
	cout<< "add: " << result << endl;
	result = bear - wed;
	cout<< "minus: " << result << endl;
	result = thu * fri;
	cout<< "multiple: " << result << endl;
	result = sat / bear;
	cout<< "divide: " << result << endl;
	result = mon & fri;
	cout<< "and: " << result << endl;
	result = thu | squirrel;
	cout<< "or: " << result << endl;
	result = ~dear;
	cout<< "not: " << result << endl;
	result = mon << 1;
	cout<< "move left: " << result << endl;
	result = bear >> 1;
	cout<< "move right: " << result << endl;
	result = fri ^ bear;
	cout<< "XOR: " << result << endl;
	x = fri;
	result = ++x;
	cout<< "self++: " << result << endl;
    x = fri;
	result = --x;
	cout<< "self--: " << result << endl;
	return 0;
}
