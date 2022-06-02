def getBranch(rollno):
        key = rollno[4:6]
        branch = ""
        Dict = { "AA" : "ECE", "AB" : "Manu", "A1" : "Chemical", "A2" : "Civil", "A3" : "EEE",
        "A4" : "Mech", "A5" : "Pharma", "A7" : "CSE", "A8" : "ENI", "B1" : "MSc BIO",
        "B2" : "MSc Chem", "B3" : "MSc Eco", "B4" : "MSc Mathematics", "B5" : "MSc Physics" }
        branch = Dict[key]
        return branch

def firstBranch (rollno) :
    try : 
        firstBranch = getBranch (rollno)
        return firstBranch
    except:
        firstBranch = "Invalid Branch"
        return firstBranch
    
def secondBranch (rollno) :
    if rollno[6] == "P" :
        #Single degree (Practice school)
        return "NA"
    elif rollno[6] != "P" :
        #Dual degree
        temp = ""
        temp = rollno[2:]
        secondBranch = getBranch (temp)
        return secondBranch

def obtain_year(rollno):
    try : 
        year = int (rollno[0:4])
        return year
    except :
        print("Not working")