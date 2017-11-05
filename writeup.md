## P, I, D Components discussion
* The P component stands for the **proportional**. It is the main one and its task is to reduce the (cross track) error in proportion.
* The D component (**derivative**) counteracts the impact of the P component. The controller with the P component only will overshoot the target and will end up in a state of oscilations. The D component smoothes the whole process - slows down the controller so it does not overshoot.
* The I component (**integral**) is useful when we have to deal with a bias. Without it the controller may never reach the state of no error. Basically the integral term monitors the cumulative error and counters it, so even if there is a bias the controller can move towards zero error.

## Selection of the PID controller parameters
The first implementation used the following paramters `Kp = 0.5`, `Ki = 0.00004` and `Kd = 0.5`. This did not work very well. I tried to implement the twiddle algorithm in the project, but because of its structure it was hard to achive without rewriting most of it. So I ended up with a mixed solution.

The twiddle algorithm was implemented in python (see the `twiddle.py` file) and provided the paramters via the command line arguments. The process of finding the optimal paramters was very slow (about half a day) so to make it a bit faster the simulation stopped after the first turn after the bridge. I got the follwing paramters from the twiddle algorithm `Kp = 0.981`, `Ki = 0.00669` and `Kd = 21.233`. I think this is a local minimum, because at some point the car went into oscillations and started leaving the track.

I started manually tweeking the result from twiddle. To minimize the osciallations is started reducing the `Kp` paramter and then all the others (so the remaing components do not overreact). I finished with the following paramters `Kp = 0.281`, `Ki = 0.001` and `Kd = 5.233`.