import matplotlib.pyplot as plt

def ErrorChecker(ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Week):
    if POPULATION != round(ActiveUsers + DormantUsers + Influencers + NonUsers):
        print(ActiveUsers + DormantUsers + Influencers + NonUsers)
        print(POPULATION)
        exit()
    if (ActiveUsers <= 0 or DormantUsers <= 0 or Influencers <= 0 or NonUsers <= 0 ) and Week > 0:
        print("The model is out of range because a value is below zero.")
        PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)
        exit()

def StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
                 DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers):
    """
    This defines initial population conditions and coefficients for the movement of users.
    A for loop then calculates the change in each type of user and calls the function to print the number of each type of user.
    """
    POPULATION = 10**4
    ActiveUsers = 0
    DormantUsers = 0
    Influencers = 100
    NonUsers = POPULATION - Influencers
    Time = 150

    ActiveUsersValues = []
    DormantUsersValues = []
    InfluencersValues = []
    NonUsersValues = []
    WeekValues = []

    for Week in range(Time):
        #Creating lists of values of Users
        ActiveUsersValues.append(ActiveUsers)
        DormantUsersValues.append(DormantUsers)
        InfluencersValues.append(Influencers)
        NonUsersValues.append(NonUsers)
        WeekValues.append(Week)

        PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)

        ActiveUsers += ((RecruitmentRateFromFriends * ActiveUsersValues[Week] * NonUsersValues[Week] / POPULATION**2
                        + (RecruitmentRateFromInfluencers + InfluencerToActive) * InfluencersValues[Week]
                        + DormantToActive * DormantUsersValues[Week])
                        - (ActiveToInfluencer + ActiveToDormant) * ActiveUsersValues[Week])
        DormantUsers += (ActiveToDormant * ActiveUsersValues[Week]
                     - (DormantToNonUsers + DormantToActive) * DormantUsersValues[Week])
        Influencers += (ActiveToInfluencer * ActiveUsersValues[Week]
                    - InfluencerToActive * InfluencersValues[Week])
        NonUsers += (DormantToNonUsers * DormantUsersValues[Week]
                    - (RecruitmentRateFromFriends * ActiveUsersValues[Week] * NonUsersValues[Week] / POPULATION**2)
                    - RecruitmentRateFromInfluencers * InfluencersValues[Week])
        ErrorChecker(ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Week)
    PlotStatistics(ActiveUsersValues, DormantUsersValues,InfluencersValues,NonUsersValues, WeekValues)

def PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week):
    """
    A function to print the number of each type of user.
    """
    print(Week)
    print("Active Users: ", ActiveUsers)
    print("Dormant Users: ", DormantUsers)
    print("Influencers: ", Influencers)
    print("NonUsers: ", NonUsers)
    print("MonthlyActiveUsers: ", ActiveUsers + Influencers)
    print()

def PlotStatistics(ActiveUsersValues, DormantUsersValues,InfluencersValues,NonUsersValues, WeekValues):
    Figure = plt.figure()
    Figure.suptitle("Types of user")
    plt.plot(WeekValues, ActiveUsersValues, "r",
             WeekValues, DormantUsersValues, "b",
             WeekValues, InfluencersValues, "g",
             WeekValues, NonUsersValues, "y")
    plt.show()