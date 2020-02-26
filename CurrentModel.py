import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import Slider, Button, RadioButtons


def StateChanges(ActiveToInfluencer = 0.001,InfluencerToActive = 0.1, ActiveToDormant = 0.1, DormantToActive = 0.1, DormantToNonUsers = 0.1, RecruitmentRateFromFriends = 1, RecruitmentRateFromInfluencers = 10, POPULATION = 10**9, ActiveUsers = 0, DormantUsers = 0, Influencers = 100 ):
    """
    This defines initial population conditions and coefficients for the movement of users.
    A for loop then calculates the change in each type of user and calls the function to print the number of each type of user.
    """
    #These coefficients currently produce nonsense numbers.


    # going to assume that ^^ collectively make up 11 coefficients to me messed with.



    NonUsers = POPULATION - Influencers

    Time = 600

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
        if ActiveUsers <= 0 or DormantUsers <= 0 or Influencers <= 0 or NonUsers <= 0:
            print("The model is out of range because a value is below zero.")
            PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)
            PlotStatistics(ActiveUsersValues, DormantUsersValues, InfluencersValues, NonUsersValues, WeekValues)
            break
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
    LineActiveUsers.set_data(WeekValues, ActiveUsersValues)
    LineDormantUsers.set_data(WeekValues, DormantUsersValues)
    LineInfluencers.set_data(WeekValues, InfluencersValues)
    LineNonUsers.set_data(WeekValues, NonUsersValues)
    ax.relim()
    ax.autoscale(enable=True, axis='both')
    
    plt.draw()


def update(val):
    OpenActiveToInfluencer = SliderActiveToInfluencer.val
    OpenInfluencerToActive = SliderInfluencerToActive.val
    OpenActiveToDormant = SliderActiveToDormant.val
    OpenDormantToActive = SliderDormantToActive.val
    OpenDormantToNonUsers = SliderDormantToNonUsers.val
    OpenRecruitmentRateFromFriends = SliderRecruitmentRateFromFriends.val
    OpenRecruitmentRateFromInfluencers = SliderRecruitmentRateFromInfluencers.val
    OpenPOPULATION = SliderPOPULATION.val

    OpenInfluencers = SliderInfluencers.val

    StateChanges(OpenActiveToInfluencer, OpenInfluencerToActive, OpenActiveToDormant, OpenDormantToActive, OpenDormantToNonUsers, OpenRecruitmentRateFromFriends, OpenRecruitmentRateFromInfluencers, OpenPOPULATION, 0, 0, OpenInfluencers)
    #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    #fig.canvas.draw_idle()

fig = plt.figure("MDM3 Social Network Pop Model")
ax = fig.add_subplot(111)
LineActiveUsers, = ax.plot([1,2,3,4],[0,2,4,6],"r", label="ActiveUsers")
LineDormantUsers, = ax.plot([1,2,3,4],[0,2,4,6],"b", label="DormantUsers")
LineInfluencers, = ax.plot([1,2,3,4],[0,2,4,6],"g", label="Influencers")
LineNonUsers, = ax.plot([1,2,3,4],[0,2,4,6], label="Non-Users")
plt.subplots_adjust(left=0.25, bottom=0.55)
ax.margins(x=0)
fig.suptitle("Types of user")
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

axcolor = 'lightgoldenrodyellow'
yoffset = -0.07
axActiveToInfluencer = plt.axes([0.25, 0.1 + yoffset, 0.65, 0.03], facecolor=axcolor)
axInfluencerToActive = plt.axes([0.25, 0.15 + yoffset, 0.65, 0.03], facecolor=axcolor)
axActiveToDormant = plt.axes([0.25, 0.2 + yoffset, 0.65, 0.03], facecolor=axcolor)
axDormantToActive = plt.axes([0.25, 0.25 + yoffset, 0.65, 0.03], facecolor=axcolor)
axDormantToNonUsers = plt.axes([0.25, 0.3 + yoffset, 0.65, 0.03], facecolor=axcolor)
axRecruitmentRateFromFriends = plt.axes([0.25, 0.35 + yoffset, 0.65, 0.03], facecolor=axcolor)
axRecruitmentRateFromInfluencers = plt.axes([0.25, 0.4 + yoffset, 0.65, 0.03], facecolor=axcolor)
axPOPULATION = plt.axes([0.25, 0.45 + yoffset, 0.65, 0.03], facecolor=axcolor)
axInfluencers = plt.axes([0.25, 0.5 + yoffset, 0.65, 0.03], facecolor=axcolor)


OpenActiveToInfluencer = 0.001
OpenInfluencerToActive = 0.1
OpenActiveToDormant = 0.1
OpenDormantToActive = 0.1
OpenDormantToNonUsers = 0.1
OpenRecruitmentRateFromFriends = 1
OpenRecruitmentRateFromInfluencers = 10
OpenPOPULATION = 10 ** 7

OpenInfluencers = 100

SliderActiveToInfluencer            = Slider(axActiveToInfluencer, 'ActiveToInfluencer', int(OpenActiveToInfluencer/float(10)), OpenActiveToInfluencer*5, valinit=OpenActiveToInfluencer, valstep=(OpenActiveToInfluencer/float(10)))
SliderInfluencerToActive            = Slider(axInfluencerToActive, 'InfluencerToActive', int(OpenInfluencerToActive/float(10)), OpenInfluencerToActive*5, valinit=OpenInfluencerToActive, valstep=(OpenInfluencerToActive/float(10)))
SliderActiveToDormant               = Slider(axActiveToDormant, 'ActiveToDormant', int(OpenActiveToDormant/float(10)), OpenActiveToDormant*5, valinit=OpenActiveToDormant, valstep=(OpenActiveToDormant/float(10)))
SliderDormantToActive               = Slider(axDormantToActive, 'DormantToActive', int(OpenDormantToActive/float(10)), OpenDormantToActive*5, valinit=OpenDormantToActive, valstep=(OpenDormantToActive/float(10)))
SliderDormantToNonUsers             = Slider(axDormantToNonUsers, 'DormantToNonUsers', int(OpenDormantToNonUsers/float(10)), OpenDormantToNonUsers*5, valinit=OpenDormantToNonUsers, valstep=(OpenDormantToNonUsers/float(10)))
SliderRecruitmentRateFromFriends    = Slider(axRecruitmentRateFromFriends, 'RecruitmentRateFromFriends', int(OpenRecruitmentRateFromFriends/float(10)), OpenRecruitmentRateFromFriends*5, valinit=OpenRecruitmentRateFromFriends, valstep=(OpenRecruitmentRateFromFriends/float(10)))
SliderRecruitmentRateFromInfluencers= Slider(axRecruitmentRateFromInfluencers, 'RecruitmentRateFromInfluencers', int(OpenRecruitmentRateFromInfluencers/float(10)), OpenRecruitmentRateFromInfluencers*5, valinit=OpenRecruitmentRateFromInfluencers, valstep=(OpenRecruitmentRateFromInfluencers/float(10)))
SliderPOPULATION                    = Slider(axPOPULATION, 'Population',int(OpenPOPULATION/float(10)), OpenPOPULATION*5, valinit=OpenPOPULATION, valstep=int(OpenPOPULATION/float(10)))
SliderInfluencers                   = Slider(axInfluencers, 'Influencers',int(OpenInfluencers/float(10)), OpenInfluencers*5, valinit=OpenInfluencers, valstep=(OpenInfluencers/float(10)))

SliderActiveToInfluencer.on_changed(update)
SliderInfluencerToActive.on_changed(update)
SliderActiveToDormant.on_changed(update)
SliderDormantToActive.on_changed(update)
SliderDormantToNonUsers.on_changed(update)
SliderRecruitmentRateFromFriends.on_changed(update)
SliderRecruitmentRateFromInfluencers.on_changed(update)
SliderPOPULATION.on_changed(update)

SliderInfluencers.on_changed(update)

plt.show()
StateChanges()

