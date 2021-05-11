# Code Folder

This folder contains all of the code used in our project, with the exception of the master Colab notebook which is one directory up from here. 

While these files can be run directly from the command line, it is recommended to run them in the Colab document. There are detailed and insighful, useful examples and comments throughout the Colab document guiding the viewer on how to navigate the code for training a model or evaluating its performance on the test set. The Colab document contains all of the code we used for this project (including command line calls to the python scripts contained in the Code folder), and it should not be necessary to move files around for the notebook to work effectively. 

Do not run the pre-process code. Some filepaths have changed, and running this might overwrite the current data files. All of the data needed is contained in the data folder. 

If you would like to use our scoring script to evaluate the performance of a file of predictions, please run:

python score.py gold-filepath pred-filepath

in the command line. However, as mentioned before, it would be better to run this from the notebook, since everything is nicely organized and all in one place. 