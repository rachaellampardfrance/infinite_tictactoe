<a id='top'></a>

# "Infinite" TicTacToe

<a id='table_of_contents'></a>

<details open>
<summary>Table of Contents</summary>

## Table of Contents
1. [About The Project](#about_the_project)
    - [Summary](#summary)
    - [Intentions](#intentions)
2. [Play Modes](#play_modes)
    - [2x Player](#2x_player)
    - [Easy Mode](#easy_mode)
    - [Hard Mode](#hard_mode)
3. [Built With](#built_with)
4. [Getting Started](#getting_started)
    - [Prerequisites](#prerequisites)
    <!-- - [Installation](#installation) -->
5. [Contact](#contact)
</details>

<a id='about_the_project'></a>

## About The Project
<a id='summary'></a>

### Summary:
This program creates an "infinate" tic tac toe game. The program has been made so that the board, winner/stalemate checks and computer placement priority, are all automated. In theory the game can scale to any size and the logic will still work
> for sanity board size has been limited to 10x10.

<a id='intentions'></a>

### Intentions

**create automated logic for:**
- Formatting game board to any size
- Winner and stalemate condition checks
- Computer placement priorities

**focus on:**
- Error handling
- Clean code approaches
- Type hinting and Docstrings
- Automated unit testing with Pytest - *(switch to test branch to see test files)*
- OOP approach and inheritance

<a id='play_modes'></a>

## Play modes

<a id='2x_player'></a>

### 2x player
Two player mode where the players can play against each other on a board of their chosen size

<a id='easy_mode'></a>

### Easy mode
Against the computer: In most cases the user should win...

The computer will place it's token at a random valid board location

<a id='hard_mode'></a>

### Hard mode

Against the computer: In most cases hard mode should result in a stalemate...

The computer will follow an order of operation, for the size of the board for each:

    1. try to make the winning/best progress move
    2. try to prevent the player from winning/ block player progression

> *(Hard mode does not increase the game board size)*

<img src='static/10x10_gameboard.png' alt='10x10 tic tac toe game board' width='300'>
<img src='static/3x3_gameboard.png' alt='3x3 tic tac toe game board' width='100'>

<a id='built_with'></a>

### Built with
- Python
- Visual Studio Code

<a id='getting_started'></a>

## Getting Started

<a id='prerequisites'></a>

### Prerequisites

<details open>
<summary>packages</summary>

[Python](https://www.python.org/downloads/)

    Download Python3 
</details>

<a id='contact'></a>

## Contact

###  Creator: Rachael Lampard-France

<a href='https://www.linkedin.com/in/rachael-lampard-france-a5995b195/'><img src='static/linkedin.png' alt='Linkedin Logo' width='100'></a>

Project Link - https://github.com/rachaellampardfrance/Infinite_TicTacToe

[return to top](#top)