import matplotlib.pyplot as plt
import mysql.connector # to install this though pycharm, open file->Settings->Project Inturpreter->'+'[logo on right]->install 'mysql-connector'.
import numpy
from matplotlib.widgets import Slider, Button, RadioButtons
import time

HOST = "ls-7747fafb702e9b0e95827d986e35040c609dd263.cztwonmsggwh.eu-west-2.rds.amazonaws.com"
USERNAME = 'mdm3socialnetwork'
PASSWORD = 'Once Upon A Time I Made A Password For A Thing'
DATABASENAME = 'SocialMediaPop' # DO NOT CHANGE THIS UNLESS YOU KNOW WHAT YOU ARE DOING. It will create a new database on my mysql server. (Don't worry it's not actually the end of the world. Just work.)

SLIDERSENSITIVITYUP = 2
SLIDERSENSITIVITYDOWN = 0.4
STEPSENSITIVITY = 100

# Tempory starting values so I know the globals are initalised.
OpenActiveToInfluencer = 0.001
OpenInfluencerToActive = 0.1
OpenActiveToDormant = 0.1
OpenDormantToActive = 0.1
OpenDormantToNonUsers = 0.1
OpenRecruitmentRateFromFriends = 1
OpenRecruitmentRateFromInfluencers = 10
OpenPOPULATION = 10 ** 7
OpenInfluencers = 100



class DatabaseHandler:

    def __init__(self):
        try:
            self.db = mysql.connector.connect(host=HOST, user=USERNAME, passwd=PASSWORD)
            self.cursor2ex = self.db.cursor()
            self.CreateDatabase()
            #self.CreateSudoData()
            # Test of my functions until I bother with button events

        except ValueError as e:
            print("Error while connecting to MySQL", e)
            # Assumes error was caused by no Database existing called texchange

    def CreateDatabase(self):
        try:
            self.db.connect(host=HOST, user=USERNAME, passwd=PASSWORD)
        except ValueError as e:
            print("Error while connecting to MySQL ", e)
        self.cursor2ex = self.db.cursor()
        self.cursor2ex.execute("CREATE DATABASE IF NOT EXISTS " + DATABASENAME)
        self.db.close()
        try:
            self.db = mysql.connector.connect(host=HOST, user=USERNAME, passwd=PASSWORD, database=DATABASENAME)
            self.cursor2ex = self.db.cursor()
            self.CreateTablesIfNotExists()
        except ValueError as e:
            print("Error while connecting to MySQL after Database Creation ", e)

    def CreateTablesIfNotExists(self):

        """
            For Ref:
                ActiveToInfluencer
                InfluencerToActive
                ActiveToDormant
                DormantToActive
                DormantToNonUsers
                RecruitmentRateFromFriends
                RecruitmentRateFromInfluencers
                POPULATION
                Influencers
        """
        try:
            self.cursor2ex.execute("""CREATE TABLE IF NOT EXISTS storedparameters (
            paramID INT AUTO_INCREMENT PRIMARY KEY,  
            ActiveToInfluencer Double NOT NULL,
            InfluencerToActive Double NOT NULL,
            ActiveToDormant Double NOT NULL,
            DormantToActive Double NOT NULL,
            DormantToNonUsers Double NOT NULL,
            RecruitmentRateFromFriends Double NOT NULL,
            RecruitmentRateFromInfluencers Double NOT NULL,
            POPULATION Double NOT NULL,
            Influencers Double NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        except ValueError as e:
            print("MySQL error after Table Creation ", e)

    def SaveParameters(self, ActiveToInfluencer, InfluencerToActive, ActiveToDormant, DormantToActive, DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers, POPULATION, Influencers):
        # returns success or not depending on whether username is taken and account successfully created.

        # this function will add a New Set of parameters based on when program was last open.
        try:
            self.cursor2ex.execute("INSERT INTO storedparameters (ActiveToInfluencer, InfluencerToActive, ActiveToDormant, DormantToActive, DormantToNonUsers, RecruitmentRateFromFriends, RecruitmentRateFromInfluencers, POPULATION, Influencers) VALUES ('" + str(ActiveToInfluencer) + "', '" + str(InfluencerToActive) + "', '" + str(ActiveToDormant) + "', '" + str(DormantToActive) + "', '" + str(DormantToNonUsers) + "', '" + str(RecruitmentRateFromFriends) + "', '" + str(RecruitmentRateFromInfluencers) + "', '" + str(POPULATION) + "', '" + str(Influencers) + "');")
            self.db.commit()
        except():
            return False
        return True

    def GetLatest(self):
        try:
            self.cursor2ex.execute("SELECT * FROM storedparameters ORDER BY paramID DESC LIMIT 1;")
            result = self.cursor2ex.fetchall()
        except ValueError as e:
            print("MySQL error finding user for login", e)
        #print(result)
        if not len(result) == 0:
            return result
        else:
            return False
    # End of Database handler Class


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

        ActiveUsers += ((RecruitmentRateFromFriends * ActiveUsersValues[Week] * NonUsersValues[Week] / POPULATION ** 2
                         + (RecruitmentRateFromInfluencers + InfluencerToActive) * InfluencersValues[Week]
                         + DormantToActive * DormantUsersValues[Week])
                        - (ActiveToInfluencer + ActiveToDormant) * ActiveUsersValues[Week])
        DormantUsers += (ActiveToDormant * ActiveUsersValues[Week]
                         - (DormantToNonUsers + DormantToActive) * DormantUsersValues[Week])
        Influencers += (ActiveToInfluencer * ActiveUsersValues[Week]
                        - InfluencerToActive * InfluencersValues[Week])
        NonUsers += (DormantToNonUsers * DormantUsersValues[Week]
                     - (RecruitmentRateFromFriends * ActiveUsersValues[Week] * NonUsersValues[Week] / POPULATION ** 2)
                     - RecruitmentRateFromInfluencers * InfluencersValues[Week])

        if ActiveUsers <= 0 or DormantUsers <= 0 or Influencers <= 0 or NonUsers <= 0:
            print("The model is out of range because a value is below zero.")
            PrintStatistics(ActiveUsers, DormantUsers, Influencers, NonUsers, Week)
            PlotStatistics(ActiveUsersValues, DormantUsersValues, InfluencersValues, NonUsersValues, WeekValues)
            break
        if POPULATION != round(ActiveUsers + DormantUsers + Influencers + NonUsers):
            print(ActiveUsers + DormantUsers + Influencers + NonUsers)
            print(POPULATION)
            print("The total population is not constant.")
    PlotStatistics(ActiveUsersValues, DormantUsersValues, InfluencersValues, NonUsersValues, WeekValues)


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
    OpenActiveToInfluencer = SliderActiveToInfluencer.val/100
    OpenInfluencerToActive = SliderInfluencerToActive.val
    OpenActiveToDormant = SliderActiveToDormant.val
    OpenDormantToActive = SliderDormantToActive.val
    OpenDormantToNonUsers = SliderDormantToNonUsers.val
    OpenRecruitmentRateFromFriends = SliderRecruitmentRateFromFriends.val
    OpenRecruitmentRateFromInfluencers = SliderRecruitmentRateFromInfluencers.val
    OpenPOPULATION = SliderPOPULATION.val
    OpenInfluencers = SliderInfluencers.val
    db.SaveParameters(OpenActiveToInfluencer, OpenInfluencerToActive, OpenActiveToDormant, OpenDormantToActive, OpenDormantToNonUsers, OpenRecruitmentRateFromFriends, OpenRecruitmentRateFromInfluencers, OpenPOPULATION, OpenInfluencers)
    StateChanges(OpenActiveToInfluencer, OpenInfluencerToActive, OpenActiveToDormant, OpenDormantToActive, OpenDormantToNonUsers, OpenRecruitmentRateFromFriends, OpenRecruitmentRateFromInfluencers, OpenPOPULATION, 0, 0, OpenInfluencers)
    #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    #fig.canvas.draw_idle()


def getLatestParams(result):
    global OpenActiveToInfluencer
    global OpenInfluencerToActive
    global OpenActiveToDormant
    global OpenDormantToActive
    global OpenDormantToNonUsers
    global OpenRecruitmentRateFromFriends
    global OpenRecruitmentRateFromInfluencers
    global OpenPOPULATION
    global OpenInfluencers
    if len(result) > 0:
        OpenActiveToInfluencer = result[0][1]
        OpenInfluencerToActive = result[0][2]
        OpenActiveToDormant = result[0][3]
        OpenDormantToActive = result[0][4]
        OpenDormantToNonUsers = result[0][5]
        OpenRecruitmentRateFromFriends = result[0][6]
        OpenRecruitmentRateFromInfluencers = result[0][7]
        OpenPOPULATION = result[0][8]
        OpenInfluencers = result[0][9]


db = DatabaseHandler()
getLatestParams(db.GetLatest())
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




SliderActiveToInfluencer            = Slider(axActiveToInfluencer, 'ActiveToInfluencer *10^2', int(OpenActiveToInfluencer*100*SLIDERSENSITIVITYDOWN), OpenActiveToInfluencer*100*SLIDERSENSITIVITYUP, valinit=OpenActiveToInfluencer*100, valstep=(OpenActiveToInfluencer*100/float(STEPSENSITIVITY)))
SliderInfluencerToActive            = Slider(axInfluencerToActive, 'InfluencerToActive', int(OpenInfluencerToActive*SLIDERSENSITIVITYDOWN), OpenInfluencerToActive*SLIDERSENSITIVITYUP, valinit=OpenInfluencerToActive, valstep=(OpenInfluencerToActive/float(STEPSENSITIVITY)))
SliderActiveToDormant               = Slider(axActiveToDormant, 'ActiveToDormant', int(OpenActiveToDormant*SLIDERSENSITIVITYDOWN), OpenActiveToDormant*SLIDERSENSITIVITYUP, valinit=OpenActiveToDormant, valstep=(OpenActiveToDormant/float(STEPSENSITIVITY)))
SliderDormantToActive               = Slider(axDormantToActive, 'DormantToActive', int(OpenDormantToActive*SLIDERSENSITIVITYDOWN), OpenDormantToActive*SLIDERSENSITIVITYUP, valinit=OpenDormantToActive, valstep=(OpenDormantToActive/float(STEPSENSITIVITY)))
SliderDormantToNonUsers             = Slider(axDormantToNonUsers, 'DormantToNonUsers', int(OpenDormantToNonUsers*SLIDERSENSITIVITYDOWN), OpenDormantToNonUsers*SLIDERSENSITIVITYUP, valinit=OpenDormantToNonUsers, valstep=(OpenDormantToNonUsers/float(STEPSENSITIVITY)))
SliderRecruitmentRateFromFriends    = Slider(axRecruitmentRateFromFriends, 'RecruitmentRateFromFriends', int(OpenRecruitmentRateFromFriends*SLIDERSENSITIVITYDOWN), OpenRecruitmentRateFromFriends*SLIDERSENSITIVITYUP, valinit=OpenRecruitmentRateFromFriends, valstep=(OpenRecruitmentRateFromFriends/float(STEPSENSITIVITY)))
SliderRecruitmentRateFromInfluencers= Slider(axRecruitmentRateFromInfluencers, 'RecruitmentRateFromInfluencers', int(OpenRecruitmentRateFromInfluencers*SLIDERSENSITIVITYDOWN), OpenRecruitmentRateFromInfluencers*SLIDERSENSITIVITYUP, valinit=OpenRecruitmentRateFromInfluencers, valstep=(OpenRecruitmentRateFromInfluencers/float(STEPSENSITIVITY)))
SliderPOPULATION                    = Slider(axPOPULATION, 'Population',int(OpenPOPULATION*SLIDERSENSITIVITYDOWN), OpenPOPULATION*SLIDERSENSITIVITYUP, valinit=OpenPOPULATION, valstep=int(OpenPOPULATION/float(STEPSENSITIVITY)))
SliderInfluencers                   = Slider(axInfluencers, 'Influencers',int(OpenInfluencers*SLIDERSENSITIVITYDOWN), OpenInfluencers*SLIDERSENSITIVITYUP, valinit=OpenInfluencers, valstep=int(OpenInfluencers/float(STEPSENSITIVITY)))

SliderActiveToInfluencer.on_changed(update)
SliderInfluencerToActive.on_changed(update)
SliderActiveToDormant.on_changed(update)
SliderDormantToActive.on_changed(update)
SliderDormantToNonUsers.on_changed(update)
SliderRecruitmentRateFromFriends.on_changed(update)
SliderRecruitmentRateFromInfluencers.on_changed(update)
SliderPOPULATION.on_changed(update)

SliderInfluencers.on_changed(update)
time.sleep(0.5)
StateChanges()
update(2)
plt.show()



