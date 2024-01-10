# Crazyflie_Keyboard
A working (as of January 2024) keyboard control setup for a Crazyflie, in the most basic terms available. The first script works without a Flow Deck. The second script requires one, but enables much smoother movement.

# Setup

This script works out of the box on the Crazyflie's associated virtual machine - pull the repo, run the script, and you're golden. It should also work on any computer with the requisite Python libraries.

# Usage

```
python kcontrol_basic.py
```

Controls are as follows:

 - Tap spacebar and c to increment your vertical thrust upwards or downwards.
 - Hold Q or E to turn right or left.
 - Hold WASD to strafe along the horizontal plane.
 - Tap the 'L' key to cut engine power and exit the program.

```
python kcontrol_flow.py
```

Controls are as follows:

 - Hold W and S to move upwards or downwards
 - Hold Q or E to turn right or left.
 - Hold the arrow keys to strafe along the horizontal plane.
 - Tap the 'L' key to land the quadrocopter and exit the program.
