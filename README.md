# epaperbadge
E-paper badge scripts for use with pimoroni button shim

You can use this badge with either a Pimoroni Inky phat (recommended) or a Waveshare e-paper display 2.13 phat (not recommended).

Using with the e-paper display from Waveshare requires some modifications of the inkyphat library.

This project requires python3 and the inkyPhat libraries.  To install the inkyPhat library, ssh into your raspberry pi as the user 'pi' and run this from the command line:

<pre>
curl https://get.pimoroni.com/inkyphat | bash
</pre>

If you are using the InkyPhat, that is all you need to do.  If you are using the Waveshare board, you need to change the following settings in the InkyPhat library to correspond to the waveshare 2.13 epd pinout:


You will also need the button shim library from Pimoroni:

<pre>
https://get.pimoroni.com/buttonshim | bash 
</pre>

So, find this file on your system - inky212x104.py

(if you are using python3, which you should be, the file should be here:  /usr/lib/python3/dist-packages/inkyphat)

open it with nano
<pre>
sudo nano /usr/lib/python3/dist-packages/inkyphat/inky212x104.py
</pre> 
And change
<pre>
RESET_PIN = 27
BUSY_PIN = 17
DC_PIN = 22
</pre>
to
<pre>
RESET_PIN = 17
BUSY_PIN = 24
DC_PIN = 25
</pre>

Save the file (ctrl-x,y)

When you are ready, run the script with:
<pre>
sudo python3 begin.py
</pre>

If you want to run the script at boot, you would have to install the screen utility as it requires an active user logged into a terminal:
<pre>
sudo apt-get install screen
</pre>
Then add the command to execute it in a detached screen in rc.local;  
<pre>
sudo nano /etc/rc.local
</pre>
and before the exit 0 add this line (I put all my scripts in /home/pi/scripts - change this to wherever this directory lives on your pi)
<pre>
screen -dmS epaper bash -c "/home/pi/scripts/begin.py" &
</pre>

Make sure to add the & after the call and put it all between the fi and exit 0 of your rc.local, or it will hang on boot!


--hyperjoule
