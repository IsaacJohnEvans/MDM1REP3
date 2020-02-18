import matplotlib.pyplot as plt
import numpy

def StateChanges():
    """
    This defines initial population conditions and coefficients for the movement of users.
    A for loop then calculates the change in each type of user and calls the function to print the number of each type of user.
    """
    #These coefficients currently produce nonsense numbers.
    ActiveToInfluencer = 0.001
    InfluencerToActive = 0.1
    ActiveToDormant = 0.1

    DormantToActive = 0.005
    DormantToNonUsers = 0.1

    RecruitmentRateFromFriends = 1
    RecruitmentRateFromInfluencers = 15

    POPULATION = 10**5
    ActiveUsers = 0
    DormantUsers = 0
    Influencers = 100
    NonUsers = POPULATION - Influencers

    Time = 120

    ActiveUsersValues = []
    DormantUsersValues = []
    InfluencersValues = []
    NonUsersValues = []
    WeekValues = []

    for Week in range(Time):
        ActiveUsersValues.append(ActiveUsers)
        DormantUsersValues.append(DormantUsers)
        InfluencersValues.append(Influencers)
        NonUsersValues.append(NonUsers)
        WeekValues.append(Week)
        PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)
        ActiveUsers += RecruitmentRateFromFriends * ActiveUsers * NonUsers / POPULATION**2 + (RecruitmentRateFromInfluencers + InfluencerToActive) * Influencers + DormantToActive * DormantUsers - (ActiveToInfluencer + ActiveToDormant) * ActiveUsers
        DormantUsers += ActiveToDormant * ActiveUsers - (DormantToNonUsers + DormantToActive) * DormantUsers
        Influencers += ActiveToInfluencer * ActiveUsers - (InfluencerToActive * Influencers)
        NonUsers += DormantToNonUsers * DormantUsers - (RecruitmentRateFromFriends * ActiveUsers * NonUsers / POPULATION**2 + RecruitmentRateFromInfluencers * Influencers)
        if ActiveUsers <= 0 or DormantUsers <= 0 or Influencers <= 0 or NonUsers <= 0 :
            print("The model is out of range because a value is below zero.")
            PlotStatistics(ActiveUsersValues, DormantUsersValues, InfluencersValues, NonUsersValues, WeekValues)
            exit()
    PlotStatistics(ActiveUsersValues,DormantUsersValues,InfluencersValues,NonUsersValues,WeekValues)

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
    plt.plot(WeekValues, ActiveUsersValues, "r", WeekValues, DormantUsersValues, "b", WeekValues, InfluencersValues, "g", WeekValues, NonUsersValues, "y")
    plt.show()

StateChanges()
