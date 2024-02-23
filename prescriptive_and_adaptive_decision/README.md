**The repository contains following elements:**
- Folder with data stored in txt files in a .csv format. Dataset contains raw data with different parameters of jet engines reflecting the "health" conditions of engines. The train files contain data for model training, test files contain data for model testing and finaly the RUL files contain the ground truth, i.e. right lables for the testing dataset. The latter is needed to assess the efficiency of the ML model.
- File "untitled_project" with a trained LSTM model that is used for classification of samples, classifying a sample belongs to the red zone interval (last 30 samples before engine failure) or not.
- The .ipynb file containing the source code for data pre-processing, model definition, training and plotting.

There are two ways to use the .ipynb file: either to open it with Jupyter Notebook or with Google Colab. If Google Colab is used, no further installations are needed besides the availability of the web browser. In the case if Jupyter Notebook is used the **pre-requisites are as follows**:
- Installed Python's interpreter.
- Installed Anaconda distribution that already contains jupyter notebook.
- A set of libraries that can be installed using, for instance, pip package manager.

**Detailed steps to deploy the use-case:**
- Create a folder, where the use-case files will be deplyoed.
- Copy all the files into the folder.
- Open Jupyter Notebook and open the .ipynb file ("RUL_jet_engine_predictions_final").
- Change the path to the datasets, so it corresponds to the path of newly created folder.
- Install the libraries that are specified in the beginning of the file.
- After all libraries are installed, click the "Run" button.
- Further details on presented use-cases can be found in the demonstration video.
