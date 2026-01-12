// Author Nicholas Meehan
// 10/Dec/2025

/* compress a line of integer inputs using run length encoding
for example 111 -> 1 3 or 22 -> 2 2 or 44444 -> 4 5
*/


/* what i wouldve done if i had more time,
I would have added a function to take in the value and all counts
and add that to a struct

I would have then added a function that would have transfered
each values count amount into an integer 1-9 (as i didnt see a value over 9 in the input example)

I would have then print each value following their subsequent count value

since the question wants spaces to act as new line characters when printing out values
I would have also setup a tracker in the while loop where if the character was a space character
then it would take that value and store it in an array for later use*/

// adding includes
#include <stdio.h>
#include <stdlib.h>
// defining struct type Count
typedef struct Count Count;
// defining struct Count
struct Count
{
	int count;
	int value;
};
// initialising varable
void AddCount(Count c[], int argc, char*argv[]);
// main
int main(int argc, char* argv[]){
	Count values[50];//Declare a maximum of 50 values.
	int NumberOfIntegers = argc - 1; //count the number of pairs in stadard input
	AddCount(values, argc, argv); //calling AddCount

}
// this will add the count of each value to the values in struct Count
void AddCount(Count c[], int argc, char*argv[]){
	int NumberOfIntegers = argc - 1;

	int i = 0;
	int counter = 0;
	int prev_counter = 0;
	for (int i = 0; i < argc  - 1; i++){
		while (argv[i + 1] = argv[i]){
			counter++;
		}
	}


}

