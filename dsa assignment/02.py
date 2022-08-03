def reverse(stringg,start,end):

    while start<end:
        stringg[start],stringg[end]=stringg[end],stringg[start]
        start+=1
        end-=1
stringg = [1, 2, 3, 4, 5, 6,7]
print(stringg)
reverse(stringg, 0, 6)
print("Reversed list is")
print(stringg)
        