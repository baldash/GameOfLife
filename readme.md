Pong QL
=======

**Author:** *baldash*

## Overview

GUI to edit and run Conway's game of life

## Usage

All of the program's params can be edited in the **params.py** file and are pretty self explanatory. All the maps are stored in the **maps/** folder and automatically **all** loaded when playing.
The maps format is **bld** and is simply written like this :  
```
# this is a comment line
# x y -> x and y position of a living cell in the grid
# this for example will be a blinker in the grid

2 1
2 2
2 3
```

To run the program simply use:  
`python main_menu.py`

## Docker

You can also build and run the docker image like so (on linux or WSL):  
```
docker build -t game-of-life .
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix game-of-life
```

## Language and libs

- Python 3.13.7
- PyRaylib 5.5.0.3
- Numpy 2.3.3

## Refs

- [Raylib python docs](https://electronstudio.github.io/raylib-python-cffi/)
- [Game of life's wikipedia page](https://www.wikiwand.com/en/articles/Conway%27s_Game_of_Life)
- [Numpy docs](https://numpy.org/devdocs/)
- [Regex builder](https://pythex.org)
- LMStudio - OpenAI GPTOss-20B