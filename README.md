=== LABYMACGYVERFACE ===

Project version : 2.0 (19/04/2019)

Endless hours of pythonic fun brought to you by V.S. Studios !



*** Installation ***

This project uses pipenv ; everything you need is within the root folder

Simply run 'pipenv install' in the root folder to install all dependencies



*** Configuration ***

The 'path-layout.json' file is used to create a specific labyrinth structure

Each number within the array represents specific square on the grid

Every square thus represented is pathable, every other square will be a wall

IMPORTANT : the first number in the list will always be the character's spawn square

IMPORTANT : the second number in the list will always be the labyrinth's end square (aka the warden)



*** Launch ***

Simply run the main script using 'pipenv run python main.py'



*** Gameplay ***

Move MacGyver through the labyrinth using the arrow keys

Collect all items on the floor, then go for the fabulous warden

You win if you collected every single item, otherwise you lose !