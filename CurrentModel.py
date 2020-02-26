import matplotlib.pyplot as plt

def ErrorChecker(ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Week):
    """
    Checks to see if the total population is constant.
    Checks to see if the number of each type of user is greater than zero.
    If either of these conditions are not satisfied then the program is exited.
    """
    if POPULATION != round(ActiveUsers + DormantUsers + Influencers + NonUsers):
        print(ActiveUsers + DormantUsers + Influencers + NonUsers)
        print(POPULATION)
        print("The total population is not constant.")
        exit()
    if (ActiveUsers < 0 or DormantUsers < 0 or Influencers < 0 or NonUsers < 0):
        print("The model is out of range because a value is below zero.")
        PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)
        exit()

def StateChanges(ActiveToDormant, ActiveToInfluencer, InfluencerToActive, DormantToActive,
                 DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers,
                 ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Time):
    """
    This function takes the initial arguments and then iteratively changes the number of each type of user.
    The values of each type of user are printed and recorded onto a list at each time point.
    """
    #Creating the empty lists
    ActiveUsersValues = []
    DormantUsersValues = []
    InfluencersValues = []
    NonUsersValues = []
    WeekValues = []
    """
    This for loop runs for an amount of time inputted in the initial conditions.
    Each iteration changes the number of each type of user.
    """
    for Week in range(Time):
        #Creating lists of values of Users
        ActiveUsersValues.append(ActiveUsers)
        DormantUsersValues.append(DormantUsers)
        InfluencersValues.append(Influencers)
        NonUsersValues.append(NonUsers)
        WeekValues.append(Week)
        #Printing this weeks statistics
        PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)
        #Running the iteration
        ActiveUsers += (RecruitmentRateFromFriends * ActiveUsersValues[Week]
                        + (RecruitmentRateFromInfluencers + InfluencerToActive) * InfluencersValues[Week]
                        + DormantToActive * DormantUsersValues[Week]
                        - (ActiveToInfluencer + ActiveToDormant) * ActiveUsersValues[Week])
        DormantUsers += (ActiveToDormant * ActiveUsersValues[Week]
                     - (DormantToNonUsers + DormantToActive) * DormantUsersValues[Week])
        Influencers += (ActiveToInfluencer * ActiveUsersValues[Week]
                    - InfluencerToActive * InfluencersValues[Week])
        NonUsers += (DormantToNonUsers * DormantUsersValues[Week]
                    - RecruitmentRateFromFriends * ActiveUsersValues[Week]
                    - RecruitmentRateFromInfluencers * InfluencersValues[Week])
        #Checking for errors
        ErrorChecker(ActiveUsers, DormantUsers, Influencers, NonUsers, POPULATION, Week)
    #Plotting the data
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
    """
    A function that will plot the data collected using matplotlib.
    Plots Active, Dormant and non users and influencers against the week number.
    The plot is displayed.
    """
    Figure = plt.figure()
    Figure.suptitle("Types of user")
    plt.plot(WeekValues, ActiveUsersValues, "r", label="Active Users")
    plt.plot(WeekValues, DormantUsersValues, "b", label="Dormant Users")
    plt.plot(WeekValues, InfluencersValues, "g", label="Influencers")
    plt.plot(WeekValues, NonUsersValues, "y", label="Non-users")
    plt.legend(loc="best")
    plt.show()
