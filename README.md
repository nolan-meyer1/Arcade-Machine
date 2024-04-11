# showCaseS23 Overview
These are games written by students in the CS120 Computer Science 1 course

# arcade cabinet keyboard map

All input should be based on keyboard.  The cabinet will have a mouse and keyboard,
but in gameplay mode, only the mapped keys will be available as joysticks and buttons.
In your instructions, please indicate both a key and a color for buttons, so the 
game can be played on a traditional computer as well as the cabinet.

    EG:  press f or red button for player1 to fire
         press h or red button for player2 to fire

**Left stick** 

              w - up
    a - left     +    d - right
              s - down

**Left Buttons**  

    f (red)  e (white)  
                        q (blue)
    z (yellow) x (green)

**Right Stick**  

              i = up
    j = left    +    l = right
             k = down

**Right Buttons**  

    h (red) u (white)
                    o (blue)
    b (yellow) n (green)
    
**Left side start button**  

    /

**Right side player buttons**

    2 = two players
    1 = one player

Only the keys listed in this mapping will be available during gameplay mode.
Consider adding keypress input in addition to any buttons.  
(If you have a start button, for example, also map it to / so the console start button will work.)

# User Interface

### Introduction

The first thing the UI does is it grabs the current directory that the file is being run in. We will need to get back to this directory after we run the other games so I saved this directory into a attribute of the game class called startDir. Then the game keeps track of x and y values. The x and y values are increminted based on which way the left user moves the joystick. If the joystick moves to the right(Key D) then the x value is incrimented by one. If the joystick moves to the left (Key A) then the x is decreased by one. If the joystick moves up (Key W) then the y is incrimented by one. If the joystick moves down (Key S) then the y value is decreased by one. Based on whatever the x and y values are is where the selection border hovers over (see process method). Then once something is selected the user can then play what game they have selected (see process event method). 

### Process Event Method
This is where all of the user's keyboard input is tracked. This is also where the games are ran. There is a class attribtue called gameSelected that is set whenever the user is hovering over a certain game. Once the left user is hovering over something and clicks the red button (Key F) it looks at what game is selcted and runs that game. The prcoess of running the game is always the same. We change the dirctory to the directory that the game is stored in (so we can acess all the game's files) we then call a prcoess and run the game file. After the game is done being run we will reset the directory to the original directory that was talked about in the introduction section. Lastly, we will call the rest method. 

### Process Method
This is where the selection border figures out what icon to go over. It looks at the x and y values and then set's the position of the selection border to the icon the user is intending on selecting. This is also where the boundaries are set. This makes sure that when the user tries to go over the amount of games that are in a row it loops back to the beginning, and when it won't allow the user's y value to go above the amount of rows there are. Lastly, I bulit in a way to exit full screen. If you hold all of the left buttons (Key F, E, Z, X, and Q) it will quit the game allowing you to exit from full screen.

### Reset Method
The reset method is very simple. It will reset gameSelected to be nothing, it will hide the selection border and the label telling you to play, it will reset the x and y to zero, and it will restart the background music.

## Credits Scene

This is the part of the User Interface that contains all of the credits. It includes the game logo image (same one used on the selection screen), the game name followed by the creator (EX: Warriors Arena- Nolan Meyer). 

### Atrributes
The attributes of this class are very minimal. It just contains sprites of all the image logos and labels. The first image starts at the position (50,130). The next image will appear below that with the Y value incrimented 90 from the previous image before it. The same idea is done with the labels. Except there will be minor adjustments to make sure that everything lines up nicely. Lastly, there is an action attribute that keeps track of what state we're in. Wether that's page1, page2, or quit. This state information will be returned to our main function. 

### Process Event
This keeps tracks of all of our keyboard input. If you click the "/" button you will quit. It will stop whatever current scene you're in and set the action attribute to Quit. Depedning on what scene you're in if you click either "A" or "D" it will allow you to switch between scenes. 

### Main
This function looks at the action atrribute of both classes and will then make a decision based of what state you are in. It will check if the page1's action is page2. If it is it will go to page2. Then it will check if either page1 or page2's action is Quit. If it is it will exit the loop and end the execution of the credit scene. I did this so that no matter what part of the credit's your on if you want to exit the credits all you have to do is click the side button. 




# Citations
Ball State Logo: Taken from official twitter page

Arcade Background Image: https://www.vecteezy.com/vector-art/5266448-vector-retro-futuristic-background

Arcade Font: https://www.dafont.com/arcade-ya.font

Selection Border: https://pngimg.com/image/90845

Arcade Music: Music by <a href="https://pixabay.com/users/grand_project-19033897/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Grand_Project</a> from <a href="https://pixabay.com/music//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Pixabay</a>

Icon Images: Most icon images were taken from game files and had backgrounds added. 
