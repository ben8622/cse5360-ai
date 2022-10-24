Benjamin Knight  
1001788622
CSE 5360-004 T/Th


# [Assignment 1](https://crystal.uta.edu/~gopikrishnav/classes/2022/fall/4308_5360/assmts/assmt1.html)

**GOAL** - Implement a search algorithm to find the shortest route between two cities.  

**INPUT** - Will be a .txt provided in the program arugments that looks like:  
> Luebeck Hamburg 63  
Hamburg Bremen 116  
Hamburg Hannover 153  
Hamburg Berlin 291  
*... extra nodes ...*  
Birmingham Bristol 85  
Birmingham London 117  
END OF INPUT  

**OUTPUT** - Will return a set of statistics and the path like:
> Nodes Popped: 12  
Nodes Expanded: 6  
Nodes Generated: 20  
Distance: 297.0 km  
Route:  
Bremen to Hannover, 132.0 km  
Hannover to Kassel, 165.0 km  

## How to run:
**Developed on:**
- Windows 10
- python 3.10.7

1. Download the [repo from github](https://github.com/ben8622/cse5360-ai)
2. cd into the ./task1 directory
3. For **informed search** run `python ./main.py example_inputs/input1.txt Bremen Kassel example_inputs/h_kassel.txt`  
For **uniformed search** run `python ./main.py example_inputs/input1.txt Bremen Kassel`