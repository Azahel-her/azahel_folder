Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

odd_and_even = ["even" if item %2==0 else "odd" for item in Numbers]

print(odd_and_even)

Numbers_of_3=[1,2,3,4,5,6,7,8,9,10]
multi_of_3 = [number*1 for number in Numbers_of_3 if number%3==0]
print(multi_of_3)


