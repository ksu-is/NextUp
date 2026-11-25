# NextUp Project Roadmap

**(Solo Dev Being Jack Davison)**

## Sprint 1: Setup and Research

- [x] Create the NextUp repository in KSU-IS
- [x] Create the NextUp GitHub team
- [x] Become the team Maintainer
- [x] Connect the team to the repository
- [x] Finish and commit README.md
- [x] Find and review a similar Python project
- [x] Attempt to run the existing project's code
- [x] Document what worked, what didn't, and what I learned
- [x] Create and commit projectroadmap.md
- [x] Complete the Sprint 1 Review and Log

## Sprint 2: Building the Basics
**est timeline** Nov 30th, 2026 

- [x] Create the main Python file for NextUp
- [x] Install PyQt5 and successfully launch the application
- [ ] Create a graphical navigation sidebar
- [ ] Design the game library interface
- [ ] Create an Add Game window
- [ ] Allow users to manually enter a game's title, genre, and platform
- [ ] Implement game statuses (Not Started, Playing, Completed, Dropped)
- [ ] Allow users to update game information
- [ ] Create a function to remove games from the library
- [ ] Implement a SQLite database to save and load games
- [ ] Test all basic functionality and fix errors
- [ ] Complete at least six meaningful GitHub commits
- [ ] Complete the Sprint 2 Review and Log

## Future Features

- [ ] Add a priority system for games
- [ ] Allow users to search and filter their library
- [ ] Create the "What Should I Play Next?" random selector
- [ ] Add filters to the random selector
- [ ] Experiment with a graphical interface
- [ ] Turn the random selector into a spinning wheel

## Researching Similar Projects

### Siege System
https://github.com/alterpendragon/siege-system

What I learned:

After looking through Siege System, I got a better idea of how a game backlog tracker could work using Python. It has a fairly simplistic interface which I would like to incorporate into NextUp, at least for the earlier versions. One major difference is that Siege System uses an external API to retrieve game information, while I plan on letting users manually enter their games instead.

How I attempted to run it:

I downloaded Siege System from GitHub then opened using VSC. After installing the required packages, I ran main.py through the terminal. The program started successfully, and I was able to navigate to the main menu, which included options for viewing, filtering, adding, deleting, and updating games.

Problems I encountered:

The main issue I encountered was when I tried adding a game to the backlog. Every time I entered a game title, the program displayed an "Error fetching game data" message. After looking into it, I found that the program wanted a RAWG API key to retrieve game information, which I hadn't configured. Since I don't plan on using APIs for NextUp, I decided not to spend additional time setting one up. Instead, I'll focus on building a system where users can manually enter and manage their own games.
### GameTracker
https://github.com/Inderjit01/GameTracker

I also found this project and plan to look at its
backlog management features for inspiration.
