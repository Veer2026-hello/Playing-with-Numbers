# Program to find HCF/GCD

# Enter 2 numbers
numberLargest = int(input("Enter the Largest number : "))
numberSmallest = int(input("Enter the Smallest number : "))

# Using Eucliden Algorithms
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ",numberLargest)
