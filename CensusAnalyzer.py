#Greet user
print("Welcome to the Census Analyzer!")

analyze = "yes"
while analyze.lower().strip() == "yes":
    hshld = int(input("\nHow many households would you like to analyze? "))
    tot_ppl = []
    tot_inc = []
    tot_hshld = []
    for i in range(1, hshld + 1, 1):
        hshld_inc = []
        ppl = int(input("How many people live in household " + str(i) + "? "))
        # Add number of people to the sum of the number of people
        tot_ppl.append(ppl)
        for j in range(1, ppl + 1, 1):
            inc = int(input("What was person " + str(j) + "'s income last year? "))
        # Add individual income to individual income list
            tot_inc.append(inc)
            hshld_inc.append(inc)
        # Add individual income to household income list
        tot_hshld.append(sum(hshld_inc))
        avg = round(float(sum(tot_ppl) / hshld), 2)
        avg_hshld = round(float(sum(tot_inc) /hshld), 2)
        
    # Lists incomes by bracket
    one = [] # Less than $20,000
    two = [] # At least $20,000 but less than $40,000
    three = [] # At least $40,000 but less than $60,000
    four = [] # At least $60,000 but less than $80,000
    five = [] # At least $80,000
    for x in tot_hshld:
        if x < 20000:
            one.append(x)
        elif x >= 20000 and x < 40000:
            two.append(x)
        elif x >= 40000 and x < 60000:
            three.append(x)
        elif x >= 60000 and x < 80000:
            four.append(x)
        else:
            five.append(x) 
    # Print number of people and people per household
    print("\nNumber of people: ", sum(tot_ppl))
    print("People per household: ", avg)
    
    # Print average individual and household income
    avg_ind = round(float(sum(tot_inc) / sum(tot_ppl)), 2)
    print("\nAverage individual income: ", avg_ind)
    print("Average household income: ", avg_hshld)
    
    # Print income distribution among households
    print("\nIncome distribution: ")
    print("Less than $20,000:",len(one),"household(s)")
    print("At least $20,000 but less than $40,000:",len(two),"household(s)")
    print("At least $40,000 but less than $60,000:",len(three),"household(s)")
    print("At least $60,000 but less than $80,000:",len(four),"household(s)")
    print("At least $80,000:",len(five),"household(s)")
    
    analyze = input("\nWould you like to analyze another area (yes/no)? ")

print("\nThank you for using the Census Analyzer!")