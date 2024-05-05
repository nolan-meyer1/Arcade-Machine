# Tank-Game

You and a friend fight in an arena to the best of 3! Player 1 uses WASD to move and F to shoot and player 2 uses IJKL to move and H to shoot.

Game States:

## Intro Screen:
![Screenshot 2024-04-23 111952](https://github.com/Oij13/Tank-Game/assets/156932008/232f0378-cff2-41ec-b2d7-741ea41ade4a)

- Show Instructions
- Start Button (Start game)
- Quit Button (Exit game)

## Game Play:
![Screenshot 2024-04-23 112430](https://github.com/Oij13/Tank-Game/assets/156932008/cecee3c8-b94a-47b2-b63c-7c7770c1833b)

- Show predetermined map
- Give each user a score of 0
- Every hit to the other player increases the other's score by one
- Each hit moves hit player to opposite side of the screen from attacker
- First to 3 points wins (shows winner screen when player hits 3 points)

Game Over:
- Declares winner
- Shows play again btn (starts game over)
- Quit button shown

  Player win screen:
- Shows "Player [winner] Wins!" in text box
- Play again button (starts from Game Play screen)
- Quit button (goes to home screen)

  


## Sprites:
  Player1:
- User-controlled green tank sprite
- Rotate tank with A and D
- Move forward with W
- Backwards in facing direction with S
- Shoots with F in the directions the barrel is facing
- Cant pass through outer barrier or cover barriers
- Starts on left screen

  Player2:
- User-controlled red tank sprite
- Rotate tank with J and L
- Move forward with I
- Shoots with H in the direction the barrel is facing
- Cant pass through outer barrier or cover barriers
- Starts on right screen

  Bullets:
- Shoots in direction of barrel on either tank sprite
- if bullet on one player hits other player while their bullet is in motion, it resets the hit players bullet as well
      - Gets rid of simultaneous hits
- Sound effects from firing of bullet and colliding of bullet

  Barriers:
- Stops bullets
- Stops tank movement
- Keeps sprites from moving off the screen or through cover barriers
- Placed in predetermined locations
- Moves tank sprites to keep from going through barriers

  Player win screen:
- Shows "Player [winner] Wins!" in text box
- Play again button (starts from Game Play screen)
- Quit button (goes to home screen)

## UI Components
- Background
      - Rocky
      - Contrasts well with tanks and barriers
- LblScore
      - Adds a score for each tank
      - Adds by one for each hit on the opposing tank
      -
- LblStart
      - Starts game when clicked
      - Appears on title screen and win screen
- LblQuit
      - Quit the entire game when clicked
      - Appears on title screen and win screen




# Reflection

## Goals
- To create a simple yet elegant 2d tank game
- Figure out how to code barriers
- Gain a better understanding for the SimpleGE game engine
- Make a game compatible with the class arcade machine

## Technologies and techniques used
- Referenced professor's code in multiple instances such as bullet behaviors and creating working sprites and barriers
- SimpleGE and Pygame

## Citations
- “Jsfxr.” Jsfxr, 2024, sfxr.me/. Accessed 24 Apr. 2024.  (Used for sound effects of tanks)
- “OpenGameArt.org.” OpenGameArt.org, 2024, opengameart.org/. Accessed 24 Apr. 2024. (Used for all of the graphics and sprites)

## My Process

I learned that such a simple looking game on the outside can be very challenging and complex to make
* It makes you appreciate how hard people work on games and how complex their code must be 

I got stuck when trying to create barriers
- It is difficult to check the angle of the tank sprite while colliding with a barrier
- Any angle outside of a 45 degree span of a direction would confuse the collision point of the barrier
- Solution: Create 4 different barrier sprites to isolate the collision checking for the sprite
    - Each barrier side will only check one side for collision, giving a whole 180 degree angle for the tank to collide with
 
I would like to decorate the home screen and win screens a bit
- Plain black with white buttons
- Could be more decorative

I would take more breaks while coding
- A lot of the struggle in coding barriers came from overthinking about the problem
- Breaks would allow me to think in much more simple terms to help me solve the problem

I did not allow for a custom map selection in my final product
- My original game document called for that
- Put much more focus on mechanics than bells and whistles

Each class period I would have at least one new feature added to my game
- This allowed me to stay on track and complete my game on a good timeline
- One week would be focused on sprites and another focused on barriers, for example



‌





  
