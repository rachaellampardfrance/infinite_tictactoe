<a id='top'></a>

# <img src='static/5x5_gameboard.png' alt='3x3 tic tac toe game board' width='150'><img src='static/logo.png' alt='3x3 tic tac toe game board' width='600'>

<a id='table_of_contents'></a>

## <img src='static/table_of_contents.png' alt='3x3 tic tac toe game board' width='450'> 

<details open>
<summary>📚 Table of Contents</summary>

1. [📖 About The Project](#about_the_project)
    - [Summary](#summary)
    - [Intentions](#intentions)
2. [🎮 Play Modes](#play_modes)
    - [👥 2x Player](#2x_player)
    - [👤🎯 Easy Mode](#easy_mode)
    - [👤⚔️ Hard Mode](#hard_mode)
3. [🔧 Built With](#built_with)
4. [❔ Getting Started](#getting_started)
    - [Prerequisites](#prerequisites)
    <!-- - [Installation](#installation) -->
5. [📧 Contact](#contact)
</details>

<a id='about_the_project'></a>

## <img src='static/about_the_project.png' alt='3x3 tic tac toe game board' width='480'>
<a id='summary'></a>

### Summary:
Create any size game of tic tac toe! This program has been made so that the board formatting, winner/stalemate checks and computer player placement priority, are all automated. In theory the game can scale to any size and the logic will still work!
> for sanity board size has been limited to 10x10.

<a id='intentions'></a>

### Intentions

**Design Automated Logic:**
- Formatting game board to any size
- Winner and stalemate condition checks
- Computer logic for placement priority

**focus on:**
- Error handling
- Clean code approaches
- Type hinting and Docstrings
- Automated unit testing with Pytest - *(switch to test branch to see test files)*
- OOP approach and inheritance

**Modules:** limited use to focus on learning practices 
- <a href= 'https://pypi.org/project/pyfiglet/'>Pyfiglet</a> to print the game logo and create this documents headings
- Random - the inbuilt module, used to generate random placements when the computer player is in easy mode, or can't find a best placement option when in hard mode!  

<a id='play_modes'></a>

## <img src='static/play_modes.png' alt='3x3 tic tac toe game board' width='300'>
<a id='2x_player'></a>

### 👥 2x player
Two player mode where the players can play against each other on a board of their chosen size

<a id='easy_mode'></a>

### 👤🖥️🎯 Easy mode
Against the computer: In most cases the user should win...

The computer will place it's token at a random valid board location

<a id='hard_mode'></a>

### 👤🖥️⚔️ Hard mode

Against the computer: In most cases hard mode should result in a stalemate...

The computer will adhere to the following order of operation:
    
    for the size of the board in reverse:
        1. try to make the winning/best progress move
        2. try to prevent the player from winning/block player progression

1. generate priority arguments to be passed into the placement generation function...

<img src='static\generate_computer_priorities.png' alt='10x10 tic tac toe game board' width='600'>

2. run all generated priority arguments on the function until a priority is met and a placement location is  returned...

<img src='static\run_computer_priorities.png' alt='10x10 tic tac toe game board' width='400'>

> *'Hard Mode' does not increase the game board size*

<img src='static/10x10_gameboard.png' alt='10x10 tic tac toe game board' width='300'><img src='static/3x3_gameboard.png' alt='3x3 tic tac toe game board' width='100'>

<a id='built_with'></a>

## <img src='static/built_with.png' alt='3x3 tic tac toe game board' width='275'>
- 🐍 Python
    - <a href= 'https://pypi.org/project/pyfiglet/'>Pyfiglet</a> for README.md text and game logo
- 💠 Visual Studio Code

<a id='getting_started'></a>

## <img src='static/getting_started.png' alt='3x3 tic tac toe game board' width='400'>

<a id='prerequisites'></a>

### Prerequisites

<details open>
<summary>packages</summary>

[Python](https://www.python.org/downloads/)

    Download Python3 
</details>

<a id='contact'></a>

## <img src='static/contact.png' alt='3x3 tic tac toe game board' width='220'>

###  Creator: Rachael Lampard-France

<a href='https://www.linkedin.com/in/rachael-lampard-france-a5995b195/'><img src='static/linkedin.png' alt='Linkedin Logo' width='100'></a>

Project Link - https://github.com/rachaellampardfrance/Infinite_TicTacToe

[return to top](#top)