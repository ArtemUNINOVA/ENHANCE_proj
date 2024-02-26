**The repository contains following elements:**
- Folder with dataset in .xlsx format. This will be pre-processed by the Python script.
- Python script that will pre-process dataset. This Python script is executed from within a Node-red flow.
- JSON files that are needed to import the Node-red flows into the Node-red environment.

**Pre-requisites:**
- Installed Node-red environment. As Node-red relies on Node.js, the one needs to instal the Node.js before installing Node-red.
- Installed Python Interpreter to run the python scripts. (installed libraries that are sepcified within the script)
- Installed MongoDB.
- Web browser to use the GUI of Node-red.
- Optional: the GUI for MongoDB, e.g. Compass.
- Optional: registration at [Openweathermap](https://openweathermap.org/)https://openweathermap.org/ to use cutomized API.

**Detailed steps to deploy the use-case:**
1. First, the one needs to install the Node.js. It can be downloaded from the official page on Node.js (https://nodejs.org/en/download).
2. Then install the npm package manager. After Node.js is installed this can be done via command line.
3. Using npm, the one can install the Node-red. For more information check the video: https://www.youtube.com/watch?v=hEpeobDyj8k
4. After Node-red is installed it can be run locally in the web browser: http://localhost:1880/
5. Now, the MongoDB need to be installed (optionaly, but recommended also GUI, e.g. Compass). More details, here: https://www.mongodb.com/docs/manual/installation/
6. When the MongoDB is installed create a database, database in the Node-red flow is named: "ZDMP_2". The one should consider this while creating the DB, and, either give the same name or change it in the Node-red flow. If the MongoDB is deployed locally (127.0.0.1) it is typically available at the port 27017.
7. To use MongoDB from wihtin the Node-red, the one needs to install additional nodes that enable connection to MongoDB. This can be done in the Palette Manager of Node-red. The needed package is called: "node-red-node-mongodb". Moreover, the dashboard nodes are needed for plotting, package name is: "node-red-dashboard".
8. When all the steps are done, the flows that are stored in the JSON files can be imported. Node-red has the import option, the one only needs to copy the JSON content into the import window of Node-red and click on import button.
9. Further details on the presented use-cases can be found in the demonstration video. 
