# CIS 530 Final Project

Authors: Francesca Marini & Efe Ayhan
Spring 2021
Prof. Mark Yatskar
CIS 530: Computational Linguistics

Project Title: Low-Resource Machine Translation of Uyghur

In this directory:

1. data/ - a directory containing all of the train, dev, test data used in this project, as well as some other intermediate documents used during pre-processing. This is the least organized folder, but there is an informative README.md in that directory. In addition, the current setup should work as-is with the Colab notebook.

2. output/ - a directory containing several sub-directories. Each of these subdirectories contains the predicted output written to file of the best models for each type of model. There is also a subdirectory containing the gold data (the same as the test data contained in the data folder). This folder also contains an informative README.md.

3. code/ - a directory containing all of the code needed to replicate our project. Models also end up saving inside this directory (if anyone were to try to run the code). (We have removed the models because of space constraints.) This folder also contains an informative README.md. We do not recommend directly running these files (though it is certainly feasible from the command line, as shown in the Colab notebook); this is because it is much simpler to follow along with the Colab notebook.

4. Final Presentation - a PDF of our presentation slides, along with the corresponding presenter notes.

5. Final Report - a PDF of our final project report. This, along with the Colab notebook, is the most comprehensive record of everything done in this project. 

6. Final Project Colab Notebook - This is the master Colab notebook for our entire project. It is organized into sections for all elements of all milestones. It contains virtually all of the code we have run, and it includes some useful comments throughout to guide the reader through our process. Not all cells should be run (especially those dedicated to data pre-processing and training various models), but most things should work with the current setup of this folder. Training and evaluating models from the Colab document utilizing the current directory structure should be the easiest way to navigate all of our code. 

