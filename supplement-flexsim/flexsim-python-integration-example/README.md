# General purpose

The purpose of the example is to show how to implement some decision logic for decision points in a FlexSim simulation in external code written in Python.

# Simulation objective

A simple simulation contains the source connected with 3 buffers. The source produces some parcels, that can be sent to one of the buffers. This is the decision point controlled by an external function written in Python.

 The function simply reads active buffer ID from 'source_output.txt' and returns it.

# FlexSim - Python integration

The integration is done according to the FlexSim documentation https://docs.flexsim.com/en/24.1/Reference/DeveloperAdvancedUser/ConnectingToExternalCode/ConnectingToExternalCode.html. An external code link is defined in the source 'output port' property.

```
external python "FlexSimPy" "assign_output"
```

The 'FlexSimPy.py' file with the 'assign_output' function definition is placed in the same directory as the simulation file.

# How to test

Open 'source_output.txt' in an editor and run the simulation. While the simulation is running, try changing the output port number and save the file. Parcels in the simulation should immediately be redirected to the new destination.