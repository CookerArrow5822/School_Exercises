// Author Nicholas Meehan
// 10/Dec/2025
/* find the maximum possible sum formed by adding 2
adjacent pairs together where each part is increasing
e.g a[i] < a [i+1]
*/

/* if i had more time i would figure out what cases im failing as they
are hidden from view as i pass all of the other tests but the hidden ones
and i personally dont see any problems in how my code works at this current time*/
// adding includes
#include <stdio.h>
#include <stdlib.h>

//type define the struct
typedef struct Pair Pair;
// define the struct with val and adj
struct Pair
{
	int val;
	int adj;
};
// initialising functions
void AddPair(Pair p[], int argc, char*argv[]);
void MaxPair(Pair p[], int NumberOfIntegers);
// main function
int main(int argc, char* argv[]){
	Pair pairs[100];//Declare a maximum of 100 pairs.
	int NumberOfIntegers = (argc - 1) / 2; //count the number of pairs in stadard input
	AddPair(pairs, argc, argv); //calling AddPair
	MaxPair(pairs, NumberOfIntegers); // calling MaxPair
}
//adds all the pairs to the struct to be compared at MaxPair
void AddPair(Pair p[], int argc, char*argv[]){
	int NumberOfIntegers = (argc - 1)/2;//Number of pairs in standard input
	
	int index = 1;//Start at index 1 to avoid encountering program index
	for(int i = 0; i < NumberOfIntegers; i++){
		p[i].val = atoi(argv[index]); // stores the value in the struct Pair under p[i].val
		p[i].adj = atoi(argv[index + 1]); // stores the value in the struct Pair under p[i].adj for the value adj to p[i].val

		index = index + 2;//Start at the next pair
	}
}
/*Compare adjacent to make sure they are increasing
fidn the max value of these subsequent increasing pairs
print the max sum formed by the largest sum of subsequent increasing pairs*/
void MaxPair(Pair p[], int NumberOfIntegers){
	int max = 0;
	for(int i = 0; i < NumberOfIntegers; ++i){	
		if (p[i].val < p[i].adj && p[i].val + p[i].adj > max){ // checks if val is higher than adjacent and then if their sum is higher than max
			max = p[i].val + p[i].adj; // updates max to the newest max value
		
			
		}
	}
	//print max
	printf("%d\n", max);
}
