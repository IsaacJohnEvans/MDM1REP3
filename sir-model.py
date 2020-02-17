

import random
import numpy as np
import pylab as pl

#Ok, so now we're going to set the initial state of our model.
S = 1000 #this is the number of susceptibles
I = 1 #we seed the outbreak with one infectious individual
R = 0 #and no one has recovered yet

#here, we calculate the total number of individuals in the system 
#we'll be using this for reference as we go along
N = S+I+R
N = float(N)

t = 0

#Infectivity (probability of generating a new case at each step)
b = .09

#Probability of recovering @ each step. Similarly, this is often called
#gamma, and we will abbreviate it here to 'g'.
g = .05

#Here, we make some lists to  keep track of number of individuals 
#in each state at each time step. These will be useful at the end 
#of the run when we want to see what the model actually did.

sList = [] #we'll keep the number of susceptible individuals at each step on this list
iList = [] #the number of infected individuals here
rList = [] #the number who have recovered here
newIList = [] #and we'll use this to record the number of newly infected people on each step.

#We make a loop that runs as long as there are still infectious individuals
while I > 0:
    # so far, no one has been infected yet
    newI = 0
    
    #there is a single random trial for each susceptible individual
    for i in range(S):
        #here, we're using a frequency dependent transmission process;
        #density dependence would be b*I
        
        #we use the method 'random.random()' to draw uniformly distributed numbers
        in the range [0,1).
        if random.random() < b*(I/N):
            newI += 1
        
        #to switch to density dependence, comment out the block above and
        #uncomment the following:
            if random.random() < b*I:
                newI += 1
    
    #Now we're going to see how many individuals recovery on this step.    
    recoverI = 0
    for i in range(I):
        if random.random() < g:
            recoverI += 1
    
    
    S -= newI
    I += (newI - recoverI)
    R += recoverI
    
    #Then we add these values to their respective lists
    sList.append(S)
    iList.append(I)
    rList.append(R)
    newIList.append(newI)
    
    #This prints the time to standard out - usually the terminal you're running from -
    #and increments the timestep.
    #print('t', t)
    t += 1

#We'll drop out of the loop above when we satisfy the stopping condition, I = 0 
#and then print out the values to the terminal
print('sList', sList)
print('iList', iList)
print('rList', rList)
print('newIList', newIList)
aArray = np.array(rList) + np.array(iList)
aList = aArray.tolist()

pl.figure()
pl.plot(iList)
pl.plot(rList)
pl.plot(aList)
pl.xlabel('time')
pl.show()

