import urban_planning 
import random

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def student_algorithm(option1, option2):
    """Students define their own algorithm here."""
    # print('Write your own algorithm here!')

    rank1 = -1
    rank2 = -1

    possible_ev = urban_planning.vehicles["Emergency Vehicle"]
    if option1[0] in possible_ev:
        rank1 = 1
    elif option2[0] in possible_ev:
        rank2 = 1

    possible_public_v = urban_planning.vehicles["Public Transport"]
    if option1[0] in possible_public_v:
        rank1 = 2
    elif option2[0] in possible_public_v:
        rank2 = 2

    possible_pedestrian = urban_planning.non_vehicles["Pedestrian"]
    if option1[0] in possible_pedestrian:
        rank1 = 3
    elif option2[0] in possible_pedestrian:
        rank2 = 3

    possible_cyclist = urban_planning.vehicles["Cyclist"]
    if option1[0] in possible_cyclist:
        rank1 = 4
    elif option2[0] in possible_cyclist:
        rank2 = 4   

    possible_priv_v = urban_planning.vehicles["Private Vehicle"]
    if option1[0] in possible_priv_v:
        rank1 = 5
    elif option2[0] in possible_priv_v:
        rank2 = 5

    possible_animal = urban_planning.non_vehicles["Animal"]
    if option1[0] in possible_animal:
        rank1 = 6
    elif option2[0] in possible_animal:
        rank2 = 6

    possible_robot = urban_planning.non_vehicles["Robot"]
    if option1[0] in possible_robot:
        rank1 = 7
    elif option2[0] in possible_robot:
        rank2 = 7

    if rank1 <= rank2:
        return option1, option2
    else:
        return option2, option1


    

# Example
def pick_emergancy_vehicle(option1, option2):
    """This funcion always picks the emergancy vehicle first"""

    # options contain [type of vehicle/non-vehicle, modifyer (ie type of pedestrian)]
    possible_ev = urban_planning.vehicles["Emergancy Vehicles"]
    if option1[0] in possible_ev:
        if option2[1] in possible_ev: ## both ev
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2 ## option1 ev
    elif option2[0] in possible_ev:  
        return option2, option1 ## option2 ev
    else:
        selected = random.choice([option1, option2]) ## neither ev
        if option1 == selected:
            return selected, option2
        else:
            return selected, option1

        
        

# Function to run the simulation using a given algorithm
# Run the activity
#urban_planning.run_activity()

# Run the activity using the example algorithm
# print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
# urban_planning.run_activity(num_scenarios=25, decision_function = student_algorithm)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")
print("\n🔹 Running Student Algorithm")
urban_planning.run_activity(num_scenarios=25, decision_function = student_algorithm)
