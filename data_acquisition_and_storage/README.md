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
- When the MongoDB is installed create a database, database in the Node-red flow is named: "ZDMP_2". The name can be changed in the Node-red flow, depending on the name of established database. If the MongoDB runs locally (127.0.0.1) it is typically available at the port 27017.
- To use MongoDB from wihtin the Node-red, the one needs to install additional nodes that enable connection to MongoDB. This can be done in the Palette Manager of Node-red. The needed package is called: Palette Manager "node-red-node-mongodb". Moreover, the dashboard nodes are needed, package name is: "node-red-dashboard".
- When all the steps are done, the flows that are stored in the JSON files can be imported. Node-red has the import option, the one only needs to copy the JSON content into the import window of Node-red and click on import button.
- Further details on the presented use-cases can be found in the demonstration video. 
