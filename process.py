log_file = open("um-server-01.txt")

# function that reports the sales sold
def sales_reports(log_file):
    # for loop that loops through every line in the file
    for line in log_file:
        # strips all the deadspace 
        line = line.rstrip()
        # variable that selects the day in the array and saves it as a value
        day = line[0:3]
        #checks to see if the day equals what we want and prints it
        if day == "Mon":
            print(line)


sales_reports(log_file)
