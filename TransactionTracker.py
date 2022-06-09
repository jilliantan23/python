import csv

repeat = "yes"
record = 0
pending_amount = 0.0
unique_list = []
id_list = []

print("Welcome to the transaction tracker!\n")
while repeat.lower().strip() == "yes":
    mode = input("What would you like to perform (import/statistics)? ")
    unique_list = []
    # MODE: IMPORT
    if mode.lower().strip() == "import":
        try:
            # Create a CSV file for transaction records
            with open("transaction_records.csv", "w") as file:
                writer = csv.writer(file, lineterminator = "\n")
                header = ["Transaction ID", "Vendor Name", "Status", "Due Date", "Amount"]
                writer.writerow(header)
            
            # Import file data to transaction records file   
            with open("transaction_records.csv", "r") as file:
                file_contents = csv.reader(file)
                for line in file_contents:
                    transaction_id = line[0]
                    id_list.append(transaction_id)
                    unique_list.append(transaction_id)
            
            # Ask user for file name of file to be imported
            import_name = input("Which file would you like to import? ")
            unique_list = []
            
            with open(import_name, "r") as file:
                reader = csv.reader(file)
                for line in reader:
                    transaction_id = line[0]
                    print(transaction_id)
                    # Check for duplicate transactions
                    if transaction_id in id_list:
                        print("Data for ID " + str(transaction_id) + " already in transaction records.")                    
                    # Allow user to load new transaction data
                    else:
                        id_list.append(transaction_id)
                        unique_list.append(transaction_id)
                        record += 1
                        with open("transaction_records.csv", "a") as transaction_file:
                            writer = csv.writer(transaction_file, lineterminator = "\n")
                            writer.writerow(line)
                        a_set = set(unique_list) # Create a set of values from the imported file
                        unique_num = len(a_set) # Count the number of unique values from the imported file
                print(unique_num, "transaction records successfully loaded.\n")
                
        except:
            # Print error message when user enters a file that does not exist
            print("Sorry, the file could not be not found. Please try again.\n")
                
    # MODE: STATISTICS
    elif mode.lower().strip() == "statistics":
        if record != 0:
            # Read the file for transaction records
            with open("transaction_records.csv", "r") as file:
                reader = csv.reader(file)
                for line in reader:
                # Find the total dollar amount pending
                    if "PENDING" in line:
                        pending_amount += float(line[4])
                print("Number of lifetime transactions: " + str(record))
                print("Total dollar amount pending: " + str(pending_amount) + "\n")
        # No current existing records
        else:
            print("Sorry, no transaction data was loaded yet. Please try again.\n")
    
    # MODE: NEITHER IMPORT NOR STATISTICS
    else:
        print("The requested analysis is not supported. Please try again.\n")
                        
    repeat = input("Would you like to run any further analyses (yes/no)? ")
    print()