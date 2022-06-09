import random

def check1():
    """Checks if the total profit is negative at year-end"""
    if sum(total) < 0:
        print("The total profit is negative at year-end. The manager will close the fishing operation and look for a new career.")

def check2():
    """Checks if the total profit reaches at least $250,000 at year-end"""
    if sum(total) > 250000:
        print("Over $250,000 in total profit. The manager happily retires.")

def check3():
    """Checks if there are five consecutive years of positive profit"""
    if total[0] > 0 and total[1] > 0 and total[2] > 0 and total[3] > 0 and total[4] > 0:
        print("Five consecutive years of positive profit. The manager happily retires.")

# Simulate a function for fishing operation focused on salmon
def salmon_ops(element):
    """Simulates and prints the amount of profit from salmon operations during the current year."""
    # Randomly generate a number between 1 and 20
    chance = random.randrange(1, 21)
    
    # Option 1: 5% chance, excellent yield
    if chance == 1:
        total.append(100000)
        print("\n** Year ",element," **")
        print("\nFocus this year: salmon")
        print("This year's profit (or loss): $100000")
        print("Total profit (or loss): $" + str(sum(total)))
    
    # Option 3: 20% chance, poor yield   
    elif chance >= 2 and chance <= 5:
        total.append(-10000)
        print("\n** Year ",element," **")
        print("\nFocus this year: salmon")
        print("This year's profit (or loss): $-10000")
        print("Total profit (or loss): $" + str(sum(total)))

    # Option 2: 75% chance, moderate yield   
    else:
        total.append(40000)
        print("\n** Year ",element," **")
        print("\nFocus this year: salmon")
        print("This year's profit (or loss): $40000")
        print("Total profit (or loss): $" + str(sum(total)))
 
# Simulate a function for fishing operation focused on crabs      
def crab_ops(element):
    """Simulates and prints the amount of profit from crab operations during the current year."""
    
    # Randomly generate a number between 1 and 10
    crab_chance = random.randrange(1, 11)
    
    # Option 1: 60% chance, good yield
    if crab_chance >= 1 and crab_chance <= 6:
        total.append(50000)
        print("\n** Year ",element," **")
        print("\nFocus this year: crabs")
        print("This year's profit (or loss): $50000")
        print("Total profit (or loss): $" + str(sum(total)))
        
    # Option 2: 40% chance, poor yield
    else:
        total.append(-5000)
        print("\n** Year ",element," **")
        print("\nFocus this year: crabs")
        print("This year's profit (or loss): $-5000")
        print("Total profit (or loss): $" + str(sum(total)))
        
repeat = "yes"

while repeat.lower().strip() == "yes":
    total = []
    year = 1
    net_profit = 0
    
    while net_profit < 5 and sum(total) <= 250000:
    #random_num = random.randrange(1,10)
    #while random_num >= 6:
    #for i in range(1, random_num):
        if year % 3 == 0: # Focus on crabs every 3 years
            crab_ops(year)
        else: # Focus on salmon every 1-2 years
            salmon_ops(year)
        year += 1
    
    print()
    check1()
    check2()
    check3()
        
    # Ask user if they want to repeat the simulation   
    repeat = input("\nWould you like to run another simulation (yes/no)? ")