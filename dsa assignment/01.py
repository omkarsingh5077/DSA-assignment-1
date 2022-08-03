def find(array,len,summ):
    print('Pairs whose sum is :',summ)
    for i in range(len):
        for j in range(i,len):
            if (array[i]+array[j]) == summ:
                print(array[i],array[j])
              
array = [int(x)  for x in input().split()]
summ = int(input())

print('Array=',array)
find(array,len(array),summ)
                
                
            