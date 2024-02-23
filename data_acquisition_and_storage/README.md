**The repository contains following elements:**
- Folder with dataset in .xlsx format. The will be pre-processed by the Python script.
- Python script that will pre-process dataset. This Python script is executed from within a Node-red flow.
- JSON files with that is needed to import the Node-red flow into the Node-red environment.

**Pre-requisites:**
- Installed Node-red environment. As Node-red relies on Node.js, the one needs to instal the Node.js before installing Node-red.
- Installed Python Interpreter to run the python scripts. (installed libraries that are sepcified within the script)
- Installed MongoDB.
- Web browser to use the GUI of Node-red.
- Optional: the GUI for MongoDB, e.g. Compass.
- Optional: registration at [Openweathermap](https://openweathermap.org/)https://openweathermap.org/ to use cutomized API.

**Detailed steps to deploy the use-case:**
- First, the one needs to install the Node.js. This can be done from official page on Node.js (https://nodejs.org/en/download).
- Then install the npm package manager. After Node.js is installed this can be done via command line.
- Using npm, the one can install the Node-red. For more information check the video: https://www.youtube.com/watch?v=hEpeobDyj8k
- After Node-red is installed it can be run locally: http://localhost:1880/
- Now, the MongoDB need to be installed (optionaly, but recommended also GUI, e.g. Compass). More details, here: https://www.mongodb.com/docs/manual/installation/
- 
