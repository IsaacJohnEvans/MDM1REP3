from CurrentModel import StateChanges
"""
Define the initial values and coefficients for the model.
These should create a boom bust curve.
"""
#The initial states of the users.
POPULATION = 10**8
ActiveUsers = 0
DormantUsers = 0
Influencers = 100
NonUsers = POPULATION - Influencers
Time = 520
#The coefficients for the various state changes.
ActiveToDormant = 0.145
ActiveToInfluencer = 0.0001
InfluencerToActive = 0.1
DormantToActive = 0.1
DormantToNonUsers = 0.25
RecruitmentRateFromFriends = 10
RecruitmentRateFromInfluencers = 100
#Calling the main function to run the model.
StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers,
             ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Time)