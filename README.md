# Spotify-Not-Just-a-Car-Thing
This repo for the making and version contorl of the Spotify Not Just a Car Thing by Shreyas and Emma

Description:
In this project, WE were able to control the spotify music application with 3 external buttons. The 3 buttons  we used were to pause, play and skip forward the songs. This project involves both hardware and software components. To make the connection between the microcontroller and the Spotify app, the Spotify API is used. This API acts like a communication pathway between the hardware and the app. 

Hardware components:
3 buttons, jumperwires, Raspberry Pi Pico W, Micro USB. 

Raspberry Pi Pico W Pinout

Software:
Thonny (Micropython), Spotify API, chatGPT. 

How does this program work
This program is split into 2 different sections, the first is to control the spotify app with thonny using  python. The second stage is to make the hardware components with the buttons and control it using the raspberry pi pico w. There is a link between the two codes which will allow the buttons to control functions on the spotify. 



Step 1: Spotify App ( API)
API stands for Application Programming Interface. This allows different software applications to communicate and exchange data. The spotify API is available for premium users and is a set of tools for computer programs to interact with the spotify application. 

To register into the Spotify API, visit the Spotify for developers (https://developer.spotify.com/documentation/web-api) > Documentation>Make an app.
Fill in the information in this section, for the Redirect URI, add the localhost and for the API use click web api. Once you have completed this section, you will receive 2 important codes, the Client ID and the Client secret, these are unique credentials that allow you to connect your project to the application. 

What is a Redirect URI?
The redirect URI is a specific web address or callback endpoint where an authorization server sends a user back after they finish logging in or approving an app. This stage is an authentication step to let Spotify know if the owner of the account allows them to use their account. 

Local host URI is http://127.0.0.1:8888/callback
http:// => simple communication protocol
127.0.0.1 => this is called a loopback address, it states ‘redirect to this computer’
8888 => which port the web server should listen to
/callback => just the path to "Go to the /callback page on my local server." 

Step 2: Install library Spotipy
This is a lightweight python library for the Spotify Web API. 
To install, open the Command Prompt and type “pip install spotipy” (pip stands for Preferred Installer Program, this is like an appstore for python library) 
To verify the installation type “pip show spotipy” and this will show you the information about the installation and the location the library has been downloaded to. 
Now open Thonny and create a new file and name it spotify_controller.py and copy paste appendix 1. Add in the Client ID and the Client secret.
When this code is first run, you will be redirected to the web browser to log into your spotify account. 

Step 3: Testing the code
In this stage you will test the different functions pause, play and skip forward. 

Step 4: Communicating to spotify
Create a new file on Thonny and name it spotify_controller.py, this file will communicate to spotify directly. And save this program onto your computer. 
This file will run function like: sp.start_playback(), sp.pause_playback(), sp.next_track()
Add the code from appendix 2 to this file

Stage 2: Connecting the buttons to Pico

Step 1: Creating the connections:
Connect 3 buttons onto a breadboard, one side of the buttons will be connected to ground while the other will be connected to the other to a GPIO pin. 
Open a new file on Thonny and name it main.py and save it to the Raspberry Pi Pico W. 
To this file, add the code from appendix 3. 

Step 2: Test whether the code works:
Press the buttons to test whether the code works, if ‘PAUSE’, ‘PLAY’ and ‘SKIP’ are printed, the buttons work. 

Stage 3: Making the Pico communicate with the python:
This connection is down with serial communication over the USB cable. Serial communication is when data is sent one by one through a communication line.

Step 1:
Replace the code in main.py with appendix 4.  
Install the serial communication library by typing ‘pip install pyserial’ into the Command Prompt
Find the Pico COM port, this can be found using Device Manager>Ports or by checking which port the pico is connected to on Thonny.

 Step 2:
Create a new program called pico_receiver.py and save it on the computer. 
Copy appendix 5 into the file
Replace COM5 with the actual port the Pico is connected to, ‘115200’ is the baud rate. Higher the baud rate, faster the communication speed. 

Step 3: Modifying computer program
Creating a program to listen to the pico and send the command to spotify. 

Create a file named spotify_pico_controller.py and save it on the computer. 
Add the code from appendix 6
You are now ready to test your program. Save the program for the pico and close the file. Now run Spotify in the background and run the program and test by clicking the buttons. 

Overall flowchart on how the program works:



Challenges along the way:
Connecting the Spotipy library onto Thonny: When I first tried to test whether Spotipy could be imported, it showed that the library could not be imported. This was because the location where the library was saved and Thonny was saved was different because I had other software on the computer that also runs python. To solve this issue, I changed the location by going to Tools > Options > Interpreter and changing the location. 
The settings for when coding the files on  pico and the files on the computer are different because the pico uses Micropython however the computer uses normal python which needs to be changed at the lower right-hand side. 

