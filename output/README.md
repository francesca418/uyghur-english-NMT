# Output Folder

This folder contains several subdirectories. They are as follows:

1. test-gold/ - the gold test data

2. test-simple-baseline/ - the simple baseline predictions in English and Uyghur (both Arabic and Latin scripts)

3. test-published-baseline/ - the published baseline predictions in English and Uyghur (both Arabic and Latin scripts), for models translating from English-Uyghur (Arabic), English-Uyghur (Latin), Uyghur (Arabic) to English, and Uyghur (Latin) to English. (Note: anything denoted "transliterated" means the Uyghur text used was in Latin script.)

4. test-related-languages/ - the predictions in English made by Uyghur (Arabic) to English and Uyghur (Latin) to English models trained with training data augmented by some parallel Uzbek-English data

5. test-combined-dev/ - the predictions in English and Uyghur (both Arabic and Latin scripts), for models translating from English-Uyghur (Arabic), English-Uyghur (Latin), Uyghur (Arabic) to English, and Uyghur (Latin) to English. These results were predicted by models trained using the modified development set described in the final report

For information about how to run our scoring script, please refer to either the README.md file contained in the code folder or the master Colab notebook, which contains everything needed to step through the process of our project. 

(For reference: "python score.py gold-filepath pred-filepath" in the command line should evaluate these predictions.)