'''
BASED ON TUTORIAL 1 TEMPLATE
FROM MICROSOFT
'''

import MalmoPython
import os
import sys
import time
import random
from agent import getNextLayout


sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)




'''
Returns the block XML given the x,y,z coordinates and the kind of block
'''
def getBlockXML(x, y, z, color):
    #return '<DrawBlock x="' + str(x) + '" y="' + str(y) + '" z="' + str(z) + '" type="' + str(kind) + '"/>'    
    return '<DrawBlock x="' + str(x) + '" y="' + str(y) + '" z="' + str(z) + '" type="' + 'wool"' + ' colour="' + str(color)  + '"/>'

'''
Returns an XML string representation of a tree given a 2D matrix layout
Uses rotations
'''
def renderTreeWithRotation(x, y, z, layout):
    result = ''
    
    # First rotatation
    for count, i in enumerate(range(len(layout)-1,-1,-1)):
        for count2, j in enumerate(range(len(layout[i]))):
            s = layout[i][j]
            if s != '':
                result += getBlockXML(x + count2, y + count, z, s)
    if len(layout[0]) % 2 == 1:
        #Second rotation and odd
        for count, i in enumerate(range(len(layout)-1,-1,-1)):
            for count2, j in enumerate(range(len(layout[i]))):
                s = layout[i][j]
                if s != '':
                    result += getBlockXML(x + 1, y + count, z + count2 - 1, s)    
    else:
        #Second rotation and even
        for count, i in enumerate(range(len(layout)-1,-1,-1)):
            for count2, j in enumerate(range(len(layout[i]))):
                s = layout[i][j]
                if s != '':
                    result += getBlockXML(x + 1, y + count, z + count2 - 1, s)        
    
    return result

'''
Returns an XML string representation of a tree given a 2D matrix layout
Only expands into 3D
'''
def renderTree(x, y, z, layout):
    result = ''
    
    for count, i in enumerate(range(len(layout)-1,-1,-1)):
        for count2, j in enumerate(range(len(layout[i]))):
            s = layout[i][j]
            if s != '': # If s is not empty, generate the block, and the depth blocks
                result += getBlockXML(x + count2, y + count, z, s)

                # depth blocks
                #for k in range(len(layout[i])): # TODO: subtract size of trunk
                #     result += getBlockXML(x + count2, y + count, z + k, s)
    return result


'''
Render a forest of Trees
'''
def renderForest():
    baseHeight = 227
    baseLR = 0
    baseNS = 5
    layout = getNextLayout()
    result = ''
    result += renderTree(baseLR, baseHeight, baseNS, getNextLayout())
    #for i in range(10):
    for i in range(1):
        baseLR = 0
        baseNS -= getChange(layout)
        #for i in range(10):
	for i in range(7):
            layout = getNextLayout()
            baseLR -= getChange(layout)
            result += renderTree(baseLR, baseHeight, baseNS + getChange(layout), layout)
    return result

def getChange(layout):
    b = len(layout[0])
    b += int(random.random()*5)
    return b




missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Trees!</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                   <Time>
                    <StartTime>12000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                   </Time>
                </ServerInitialConditions>

                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" forceReset="true"/>

                  <DrawingDecorator>''' + renderForest() + '''</DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="1000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Creative">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x="0" y="227" z="0"/>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()
#print my_mission.getAsXML(True)

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print "Error starting mission:",e
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print "Waiting for the mission to start ",
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission running ",

# Loop until mission ends:
while world_state.is_mission_running:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission ended"
# Mission has ended.
