import arff

# Write training and testing files


training = arff.write("training.arff.txt"))

"""
# Read in original file
with open("pp-complete.csv", "rb") as f:
    csvreader = csv.reader(f, delimiter=",")
    # Split up data
    for row in csvreader :
        if "2015" in row[2]:
            print "2015 spotted"
            testing.writerow(row)
        else:
            print "writing to training"
            training.writerow(row)
          
"""        

            
    

    
    
    


