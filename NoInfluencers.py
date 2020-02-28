from CurrentModel import StateChanges
"""
Define the initial values and coefficients for the model.
These should create a boom bust curve.
"""
#The initial states of the users.
POPULATION = 10**5
ActiveUsers = 100
DormantUsers = 0
NonUsers = POPULATION - ActiveUsers
Time = 600
#The coefficients for the various state changes.
ActiveToDormant = 0.1
DormantToActive = 0.1
DormantToNonUsers = 0.5
RecruitmentRateFromFriends = 100
#Calling the main function to run the model.
StateChanges(ActiveToDormant, 0, 0, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, 0,
             ActiveUsers, DormantUsers, 0, NonUsers, POPULATION, Time)