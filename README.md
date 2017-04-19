# h4Ck3Rs: Th3 G4m3

## About
This game is inspired by the movie Hackers and other 80s-2000 era movies, books, and games. It was developed in Python 3.3.2 and runs best on 'nix systems. This version of Python was chosen to maintain maximum compatibility with Oregon State University's testing environment, but it should run on newer (and possibly older) versions of Python3 as very few advanced language features were used.

Players can explore the 16 different rooms and use the items they find, buy, or steal in order to thwart EvilCorp Bank’s plans. There are three skills you can learn and you can end up in jail.

I was responsible for the project architecture and game engine. Not every modification to the core game engine by other developers is marked and some compromises in the design were made.

## Future Enhancement Opportunities
Feature creep resulted in the original architecture being stretched a bit beyond the original specifications. As a result, a refactoring of the entire project is in order. Also, the Language Parser is not particularly sophisticated or robust. The JSON format for rooms and objects could be made more modular, and the code is highly dependent on the rooms and objects that populate the world.

1. I think refactoring the language parser to be more sophisticated would be the best first step. Utilizing an open-source parser or using proper data structures such as trees and actually defined grammars would be a top priority.

2. Loading and saving of GameState could be modularized quite a bit. Creating a .to_JSON() method on GameState would eliminate a huge chunk of parsing and logic in the SaveGame class and eliminate the work that that class has to do.

3. The choice of Python3 was deliberate so that we could focus on design decisions. We had to choose a language that would run at the Linux command-line on the schools servers, so we chose Python over C and C++ (or Java) as it was the leanest language. I would consider a switch to Java (for cross-platform compatability) or C# (if making it a more robust windows app) before moving forward with a major refactoring of the code.

4. The game could be made a lot more modular and less "obvious" to the users. I would construct room descriptions more programatically, plugging in changes to the environment and objects in the room based on the current GameState. Right now, most of the changes that happen in the game require looking at an object or room feature. It's also a little too obvious what objects and features are something a player could interact with. Coupled with a parser that unfortunately cannot handle ambiguity very well and the game does not stand up from the perspective of being an "interactive novel". Instead, it looks like something designed to be playtested by an instructor or TA... which it deliberately was designed to do.

5. More game mechanics. As it stands now, you can beat the game in ~29 typed in commands, and some of the mechanics are very boring.

6. More modular way to handle objects.

7. Convert the game engine into a setting-agnostic system where users could plug in room and object (and other?) JSON files tobuild their own world that wouldn't depend on the game engine knowing all of the JSON data files' details.


## Authors:
* Shawn Hillyer: Game Engine and Architecture
* Sara Hashem: File input and output 
* Niza Volair: Language Parsing
