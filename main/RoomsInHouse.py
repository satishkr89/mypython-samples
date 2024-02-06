# To Do:
# Try to code for this scenario:

# You initially have two rooms in your house.
# You construct three more rooms on the first floor.
# Tell the total number of rooms that you have in your home now.
# Now... you just changed your mind and want to have an open space desgin on your first floor. so you break the wall between 
# two of the rooms on your first floor and make it one large room. So that now you have two rooms on the ground floor and two rooms on the first floor.
# Tell your friend (print out) that you have changed your house design to an open space plan.
# Also tell him the number of rooms that you had earlier in your home and the new number of rooms that you have now.

rooms_in_home=2
nw_
newly_built_rooms_first_floor=3

total_rooms_in_home = rooms_in_home + newly_built_rooms_first_floor

print(f"Initially we had {rooms_in_home}, then we build {newly_built_rooms_first_floor} rooms on first floor")

print(f"now we have {total_rooms_in_home} rooms in our home")

post_remodel_room_onFirstfloor= newly_built_rooms_first_floor - 1

print("we remodelled and breakdown walls between two rooms to make one big room on first floor")

print(f"now we have {post_remodel_room_onFirstfloor} room on first floor")

total_rooms_in_home = rooms_in_home + post_remodel_room_onFirstfloor

print(f"now we have {total_rooms_in_home} rooms in our home")

