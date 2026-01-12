#include <stdio.h>
#include <stdlib.h>

// Fill matrix from argv using pointer
void fillMatrix(int *matrix, int rows, int cols, char *argv[], int *index)
{
    for (int i = 0; i < rows * cols; i++)
    {
        *(matrix + i) = atoi(argv[(*index)++]);
    }
}

// Multiply matrices A (m1×n1) and B (m2×n2) into C (m1×n2)
void multiplyMatrices(int *A, int *B, int *C, int m1, int n1, int m2, int n2)
{
    for (int i = 0; i < m1; i++)
    {
        for (int j = 0; j < n2; j++)
        {
            *(C + i * n2 + j) = 0;
            for (int k = 0; k < n1; k++)
            {
                *(C + i * n2 + j) += (*(A + i * n1 + k)) * (*(B + k * n2 + j));
            }
        }
    }
}

// Print matrix
void printMatrix(int *matrix, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("%d", *(matrix + i * cols + j));
            if (j < cols - 1)
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main(int argc, char *argv[])
{
    int index = 1;

    // First matrix
    int m1 = atoi(argv[index++]);
    int n1 = atoi(argv[index++]);
    int A[m1][n1];
    fillMatrix(&A[0][0], m1, n1, argv, &index);

    // Second matrix
    int m2 = atoi(argv[index++]);
    int n2 = atoi(argv[index++]);
    int B[m2][n2];
    fillMatrix(&B[0][0], m2, n2, argv, &index);

    // Result matrix
    int C[m1][n2];
    multiplyMatrices(&A[0][0], &B[0][0], &C[0][0], m1, n1, m2, n2);

    // Output
    printMatrix(&C[0][0], m1, n2);

    return 0;
}