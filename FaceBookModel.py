from CurrentModel import StateChanges
"""
Define the initial values and coefficients for the model.
These should create a boom bust curve.
"""
#The initial states of the users.
POPULATION = 6*10**9
ActiveUsers = 0
DormantUsers = 0
Influencers = 100
NonUsers = POPULATION - Influencers
Time = 676
#The coefficients for the various state changes.
ActiveToDormant = 0.05
ActiveToInfluencer = 0.0001
InfluencerToActive = 0.21
DormantToActive = 0.05
DormantToNonUsers = 0.25
RecruitmentRateFromFriends = 15
RecruitmentRateFromInfluencers = 100
#Calling the main function to run the model.
StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers,
             ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Time)