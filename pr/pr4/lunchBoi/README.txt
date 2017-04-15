4/12:
Began working on menu stuff. Skeleton code is looking pretty solid.
I need to make a map object (and possibly others) that will be separate from the
menu objects. Menu objects are only to be concerned with selection. All classes/
functions in this project are going to be as specific as possible.
As far as the back end goes, the basic layout that I have will be enough to work from
until I get the map and other visuals up and running. Menu functionality is the priority
at this point.

4/11:
Curses windows can be made as objects, constructing a string or similar data-type
to be "printed" to the terminal by curses.

4/7:
I am beginning by creating skeleton code similar to that in .../pr4/starter.
This includes rudimentary character, world, object, and respective subsidiary classes.
The plan is to create the game world by iterating upon these classes.
My alpha version will just be a standard text-based adventure built on top of these.
Once this has been completed, the next step will be to create a compelling hybrid
between a text based adventure and GUI based game, making use of curses.

The idea is to have three or four main screens:
-- The terminal screen, in which the PC interacts with various terminals throughout the ship.
-- The map screen, which shows the layout of the ship and the PC's location.
-- Various menus, formatted in the same way, prompting action of the PC.
-- One of these menus will be static, containing the PC's character sheet, settings, etc.
Curses will be used to construct these screens, to use key press recognition to switch
between them and to select/highlight menu items, to standardize the terminal window size,
to emulate a terminal window.

In regards to puzzle design, I should look to Mark Brown's Boss Key videos for inspiration.

Aesthetic/story inspiration comes from:
Alien, 2001, Event[0] (Gameplay), Interstellar, Duskers (UI, Gameplay), Fallout (UI), The Witness (Gameplay?)

Working Title: LunchBoi

After reading the documentation, curses seems more than adequate for my needs.

I have recorded a semblance of what I would like the final iteration to look like.
See vision1.txt.

To do:

-- Build/iterate upon skeleton code
-- Construct a basic curses implementation that allows for menu interaction.
-- Allow for switching between such menus
-- Think about puzzle design
-- Begin to think about how I want interaction w/ the "AI" to feel/consist of.
-- Design the ship
