# showCaseS23 Overview
These are games written by students in the CS120 Computer Science 1 course

# arcade cabinet keyboard map

**Left stick** 

    w - up
    a - left
    s - down
    d - right

**Left Buttons**  

    f  e  
          q
    z  x

**Right Stick**  

    i = up
    j = left
    k = down
    l = right

**Right Buttons**  
(confirmation needed)    

    h  u
          o
    b  n

**Left side start button**  

    /

**Right side player buttons**

    2 = two players
    1 = one player

# User Interface

### Introduction

The first thing the UI does is it grabs the current directory that the file is being run in. We will need to get back to this directory after we run the other games so I saved this directory into a attribute of the game class called startDir. Then the game keeps track of x and y values. The x and y values are increminted based on which way the left user moves the joystick. If the joystick moves to the right(Key D) then the x value is incrimented by one. If the joystick moves to the left (Key A) then the x is decreased by one. If the joystick moves up (Key W) then the y is incrimented by one. If the joystick moves down (Key S) then the y value is decreased by one. Based on whatever the x and y values are is where the selection border hovers over (see process method). Then once something is selected the user can then play what game they have selected (see process event method). 

### Process Method
This is where the selection border figures out what icon to go over. It looks at the x and y values and then set's the position of the selection border to the icon the user is intending on selecting. 

### Process Event Method
This is where all of the user's keyboard input is tracked. This is also where the games are ran. There is a class attribtue called gameSelected that is set whenever the user is hovering over a certain game. Once the left user is hovering over something and clicks the red button (Key F) it looks at what game is selcted and runs that game. The prcoess of running the game is always the same. We change the dirctory to the directory that the game is stored in (so we can acess all the game's files) we then call a prcoess and run the game file. After the game is done being run we will reset the directory to the original directory that was talked about in the introduction section. Lastly, we will call the rest method. 

### Reset Method
The reset method is very simple. It will reset gameSelected to be nothing, it will hide the selection border and the label telling you to play, it will reset the x and y to zero, and it will restart the background music. 

### Citations
Ball State Logo: Taken from official twitter page
Arcade Background Image: https://www.vecteezy.com/vector-art/5266448-vector-retro-futuristic-background
Arcade Font: https://www.dafont.com/arcade-ya.font
Selection Border: https://pngimg.com/image/90845
Arcade Music: Music by <a href="https://pixabay.com/users/grand_project-19033897/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Grand_Project</a> from <a href="https://pixabay.com/music//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Pixabay</a>
Icon Images: Most icon images were taken from game files and had backgrounds added. 



    
