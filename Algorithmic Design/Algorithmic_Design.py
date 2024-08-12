# Cooper Herman
# 7.29.2024 - 8.8.2024
# A project intended for staff of FLVS (Faithful Lives Veterinary Shelter) to determine availability of animal slots and store previous animal occupants **SECURITY CODE IS 57092**

# Herman Studios 2024

import re

def canOccupy(targetCage):  # Determines availability of target cage
    canOccupy = False; currentOccupants = 0
    
    for i in identifiers: # Adds to current occupants if cage identifier matches target cage
        if i[0] == str(targetCage):
            currentOccupants += 1
            
    if cageCount[int(targetCage)] > currentOccupants: # If current occupants are less than the number of target cages, then animal can occupy. Return True
        canOccupy = True

    return canOccupy

def removeAnimal(identifier):
    global curFunds
    # Slightly complex way of ensuring user input is number/number/number. A more complex value could be used to ensure there are two, two, and four values in between the '/'s
    date = r"^\d+/\d+/\d+$"; paidFee = 0
    # Paid fee is added to current funds
    userInp = input("\nFLVS - Remove Animal\n-- -- -- -- -- -- --\nCause:\n(1) Euthanasia\n(2) Adoption\n(3) Natural Death\n(e) exit")
    
    if userInp.isdigit():
        if userInp == '1':
            removalReason = "euthanasia" # Shelter-inflicted death
        elif userInp == '2':
            removalReason = "adoption" # Animal adoption
            userInp = 'a'
            while not userInp.isdigit():
                userInp = input("\nFLVS - Remove Animal\n-- -- -- -- -- -- --\nWhat adoption fee was paid?\n\nEnter a numeric value:") # For each animal adopted, there is a fee. Animal value typically related to breed and species
            paidFee = userInp
        elif userInp == '3':
            removalReason = "natural death" # Natural animal death
    else:
        mainMenu() # Input does not have to be specifically e to return to main menu, but rather any non-numeric value
        return
        
    try:
        weightOnEntry.pop(identifiers.index(identifier)); currentWeight.pop(identifiers.index(identifier)); identifiers.remove(identifier); removedReasons.append(removalReason); removedIdentifiers.append(identifier); curFunds += int(paidFee)
    except:
        input("\nFLVS - Remove Animal\n-- -- -- -- -- -- --\nAn unexpected error has occured. Select data may be corrupt.")
        # Data may be corrupt as the try except logic goes through the function and executes until an error occurs. This may result in only partial animal information being removed
        mainMenu()
        return
    
    while True:
        userInp = input("\nFLVS - Remove Animal\n-- -- -- -- -- -- --\nWhat is the date?\nmonth/day/year")
        if re.search(date, userInp):
            break

    removedOccurrences.append(userInp)
    input("\nFLVS - Remove Animal\n-- -- -- -- -- -- --\nAnimal removed successfully.")
    mainMenu()
    return

def denial(reason):
    global denials
    date = r"^\d+/\d+/\d+$"
    while True:
        userInp = input("\nFLVS - Deny Animal\n-- -- -- -- -- --\nWhat is the date?\nmonth/day/year")
        if re.search(date, userInp):
            break
     
    denialOccurences.append(userInp)
    denialReasons.append(reason)
    denials += 1
    input("\nFLVS - Remove Animal\n-- -- -- -- -- -- --\nDenial logged.")
    
    mainMenu()

def checkOut():
    myBool = False
    while True:
        if myBool == False:
            userInp = input("\nFLVS - Check-Out\n-- -- -- -- -- -\nEnter target animal's identifier:")
            myBool = True
        else:
            userInp = input("\nFLVS - Check-Out\n-- -- -- -- -- -\nIdentifier not found. Please try again:")
        
        if userInp in identifiers:
            removeAnimal(userInp)
            return
        
        if userInp == 'e':
            input("Action aborted. You will not be returned to the main menu.\n\nEnter any input to continue.")
            mainMenu
            return()

def newAnimal():
    newAnimalType = ""; newAnimalTypeName = ""; newAnimalEntryWeight = ""; assignedCage = 5; targetCage = 0
    
    while True:
        userInp = input("\nFLVS - New Animal\n-- -- -- -- -- --\nWhat type of animal are you checking in?\n(1) Dog\n(2) Cat\n(3) Bird\n(4) Reptile\n(e) exit")
        if userInp.isdigit():
            try:
                int(userInp)
                if 0 < int(userInp) < 5:
                    break
            except:
                myVar = 0
        else:
            mainMenu()

    if userInp == '1':
        newAnimalType = 'a'
        newAnimalTypeName = "dog"
    elif userInp == '2':
        newAnimalType = 'b'
        newAnimalTypeName = "cat"
    elif userInp == '3':
        newAnimalType = 'c'
        newAnimalTypeName = "bird"
    elif userInp == '4':
        newAnimalType = 'd'
        newAnimalTypeName = "reptile"
    
    while True:
        newAnimalEntryWeight = input("\nFLVS - New Animal\n-- -- -- -- -- --\nWhat is the " + newAnimalTypeName + "'s weight? (lbs.)")
        if newAnimalEntryWeight.isdigit():
            break
    if newAnimalTypeName != "reptile" and newAnimalTypeName != "bird": # Determines target cage based on animal weight
        if int(newAnimalEntryWeight) < 21:
            targetCage = 1
        elif 20 < int(newAnimalEntryWeight) < 41:
            targetCage = 2
        elif 40 < int(newAnimalEntryWeight) < 90:
            targetCage = 3
        else:
            input("\nFLVS - New Animal\n-- -- -- -- -- --\nAnimal outside weight capacity.")
            mainMenu()
            return
    elif newAnimalTypeName == "reptile":
        targetCage = 0
    elif newAnimalTypeName == "bird":
        targetCage = 4
    
    boolCanOccupy = canOccupy(targetCage)
    if boolCanOccupy == False:
        if targetCage in [0, 3, 4]: # If animal is a reptile, is too large for smaller cages, or is a bird, then no cage will fit them. The 3 value would need to be changed if additional cages were added with larger capacities to the largest all-purpose cage. If you were to add multiple reptile-specific or bird-specific cages, then these would need to be added to the list as well
            userInp = input("\nFLVS - New Animal\n-- -- -- -- -- --\nUnable to find target cage for animal. Continuing will result in no cage being assigned.\n\nContinue? (y/n)")
            if userInp == 'y':
                assignedCage = 5 # This will cause no errors in the system, but will display no cage in select scenes
            else:
                input("\nFLVS - New Animal\n-- -- -- -- -- --\nYou will now be returned to the main menu.\n\nEnter any input to continue.")
                denial("cage")
                return
        else:
            while True:
                userInp = input("\nFLVS - New Animal\n-- -- -- -- -- --\nUnable to find target cage for animal (" + str(targetCage) + ").\n(1) Look for alternative cage\n(2) Continue without assigning\n(e) exit")
                if userInp.isdigit():
                    break
                
            if userInp == '1':
                if targetCage == 1:
                    boolCanOccupy = canOccupy(2)
                    if boolCanOccupy == True:
                        assignedCage = 2
                    else:
                        boolCanOccupy = canOccupy(3)
                        if boolCanOccupy == True:
                            assignedCage = 3
                        else:
                            userInp = input("\nFLVS - New Animal\n-- -- -- -- -- --\nUnable to find target cage for animal (2 or 3). Continuing will result in no cage being assigned.\n\nContinue? (y/n)")
                            if userInp == 'y':
                                assignedCage = 5
                            else:
                                denial("cage")
                                return                      
                elif targetCage == 2:
                    boolCanOccupy = canOccupy(3)
                    if boolCanOccupy == True:
                        assignedCage = 3
                    else:
                        userInp = input("\nFLVS - New Animal\n-- -- -- -- -- --\nUnable to find target cage for animal (3). Continuing will result in no cage being assigned.\n\nContinue? (y/n)")
                        if userInp == 'y':
                            assignedCage = 5
                        else:
                            denial("cage")
                            return
                    
            elif userInp == '2':
                assignedCage = 5
                
            else:
                input("Action aborted. You will be returned back to the main menu.\n\nEnter any input to continue.")
      
    else:
        assignedCage = targetCage
        
    latest = identifiers[len(identifiers) - 1]   
    latestIdentifier = latest[2:]
    for i in identifiers: # Finds the most recent animal admitted. If you remove the latest animal and create a new one, it will find the highest number regardless
        if int(i[2:]) > int(latestIdentifier):
            latestIdentifier = i[2:]
    for i in removedIdentifiers: # Finds the most recent animal admitted. If you remove the latest animal and create a new one, it will find the highest number regardless
        if int(i[2:]) > int(latestIdentifier):
            latestIdentifier = i[2:]
                   
    if weeklyOutgoings > weeklyRevenue + curFunds:
        identifiers.pop()
        input("\nFLVS - New Animal\n-- -- -- -- -- --\nInsufficient shelter funds. You will be directed to the denial page.\n\nEnter any input to continue")
        denial("budget")
        return

    newIdentifier = str(assignedCage) + newAnimalType + str(int(latestIdentifier) + 1)
    identifiers.append(newIdentifier)
    if assignedCage == '5':
        input("\nFLVS - New Animal\n-- -- -- -- -- --\n" + newAnimalTypeName[0].upper() + newAnimalTypeName[1:] + " assigned no cage (numeric value 5) and identifier " + newIdentifier + ".\n\nCheck-in complete.")
    else:
        input("\nFLVS - New Animal\n-- -- -- -- -- --\n" + newAnimalTypeName[0].upper() + newAnimalTypeName[1:] + " assigned cage num " + str(assignedCage) + " and identifier " + newIdentifier + ".\n\nCheck-in complete.")
    weightOnEntry.append(latestIdentifier + newAnimalEntryWeight)
    currentWeight.append(latestIdentifier + newAnimalEntryWeight)
    mainMenu()
 
def shelterData():
    global employees, weeklyRevenue, curFunds, employeeCost, denials
    occupants = 0; animalOccurence = [0, 0, 0, 0]; cageOccurence = [0, 0, 0, 0, 0]; weeklyOutgoings = determineBudget("current", employees, 0); referenceList = ['a', 'b', 'c', 'd']; animalTypeList = ["Dog", "Cat", "Bird", "Reptile"]; noCage = 0; lastIndex = ""
    
    for i in identifiers:
        if i[0] != '5':
            occupants += 1 # For each registered animal, add to occupant count
        else:
            noCage += 1
        animalOccurence[referenceList.index(i[1])] += 1
        cageOccurence[int(i[0])] += 1
        
    totalSlots = cageCount[0] + cageCount[1] + cageCount[2] + cageCount[3] + cageCount[4] # Total number of cage slots across all types
    slotOccupation = occupants/totalSlots
    
    userInp = input("\nFLVS - Shelter Data\n-- -- -- -- -- -- -\nGeneral Weekly Profit: $" + str(weeklyRevenue - weeklyOutgoings) + "\nCurrent Funds: $" + str(curFunds) + "\nSlot Occupation: %" + str(f"{slotOccupation:.2f}") + "\nMost Common Animal: " + animalTypeList[animalOccurence.index(max(animalOccurence))] + "\n\n(1) Advanced Budget Options\n(2) Slot Management\n(3) Removed Animals\n(4) Denials\n(e) exit")
    
    if userInp.isdigit():
        if userInp == '1': # Budget administration and viewing. Available changes include weekly outgoings, weekly revenue, current funds, employee count, and employee cost per week
            weeklyOutgoings = determineBudget("current", employees, 0)
            userInp = input("\nFLVS - Shelter Data > Advanced Budget Options\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- ---\n(1) Current Funds: " + str(curFunds) + "\n(2) Weekly Revenue: " + str(weeklyRevenue) + "\n(-) Weekly Outgoings: " + str(weeklyOutgoings) + "\n\n(3) Employees: " + str(employees) + "\n(4) Weekly Cost Per Employee: " + str(employeeCost))
            if userInp.isdigit():
                selection = userInp
                while True:
                    userInp = input("Enter new numeric value:")
                    if userInp.isdigit():
                        break
                    
                if selection == '1':
                    curFunds = int(userInp) # In realistic setting, this would be connected to bank account
                elif selection == '2':
                    weeklyRevenue = int(userInp) # In realistic setting, this would be calculated from inputed revenue sources with their respective values and reocurring periods
                elif selection == '3':
                    employees = int(userInp) # In realistic setting, employee list with name, position, and respective salary/hourly pay included
                elif selection == '4':
                    employeeCost = int(userInp) # In realistic setting, this would not exist but rather be attached to each employee with unique value
                input("\nFLVS - Shelter Data > Advanced Budget Options\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- --\nChanges made successfully.")
                shelterData()
                return
            else:
                shelterData()
                return
        elif userInp == '2': # Slot occupation and cage values viewing and administration respectively
            userInp = input("\nFLVS - Shelter Data > Slot Occupation\n-- -- -- -- -- -- -- -- -- -- -- -- -\nReptile Cages: " + str(cageOccurence[0]) + "/" + str(cageCount[0]) + "\nSize 1 Cage: " + str(cageOccurence[1]) + "/" + str(cageCount[1]) + "\nSize 2 Cage: " + str(cageOccurence[2]) + "/" + str(cageCount[2]) + "\nSize 3 Cage: " + str(cageOccurence[3]) + "/" + str(cageCount[3]) + "\nBird Cage: " + str(cageOccurence[4]) + "/" + str(cageCount[4]) + "\n\n(1) Change Reptile Cage Count\n(2) Change Size 1 Cage Count\n(3) Change Size 2 Cage Count\n(4) Change Size 3 Cage Count\n(5) Change Bird Cage Count")
            if userInp.isdigit():
                if 0 < int(userInp) < 6:
                    selection = userInp
                    while True:
                        userInp = input("\nFLVS - Shelter Data > Slot Occupation\n-- -- -- -- -- -- -- -- -- -- -- -- -\nWhat is the new cage count?")
                        if userInp.isdigit():
                            if int(userInp) >= 0:
                                cageCount[int(selection) - 1] = int(userInp)
                                shelterData()
                                return
                else:
                    shelterData()
                    return
            else:
                shelterData()
                return
        elif userInp == '3':
            if len(removedIdentifiers) == 0:
                input("\nFLVS - Shelter Data > Removed Animals\n-- -- -- -- -- -- -- -- -- -- -- -- -\nNo removed animals. You will be returned to the previous page.\n\nEnter any input to continue.")
                shelterData()
                return
            for i in removedIdentifiers:  # Lists through all removals
                if removedIdentifiers[len(removedIdentifiers) - 1] == i:
                    lastIndex = "\nLast removal. Proceeding will bring you to the previous page."
                userInp = input("\nFLVS - Shelter Data > Removed Animals\n-- -- -- -- -- -- -- -- -- -- -- -- -\n" + i + "\nCause: " + removedReasons[removedIdentifiers.index(i)] + "\nRemoved on: " + removedOccurrences[removedIdentifiers.index(i)] + lastIndex + "\n\n(enter) Continue\n(e) exit")
                if userInp == 'e':
                    shelterData()
                    return
                
        elif userInp == '4':
            if len(denialReasons) == 0:
                input("\nFLVS - Shelter Data > Denials\n-- -- -- -- -- -- -- -- -- --\nNo denied animals. You will be returned to the previous page.\n\nEnter any input to continue.")
                shelterData()
                return
            for i in range (denials): # Lists through all denials
                if i == denials - 1:
                    lastIndex = "\nLast denial. Proceeding will bring you to the previous page."
                userInp = input("\nFLVS - Shelter Data > Denials\n-- -- -- -- -- -- -- -- -- --\n#" + str(i + 1) + "\nCause: " + denialReasons[i] + "\nDenied on: " + denialOccurences[i] + lastIndex + "\n\n(enter) Continue\n(e) exit")
                if userInp == 'e':
                    shelterData()
                    return
    else:
        mainMenu()
        return
        
    mainMenu()
    
def animalDatabase(): # Provides every animal and its information
    printCage = "No Cage"; printType = "No Animal"; lastAnimal = ""; v = 0
    
    for i in identifiers: # Repeats for each animal
        if i[0] == '0':
            printCage = "Reptile Cage"
        elif i[0] == '1':
            printCage = "Size 1 Cage"
        elif i[0] == '2':
            printCage = "Size 2 Cage"
        elif i[0] == '3':
            printCage = "Size 3 Cage"
        elif i[0] == '4':
            printCage = "Bird Cage"
        elif i[0] == '5':
            printCage = "No Cage"
            
        if i[1] == 'a':
            printType = "Dog"
        elif i[1] == 'b':
            printType = "Cat"
        elif i[1] == 'c':
            printType == "Bird"
        elif i[1] == 'd':
            printType == "Reptile"
        
        currentAnimal = identifiers[v]
        animalCurrentWeight = currentWeight[v]
        animalWeightOnEntry = weightOnEntry[v]
        if i == identifiers[len(identifiers) - 1]:
            lastAnimal = "\nLast index. Proceeding will bring you to the main menu."
        # Prints animal information
        userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\n#" + str(v + 1) + "\n" + printType + "\n" + printCage + "\nCurrent Weight: " + animalCurrentWeight[1:] + " lbs.\nWeight on entry: " + animalWeightOnEntry[1:] + " lbs.\nIdentifier: " + i  + lastAnimal + "\n\n(c) Change\n(enter) Continue\n(e) Exit")
        if userInp.isdigit():
            mainMenu()
            return
        if userInp == 'c':
            relatedIdentifier = identifiers[v]
            while True:
                userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nWhat would you like to change?\n(1) Current Cage\n(2) Current Weight\n(3) Remove Animal\n(e) exit") # Provides ability to change animal information
                if userInp.isdigit():
                    if 0 < int(userInp) < 4:
                        if userInp == '1':
                            while True:
                                userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nWhat cage has this animal been moved to?\n(0) Reptile Cage\n(1) Cage 1\n(2) Cage 2\n(3) Cage 3\n(4) Bird Cage") # Change cage occupancy status
                                if userInp.isdigit():
                                    if -1 < int(userInp) < 5:
                                        canOccupyBool = canOccupy(userInp)
                                        if canOccupyBool == True:
                                            canMove = determineBudget("new", employees, cageCost[int(userInp) - 1]) # Determines availability in target cage
                                            if canMove == True:
                                                identifiers[v] = userInp + relatedIdentifier[1:]
                                                input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nData successfully changed.")
                                                break
                                            else:
                                                userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nShelter income does cannot support movement to cage size. Are you sure you want to continue?\n\n(y/n)")
                                                if userInp == 'y':
                                                    identifiers[v] = userInp + relatedIdentifier[1:]
                                                    break
                                                else:
                                                    input("Action aborted. You will be returned to the animal database.")
                                                    break
                                        else:
                                            userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nUnable to occupy cage: cage type slots are full.") # If no room in target cage, inform user and do not change information
                                            break
                        elif userInp == '2':
                            while True:
                                userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nWhat is the animal's weight? (lbs.)") # Update animal information to current weight. Does not change weight on entry
                                if userInp.isdigit():
                                    currentWeight[v] = currentAnimal[2:] + userInp
                                    break
                        elif userInp == '3':
                            userInp = input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nAre you sure you want to remove this animal? You cannot undo this action.\n(y/n)") # Remove animal
                            if userInp == 'y':
                                removeAnimal(identifiers[v])
                                return
                            else:
                                input("\nFLVS - Animal Database\n-- -- -- -- -- -- -- -\nAction aborted.")
                    break               
                else:
                    break
        elif userInp == 'e':
            mainMenu()
            return
        v += 1
        
    mainMenu() # End of function   

def mainMenu():
    userInp = input("\nFaithful Lives Veterinary Shelter\n-- -- -- -- -- -- -- -- -- -- --\n(1) Check in Animal\n(2) Check out Animal\n(3) Animal Database\n(4) Shelter Data\n(e) exit")
    if userInp.isdigit(): # Calls on various functions based on user input
        if userInp == '1':
            newAnimal()
        elif userInp == '2':
            checkOut()
        elif userInp == '3':
            animalDatabase()
        elif userInp == '4':
            shelterData()
    else:
        print("Goodbye.")

def staffSecurity(): # Code is 57092
    userInp = input("Faithful Lives Veterinary Shelter\n-- -- -- -- -- -- -- -- -- -- --\nEnter staff security code:")
    return userInp

def determineBudget(action, employees, newAmount): # Revenue is a static number realistically influenced by things like sponsors and government funding. Can be manually changed in code or through project (reset in each project instance to code specified value)
    global cageCost
    cageCost = [60, 60, 80, 100, 80] # Cost of animal keep per week, increased for each cage. Realistically, this would be based off specific weight and not cage, but I'm lazy. Wouldn't be crazy difficult to implement this system
    outgoings = 0
    if action == "current": # Determines current budget situation
        for i in identifiers:
            if i[0] == '0':
                outgoings += 60
            elif i[0] == '1':
                outgoings += 60
            if i[0] == '2':
                outgoings += 80
            elif i[0] == '3':
                outgoings += 100
            elif i[0] == '4':
                outgoings += 80
        return outgoings + (employees * employeeCost)
    elif action == "new": # Determines current budget situation, with additional numeric value. Returns True value if value fits in budget, False otherwise
        for i in identifiers:
            if i[0] == '0':
                outgoings += 60
            elif i[0] == '1':
                outgoings += 60
            if i[0] == '2':
                outgoings += 80
            elif i[0] == '3':
                outgoings += 100
        if (outgoings + newAmount) > curFunds + weeklyRevenue:
            return False
        else:
            return True
    
def main():
    global removedIdentifiers, removedReasons, removedOccurrences, identifiers, cageCount, weightOnEntry, currentWeight, cageAvailable, denialReasons, denialOccurences, employees, employeeCost, curFunds, weeklyRevenue, weeklyOutgoings, denials # Changes specified variables to global, so that they may be accessed and changed throughout the project
    
    # Income consists of donations, and adoption & surrender fees]
    employees = 8 # A more complex system would need to be in place to keep track of individual payrolls and positions, but currently everyone is paid 30,000 per anum. This value can be changed in the employeeCost variable below
    employeeCost = 576 # An employee's weekly pay, which can be changed here or in the project with no issue
    curFunds = 1350 # Cash funds on project start
    weeklyRevenue = 4909 # Revenue per 7 days
    
    # a - dog, b - cat, c - bird, d - reptile
    removedIdentifiers = [] # All removed animals and their respective identifier
    removedReasons = [] # Causes of removal. Separate from denials, as denials are refusals to accept an animal, while removals are occurrences of an animal being removed from the shelter
    removedOccurrences = [] # Dates of removal
    identifiers = ["3a1", "1b2", "1b3", "1a4", "3a5", "1b6", "0d7", "3a8"] # These values can be changed with no issue. Program automatically determines assigned cage and animal type if input is correct. Ensure input follows identifier guideline listed below
    # 0a1 - Example - Guideline - Assigned Cage (numeric value 0-4), Animal Type (character value a, b, c, or d), Animal Count (numeric value equal to its order in all animals accepted from 1 to infinity) - Zero non-numeric values can be included past the Animal Count
    # Following standard cage size standards: 0 - 48"x34" (-20 lbs.) | 1 - 17"x96" (-20 lbs.) | 2 - 28"x96" (21-50 lbs.) | 3 - 40"x96" (51-90 lbs.) | 4 - 28"x64" (-20 lbs.)
    # ^ Length x Height in Inches             ^ Glass cage intended for reptiles                ^ Standard cages are built into building              ^ Tall cage intended for birds
    cageCount = [8, 10, 10, 10, 4] # Each index value represents number of cages for corresponding cage size/type
    
    weeklyOutgoings = determineBudget("current", employees, 0) # Determines weekly spendings on project start. This was put further down due to identifiers needing defined

    weightOnEntry = ["147", "218", "311", "47", "561", "612", "70", "864"] # Weight (in pounds) upon entry to the shelter. First numeric value equal to related indentifier's number
    currentWeight = ["147", "218", "311", "47", "561", "612", "70", "864"] # Current weight (in pounds). First numeric value equal to related indentifier's number
    
    denials = 0
    denialReasons = [] # Reasons for animal denial
    denialOccurences = [] # When the denials occurred
    
    while True: # Ensures user is staff member
        userInp = staffSecurity()
        try:
            if int(userInp) == 57092:
                break
        except:
            True
                 
    mainMenu()  # Calls on main menu function once verified staff member

main()
