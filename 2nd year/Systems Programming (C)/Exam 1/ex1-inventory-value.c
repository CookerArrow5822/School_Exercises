/*Author: Nicholas Meehan
  Date: 30th October 2025
  This program is meant ot take input from arguments and based
  on that input to determine whether an item is discounted 
  and calculate the total cost of all items in inventory
  discount included
  
 Input may be Product Stock Price Discount status
 Output may include Price of inventory rounded to nearest .00*/

 //adding all libraries i need
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// defining a new struct
typedef struct Product Product;
//listing structs contents 
struct Product{
	char name[20];
	float price;
	int stock;
	int discount;
};
// defining prototype functions
void AddProduct(Product p[], int argc, char*argv[]);
void PrintPrice(Product p[], int numOfProducts);

//we define memory allocations and get the amount of products
// we also call out functions here
int main(int argc, char *argv[]){
	Product product[50];
	int numOfProducts = (argc - 1) / 4;
	AddProduct(product, argc, argv);
	PrintPrice(product, numOfProducts);

	return 0;
}
// this function compiles and collects all of the input data and adds them to an array
void AddProduct(Product p[], int argc, char*argv[]){ // it is voided as we aren't expecting output or reusing an return values
	int numOfProducts = (argc - 1) / 4;
	int index = 1; // we start on 1 to ignore the filename
	for (int i = 0; i < numOfProducts; i++){
		strcpy(p[i].name, argv[index]); // use strcpy as argv is a pointer not a string
		p[i].stock = atoi(argv[index + 1]);
		p[i].price = atof(argv[index + 2]);
		p[i].discount = atoi(argv[index + 3]);
		index = index + 4; //add 4 to index each time to get the next value of each product and not have duplicate data
	}
}
//this is the function that prints the output
void PrintPrice(Product p[], int numOfProducts) {
	char* discounted = ""; // define discounted
	double total = 0; // defining total as a double which a float of .2f or .00
	for (int i = 0; i < numOfProducts; ++i){ // loops through all products
		if (p[i].discount == 1){ //if discount is one assign Discoutned to discounted to be printed later
			total = total + (p[i].stock * p[i].price * 0.9); //multiplied stock, price all at 10% discount and added it to total
		}
		else if (p[i].discount == 0){// if discount is 0 assing the value No Discount to discounted to be printed later
			total = total + (p[i].stock * p[i].price);//multiplied stock and price with no discount
		}
	}
	printf("%.2f\n", total);	
}
