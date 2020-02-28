from CurrentModel import StateChanges
"""
Define the initial values and coefficients for the model.
These should create a boom bust curve.
"""
#The initial states of the users.
POPULATION = 10**9
ActiveUsers = 0
DormantUsers = 0
Influencers = 10**4
NonUsers = POPULATION - Influencers
Time = 676
#The coefficients for the various state changes.
ActiveToDormant = 0.1
ActiveToInfluencer = 0
InfluencerToActive = 0.01
DormantToActive = 0.01
DormantToNonUsers = 0.01
RecruitmentRateFromFriends = 1
RecruitmentRateFromInfluencers = 1000
#Calling the main function to run the model.
StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers,
             ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Time)