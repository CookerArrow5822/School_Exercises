/*Author: Nicholas Meehan
  Date: 30 OCT 2025
  This code finds the maximum difference
  between the ;argest and smallest number in any given arguments
  larger than 2 and less than 100*/

//initialising studio
#include <stdio.h>
#include <stdlib.h>

//declaring function prototypes
int max_difference(int *, int);

// will create an array of all of the argumens
int main(int argc, char* argv[]){
	int length = argc - 1; // -1 for filename
	int numbers[100];
	for (int i = 0; i < length; i++){
		numbers[i] = atoi(argv[i+1]); // atoi to save each number as an integer
	}
	//print final results
	printf("%d\n", max_difference(numbers, length));
	return 0; // return 0 to indicate the program is complete

}
//function that will locate max and min values and subtract min from max
int max_difference(int* numbers, int length){
	int max = numbers[0]; // initialising variables
	int min = numbers[0];
	for (int i = 0; i < length; i++){
		if (max < numbers[i]){ // finding max number
			max = numbers[i]; // if num[i] bigger than max then replace max with num[i]
		}
		if (min > numbers[i]){ // finding min number
			min = numbers[i]; // if num[i] less than min replace min with num[i]
		}
	}

	int result = max - min; // calculating the difference between max num and min num
	return result; // return the result
}