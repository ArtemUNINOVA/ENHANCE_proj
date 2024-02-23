**The repository contains following elements:**
- Folder with dataset in .xlsx format. Dataset contains raw data about the number of cars assembled and the number of batteries used during the assembly process.
- File "untitled_project" with a trained LSTM model that is used to address regression problem and predict the number of batteries.
- The .ipynb file containing the source code for data pre-processing, model definition, training and plotting.
- Another Excel file with the table that contains day, real number of installed batteries of E type (1 of 5 types) and the predicted number of batteries.

There are two ways to use the .ipynb file: either to open it with Jupyter Notebook or with Google Colab. If Google Colab is used, no further installations are needed besides the availability of the web browser. In the case if Jupyter Notebook is used the **pre-requisites are as follows**:
- Installed Python's interpreter.
- Installed Anaconda distribution that already contains jupyter notebook.
- A set of libraries that can be installed using, for instance, pip package manager.

**Detailed steps to deploy the use-case:**
1. Create a folder, where the use-case files will be deplyoed.
2. Copy all the files into the folder.
3. Open Jupyter Notebook and open the .ipynb file ("demand_prediction_final_version").
4. Change the path to the dataset, so it corresponds to the path of newly created folder.
5. Install the libraries that are specified in the beginning of the file.
6. After all libraries are installed, click the "Run" button.
7. Further details on the presented use-cases can be found in the demonstration video.
