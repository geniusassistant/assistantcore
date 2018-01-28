# Poor man's alexa

## Creating a mod

#### Setting it up

- Create a file in the mod directory with it's filw name being whatever you want the mod name to be.
- Save it with a '.py' extension
- Go into 'load.py' in the mod directory and add your mod name (without the '.py') to the variable enabled mods

#### API

- Create a function named 'outsource' with one of it's parameters being 'text'
- Do whatever you need to do, and when you are finished and need the assistent to say something, make it return the text you want it to say.
- If you do not want it to say anything, it is best practice to return None