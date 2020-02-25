from CurrentModel import StateChanges
ActiveToDormant = 0.1
ActiveToInfluencer = 0.0001
InfluencerToActive = 0.1

DormantToActive = 0.1
DormantToNonUsers = 0.1

RecruitmentRateFromFriends = 1
RecruitmentRateFromInfluencers = 10
StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
             DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers)