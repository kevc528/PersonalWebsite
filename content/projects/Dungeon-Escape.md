# Dungeon Escape
> Survive the monsters and find all the keys to escape a maze

---
**Source Code**

<https://github.com/kevc528/DungeonEscape>

---

![Dungeon Escape](/content/images/dungeon-escape.jpg)

## About
This project was actually the final project for CIS120, an progamming design class I took freshman fall. The task 
was to create a game using the Java Swing GUI library. I decided to create a maze runner game, where a player is 
stuck in a maze and has to collect all the keys to get out, while also avoiding different monsters.

## Development
There were three main pieces to developing this game: randomly generating the maze, realistic movement, and the 
visuals.

To randomly generate the maze, I used DFS to recursively generate the maze in a 2D array of 0's and 1's, 
representing paths and walls. Initially the maze would be all wall and we will use DFS to 'dig' paths. Using DFS, 
there would be a path generated in chunks of length two in random directions until the path either collides with 
another path, or is outside of the maze. In that case, we would backtrack to the previous step and continue. 
Randomly generating the positions of the keys and monster spawns were pretty easy and just involved randomly 
generate a few coordinates.

Getting the movement down was actually pretty tricky. That's because I wanted the movement to be player-friendly. 
Having movement that only takes one key pressed down at a time would be really easy, but most people don't play 
games like that. If I wanted to turn right, go up, and then continue going right, odds are I would probably want 
to hold right, hold up while still holding right, and then let go of up. This was the type of movement I wanted 
to implement. This involved having to keep track of key down and key up events, and keeping track of which keys 
are down at any moment, and handling some extra cases. Handling collisions wasn't too bad... it was just a matter 
of determining when bounding boxes intersect and setting velocities based on that.

Another key feature that relied on movement was automating the movement of the monsters. This involved randomly 
setting the directions of the monster's movements and handling direction changes when a monster hits a wall.

The visuals weren't as complicated compared to the two previous aspects... but I was really happy with how 
the game looked visually. Especially with the torchlight effect, which was my favorite feature. The torchlight 
effect was implemented by just checking the postion of the player and lighting up only a specific radius. All 
the other visuals were a matter of getting the coordinates and placing an image in that spot.

Additionally, object oriented programming was a very important for this project. A game (especially retro) 
naturally leads to a very object oriented approach since the idea of having entities that may have a common 
functions but different details is really common. For example, there are different types of monsters that each 
have their own attacks, dealing different amounts of damage. In this case, using inheritance/subtyping and 
dynamic dispatch is important.

## Final Thoughts
Overall, I thought this project was a lot of fun and relaxing. It also helped teach and enforce concepts about 
object-oriented programming and event-driven programming. The game was pretty fun to play as well :)

