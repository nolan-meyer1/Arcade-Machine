# Arcade Machine: Ball State Computer Science
These are games written by students in the CS120 Computer Science 1 course

### Featured Games
|Game Title| Currently on Machine| Author |
| -------- | --------------------| ------ |
|[Cannon Shooter](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Cannon%20Shooter)|Yes|Karter West|
|[Car Demo](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Car)|No|Proffesor Andy Harris|
|[Celestial Voyage](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/CelestialVoyage)|Yes|Christopher Davis|
|[Charlie Game](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Charlie-Game)|Yes|Proffesor Andy Harris|
|[Space Game](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Final-Project-main)|Yes|Addison Isley|
|[Driving Game](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Final-Game-main)|Yes|Isaiah Schlenker|
|[Dice Game](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/FinalDice-main)|No|Braydon Lee|
|[Mario Janitor](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Janitoring_Game-main)|No|Lance Schoenradt|
|[Mystic Monsters](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Mystic_Monsters-main)|No|Jeremy Escobar|
|[Organ Simon](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/OrganSimon)|No|Alexander Murry|
|[Platformer](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Platformer)|Yes|Proffesor Andy Harris|
|[Store Simulator](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Store-Simulator-Final-main)|No|Cater Lekron|
|[Tank Game](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Tank-Game-main)|Yes|Owen Johnson|
|[Warriors Arena](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Warriors-Arena-main)|Yes|Nolan Meyer|
|[Zombie Shooter](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/ZombShooter-main)|No|Andrew Scott|
|[Zombie Land](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/Zombie-Land-Game-main)|No|Unkown|
|[Jump Guy](https://github.com/nolan-meyer1/Arcade-Machine/tree/Experimental/jumpGuy-main)|No|Unknown|









# Arcade Machine Keyboard Map

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

# User Interface

### Introduction

The first thing the UI does is it will run the loadPage function that will create the pages based off the loaded in json file. Once the UI page is instanciated it will grab the current directory wer are in. We will need to get back to this directory after we run the other games so I saved this directory into a attribute of the game class called startDir. Then the game keeps track of x and y values. The x and y values are increminted based on which way the left user moves the joystick. If the joystick moves to the right(Key D) then the x value is incrimented by one. If the joystick moves to the left (Key A) then the x is decreased by one. If the joystick moves up (Key W) then the y is incrimented by one. If the joystick moves down (Key S) then the y value is decreased by one. Based on whatever the x and y values are is where the selection border hovers over (see process method). Then once something is selected the user can then play what game they have selected (see process event method). 

<img width="633" alt="Screenshot 2024-04-20 at 11 57 39 AM" src="https://github.com/nolan-meyer1/Arcade-Machine/assets/145584308/c2a5da21-cd94-4d62-b1cb-f86aad5c26ad">
<img width="633" alt="Screenshot 2024-04-20 at 3 09 03 PM" src="https://github.com/nolan-meyer1/Arcade-Machine/assets/145584308/04e99ef3-750d-45da-91f2-cbbf40b4bc74">


### JSON File
In order for this program to run you must have a required JSON file called configuration.json. The JSON file is very simple setup. It contains a key called "Games" that contains a list full of dictionaries. The reason it is setup like this is because the program needs to be able to iterate over the list. Whatever game you put at the beginning of the list will be the first one's added on the row. Each dictionary inside of the list will need to have a few elements:

* Name: Should contain game name and author's name. Used in credits page
* Image-Path: Path to the image you want to be the game icon
* dir: The directory of the game file that will be run.
* startFile: The game file that should be run first. 

If you are missing any of these elements and error will be generated and the program will fail execution. 
The sample structure looks like this: 

{
    "Games": [
        {
            "Name": "Warriors Arena- Nolan Meyer",
            "Image-Path": "startScreen/warriors-arena-logo.png",
            "dir": "Warriors-Arena-Main",
            "startFile": "userInterface.py"
        },
        {
            "Name": "Cannon Shooter- Karter West",
            "Image-Path": "startScreen/cannon-shooter-logo.png",
            "dir": "Cannon Shooter",
            "startFile": "CannonDefense.py"
        },
        {
            "Name": "Charlie Game- Proffesor Andy Harris",
            "Image-Path": "startScreen/charlieLogo.png",
            "dir": "Charlie-Game",
            "startFile": "catch8.py"
        }
}

As long as your structure is setup like this you can add however many games you want and the program will generate the needed pages! 

## StartScreen Class

### Overview

This is the class that is used to make pages. It contains a few class variables:
* currentPage: Keeps track of the current page you're on.
* numberPages: Keeps track of the number of pages created.
* gamePages: A list of all of the instances of startScreen created.

Attributes:
* Background: Background image
* ballState_logo: Ball State Logo displayed in the corner of the screen.
* titeLabel: The title that appears at the top of the screen.
* playLabel: The label that appears once the selection border is on something.
* game1-8: These are the game icons that will appear on the screen.
* creditsLabel: The label in the bottom left corner that shows what button to click for creits.
* startDir: The starting directory that the program is run from.
* startClicked: Boolean variable to check if a game has been selected.
* x: x value of the selection border.
* y: y value of the selection broder.
* configurationFile: The dictionary loaded in from the configuration file.
* gameList: The list of all the games on the page. 

### Rest Method
Resets:
* selectBorder
* playLabel
* x
* y
* Music (If specified)

### Process Event Method
This is where all of the user's keyboard input is tracked. This is also where the games are ran. There is a class attribtue called gameSelected that is set whenever the user is hovering over a certain game. Once the left user is hovering over something and clicks the red button (Key F) it looks at what game is selcted and runs that game. To run the game it will call the "runGame" method. If you click one player button it will select a random game (will only pick from the current screen). You still have to click the red button to play. 

### Process Method
This is where the selection border figures out what icon to go over. It looks at the x and y values and then set's the position of the selection border to the icon the user is intending on selecting. This is also where the boundaries are set. This makes sure that when the user tries to go over the amount of games that are in a row it loops back to the beginnin if there isn't a page behind it or infront of it. If there is another page it will switch to that page. It also won't allow the user's y value to go above the amount of rows there are. Lastly, I bulit in a way to exit full screen. If you hold all of the left buttons (Key F, E, Z, X, and Q) it will quit the game allowing you to exit from full screen.

### Reset Method
The reset method is very simple. It will reset gameSelected to be nothing, it will hide the selection border and the label telling you to play, it will reset the x and y to zero, and it will restart the background music.

### runGame Method
This is the method that runs the game. It takes in two parameters gameDir and gameFile. gameDir is the directory that we want to go into to run the game. gameFile is the gameFile that we want to run to start the game. If you set gameDir to None it will not change directories. 

### loadPage Function
The loadPage function is the key to creation of all the pages. It takes in two parameters. A games dictionary (loaded in from file) and a pages list. You don't need to specify this though because a list that contains None as the first elemenets is already created. I wouldn't recommend actually passing it an array the array is there for recursion purposes. The first thing it does is create a few variables:
* i: Initially set to zero. This keeps tracks of the rows.
* j: Initially set to zero. This keeps track of the colomuns.
* initialLength: Gets the initial length of the "Games" list loaded from file.
* page: Instance of the startScreen class that takes in the games parameter of the function.
  
It then will loop over every game in the games list. During each iteration it will check if i<4. If it is it will acess the gameList set the image, size, and position. It will then incriment i by one, and numberOfGamesX(instance variable). This is creating the first row. Once i is greater than 4 it will stop running and do the same process but start using the variable j for the loop. Lastly, there is a condition that checks if i == 8. If i is equal to eight that means there is a full page and we need to exit the loop so it breaks. It will then see if the length is greater than four. If it is that means there is a second row so it will incriment numberOfGamesY (instance variable). It will then append the page to the pages list. It will then check if the len of games is greater than 8. If it is that means there are too many games for this page and we need to create another page. If this is true it will game a copy of the games list, slice it. Then make a recursive call to do the process over again. This will continue until the length of the slice is less than eight meaning that we don't need to create another page. 

### Main
This function will load in the games file and pass it to loadPage. It will then get the game pages from the game pages class and run the first page in that list. 


## Credits Scene

This is the part of the User Interface that contains all of the credits. It includes the game logo image (same one used on the selection screen), the game name followed by the creator (EX: Warriors Arena- Nolan Meyer). You start the credits by clicking the left side button. 

<img width="638" alt="Screenshot 2024-04-20 at 11 57 43 AM" src="https://github.com/nolan-meyer1/Arcade-Machine/assets/145584308/e372abe2-52ca-477e-b090-0f94da9ce1f1">



### Atrributes/Class variables
Attributes:
* gameLogo1-4: Contains the logo's that will appear on the screen.
* gameLabel1-4: This is the labels that go with the logos.
* pageNumber. This shows that page that class is.
* logoList: List containing all the logos.
* labelList: List containing all the lists.
  
Class Variables:
* currrentPage: The current page you're on.
* numberPages: The number of pages created.
* creditPages: Contains a list of all the credit pages created

   
### Process Event
This keeps tracks of all of our keyboard input. If you click the "/" button you will quit. Depedning on what scene you're in if you click either "A" or "D" it will allow you to switch between scenes. On each key click it will check if there is page to switch to before you make the switch. 

### Process
This method is very simple. It will check if the currentPage does not equal the pageNum variable. If it doesn't it will make the page switch. 

### loadPage Method
This is very similar to the loadPage method from the startScreen class except a little simpler. It will loop over every game in games. Each iteration it will add a logo and label to the screen changing the logo's image, size, position, and position. It will change the label's text,center,clearBack,size, and fgColor. It will also incriment i. When i is greater than 4 that means the page is full. It will break out of the loop append it to pages then chekc if the len of the games list is greater than four. If it is that means a new page needs to be created. It will then make a copy of the list slice it and make a recursive call to the function. The recursion will stop once the sliced list length is not greater than four meaning that we don't need to make a new page because everything can be fit on that page at that recursion level. 

### Main
This function will load in the games file and pass it to loadPage. It will then get the credits pages from the credits pages class and run the first page in that list. 




# Citations
Ball State Logo: Taken from official twitter page

Arcade Background Image: https://www.vecteezy.com/vector-art/5266448-vector-retro-futuristic-background

Arcade Font: https://www.dafont.com/arcade-ya.font

Selection Border: https://pngimg.com/image/90845

Arcade Music: Music by <a href="https://pixabay.com/users/grand_project-19033897/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Grand_Project</a> from <a href="https://pixabay.com/music//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Pixabay</a>

Race Game Background image: <a href="https://www.freepik.com/free-vector/race-track-with-start-finish-line_24554257.htm#query=cartoon%20racetrack%20background&position=1&from_view=keyword&track=ais&uuid=2140b90c-5055-47e4-8933-215e1c4c4f47">Image by brgfx</a> on Freepik

Icon Images: Most icon images were taken from game files and had backgrounds added. All citations can be found from those in the game author's file 
