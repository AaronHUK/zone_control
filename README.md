# zone_control
simulator + resources for a zone-control based board game

To run the simulator, run controller/controller.py

Board full of nodes and paths connecting the nodes
Each player starts with one node
all nodes grow by 1 each turn (up to 6)
Only action is attacking another node (along path)
- This sends all units on that node towards the other node
on attack:
- if attack and defence are equal, all die and no control changes
- if attack = defence + 1, all defenders die, 2 attackers die, and (as long as attackers remain) the node is captured
- if attack = defence + 2, all defenders die, 1 attacker dies, and (as long as attackers remain) the node is captured
- if attack > defence + 2, all defenders die, no attackers die, and the node is captured
Phases:
- Start of turn
- - All controlled nodes increase by 1
- Action phase
- - Players declare which direction nodes are attacking (by moving the tokens onto the paths)
- Resolution phase
- - All units move
- - Then all attacks are resolved