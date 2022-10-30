lifts = []

while True:
    print("Do you want to enter a new days lifting?")
    n = input("y/n:")

    if n.strip() == "y":
        date = input("enter date: ")
        lifts.append(input("Enter exercise: ")) 

        while input("Do you want to enter a new exercise? (y/n)") == "y":
            inpt = input("Enter another exercise:")
            lifts.append(inpt) 

        for lift in lifts:
            print("enter values for", lift, "(whole kilos):")
            lift_sets = input("sets:")
            lift_reps = input("reps:")
            lift_load = input("load:")
            total_reps = int(lift_sets) * int(lift_reps)
            total_load = int(total_reps) * float(lift_load)        

            more_lines = f"{lift} on {date} with {lift_load} kgs sets: {lift_sets} reps: {lift_reps} total reps: {total_reps} total load: {total_load:g}"

            with open('lifting_log.txt', 'a') as f:
                f.write('\n')
                f.writelines(''.join(more_lines))

        lifts.clear()

    elif n.strip() == "n":
        quit()
