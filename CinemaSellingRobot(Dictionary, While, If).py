films = {
    "Tenet": [12,5],
    "Speed And Furious": [18,5],
    "Frozen": [6,10],
    "The Avengers":[12, 2],
    "Inception": [12, 3]
    }

while True:

    print("We have films as below, and the numbers are the seat remaining.")
    for key in films:
        print(key, films[key][1])
        
    choice = input("What film would you like to watch?: ").strip().title()

    # check the film list
    
    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age

        if age >= films[choice][0]:

            # check enough seats

            num_seats = films[choice][1]
            tickets = int(input("How many tickets do you want?: "))
            
            if num_seats > tickets:
                print("Enjoy the film! Next one, please.")
                films[choice][1] = films[choice][1] - tickets
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("Sorry, we don't have that film...")
    
