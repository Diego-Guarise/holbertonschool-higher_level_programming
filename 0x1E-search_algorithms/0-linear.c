#include "search_algos.h"

/**
 * linear_search - find the number
 * @array: pointer to array
 * @size: size array
 * @value: number that we will found
 */

int linear_search(int *array, size_t size, int value)
{
    size_t number = 0;

    if (!array)
        return (-1);
    
    while (size--)
    {
        printf("number that we have found[%ld] = [%d]\n", number, array[number]);
        if (value == array[number])
            return (number);
        number++;
    }
    return (-1);
}