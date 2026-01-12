//Author Nicholas Meehan
// 27/10/2025
/* Given 2 sorted sequences of arrays and we must
compile these 2 sorted sequences into one sorted main array*/

//adding includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// declaring functions
int BubbleSort(int sequence[], int argc);
int printArray(int sequence[], int length);

// main
int main(int argc, char* argv) {
	int n = atoi(argv[1]);// gets the first digit which is the number of elements in the first sequence
	int m = atoi(argv[n + 2]); // gets the second digit which is the number of elements in the second sequence
	int sequence[n + m]; // max amount of numbers in the sequence is the number of elements in the first and the last
    for (int i = 2; i < n + 2; ++i){ // skips the first 2 numbers and goes until i = n + 2
        sequence[i] = atoi(argv[i]); // adds the first sequence into the array
	}

	for (int i = n + 2; i < n + m + 3 + 1; i++){ // skips first 2 digits + all digits in n and starts on hhe first digit of m
		sequence[i] = atoi(argv[i]); // adds the second sequence into the array
	}

	int length = argc - 3; // length is the length of all characters in input minus the 2 numbers giving us the amount of elements in the first sequence and second
	//calling functions
	BubbleSort(sequence, argc);
	printArray(sequence, length);
}
//prints all the numbers out one by one in sorted order
int printArray(int sequence[], int length) {
    for (int i = 0; i < length; ++i){
        printf("%d\n", sequence[i]);
    }
}
//sorts the now unsorted list with the elements of the sorted lists using a bubblesort algorithm
int BubbleSort(int sequence[], int argc) {
	int length = argc - 3;

    for (int i = 0; i < length; ++i){
        for(int j = i + 1; j < length; ++j){
            if (sequence[i] > sequence[j]){
                int temp = sequence[i];
                sequence[i] = sequence[j];
                sequence[j] = temp;
            }
        }
    }
}