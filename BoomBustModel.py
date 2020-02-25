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
Time = 150
#The coefficients for the various state changes.
ActiveToDormant = 0.1
ActiveToInfluencer = 0.0001
InfluencerToActive = 0.1
DormantToActive = 0.1
DormantToNonUsers = 0.1
RecruitmentRateFromFriends = 1
RecruitmentRateFromInfluencers = 10
#Calling the main function to run the model.
StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers,
             ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Time)