from CurrentModel import StateChanges
"""
Define the initial values and coefficients for the model.
These should create a boom bust curve.
"""
#The initial states of the users.
POPULATION = 10**4
ActiveUsers = 0
DormantUsers = 0
Influencers = 100
NonUsers = POPULATION - Influencers
Time = 100000
#The coefficients for the various state changes.
ActiveToDormant = 0.1
ActiveToInfluencer = 0.01
InfluencerToActive = 0.01
DormantToActive = 0.2
DormantToNonUsers = 0
RecruitmentRateFromFriends = 1
RecruitmentRateFromInfluencers = 3
#Calling the main function to run the model.
StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers,
             ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Time)