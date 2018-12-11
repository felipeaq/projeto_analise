#include <stdio.h>
#include <stdlib.h>

#define MAX 9000
#define MIN 0

/*void counting_sort(int a[],int n,int MAX)
{
     int count[MAX]={0},i,j;

     for(i=0;i<n;++i)
      count[a[i]]=count[a[i]]+1;


     //for(i=0;i<=MAX;++i)
     // for(j=1;j<=count[i];++j)
     //  printf("%d ",i);
}

*/
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}



void counting_sort_mm(int *array, int n)
{
  int i, j, z;

  int range = MAX - MIN + 1;

  int *count = (int*)malloc(range * sizeof(*array));

  for(i = 0; i < range; i++) count[i] = 0;
  for(i = 0; i < n; i++) count[ array[i] - MIN ]++;

  for(i = MIN, z = 0; i <= MAX; i++) {
    for(j = 0; j < count[i - MIN]; j++) {
      array[z++] = i;
    }
  }

  free(count);
}




int main()
{
    int n = 0;
    scanf("%d", &n);

    int *arr=(int*)malloc(n * sizeof(int));

  
    for(int i = 0; i < n; i++){
      arr[i] = rand()%MAX;
    }
    //printArray(arr, n);

    counting_sort_mm(arr,n);
    //printArray(arr, n);
    return 0;
}
