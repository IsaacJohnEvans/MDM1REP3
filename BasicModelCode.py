

def StateChanges():
    """
    This defines initial population conditions and coefficients for the movement of users.
    A for loop then calculates the change in each type of user and calls the function to print the number of each type of user.
    """
    #These coefficients currently produce nonsense numbers.
    ActiveToInfluencer = 0.01
    InfluencerToActive = 0.005
    ActiveToDormant = 0.1

    DormantToActive = 0.05
    DormantToNonUsers = 0.2

    RecruitmentRateFromFriends = 1
    RecruitmentRateFromInfluencers = 10

    POPULATION = 10**9
    ActiveUsers = 0
    DormantUsers = 0
    Influencers = 100
    NonUsers = POPULATION - Influencers

    Time = 10

    for Week in range(Time):
        PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers)
        ActiveUsers += RecruitmentRateFromFriends * ActiveUsers + (RecruitmentRateFromInfluencers + InfluencerToActive) * Influencers + DormantToActive * DormantUsers - (ActiveToInfluencer + ActiveToDormant) * ActiveUsers
        DormantUsers += ActiveToDormant * ActiveUsers - (DormantToNonUsers + DormantToActive) * DormantUsers
        Influencers += ActiveToInfluencer * ActiveUsers - (InfluencerToActive * Influencers)
        NonUsers += DormantToNonUsers * DormantUsers - (RecruitmentRateFromFriends * ActiveUsers + RecruitmentRateFromInfluencers * Influencers)



def PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers):
    """
    A function to print the number of each type of user.
    """
    print("Active Users: ", ActiveUsers)
    print("Dormant Users: ", DormantUsers)
    print("Influencers: ", Influencers)
    print("NonUsers: ", NonUsers)
    print()

StateChanges()