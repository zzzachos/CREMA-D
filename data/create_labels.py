###
#provides lists of labels for the CREMA-D dataset in the split train, dev, test folders
#also provides additional information: the sentences spoken, demographic info on speaker
#demographic info function is unfinished


import os
import re

projstartdir = os.getcwd() #start out in data folder
projpath = projstartdir + "/AudioWAV/" 
#os.chdir(path) 

emolist = ["ANG", "DIS", "FEA", "HAP", "NEU", "SAD"]
intensitylist = ["XX", "LO", "MD", "HI"]

#function which creates a list of filenames and a corresponding list of labels
#the labels are emotions corresponding to emo list above 
#and we also have a corresponding list of intensity levels, which is optional for us to use
def labelme(dir="train"):
    path = projpath + dir + "/"# is it good practice to  change directory in the middle of a function like this?
    os.chdir(path)
    filenames = os.listdir()
    filenames.sort()
    labels = [""]*len(filenames)
    intensities =[""]*len(filenames)
    for i in range(0, len(filenames)):
        try:
            emo = re.search("\d\d\d\d_\D\D\D_(.+?)_\D\D.wav", filenames[i]).group(1)
            labels[i] = emolist.index(emo)
        except:
            None
        try:
            ints = re.search("\d\d\d\d_\D\D\D_\D\D\D?\D_(.+?).wav", filenames[i]).group(1)
            intensities[i] = intensitylist.index(ints)
        except:
            None
    return filenames, labels, intensities
    


# returns lists with demographic information, like race and sex of speaker
# could be useful for manual error analysis
def demographic_info(dir="train"):
    return None
    
sentencelist = ["IEO", "TIE", "IOM", "IWW", "TAI", "MTI", "IWL", "ITH", "DFA", "ITS", "TSI", "WSI"]    
# returns lists with sentence spoken
# could be useful for manual error analysis
def sentence_spoken(dir="train"):
    path = projpath + dir + "/"# is it good practice to  change directory in the middle of a function like this?
    os.chdir(path)
    filenames = os.listdir()
    filenames.sort()
    sentences = [""]*len(filenames)
    for i in range(0, len(filenames)):
        try:
            sentence = re.search("\d\d\d\d_(.+?)_\D\D\D_\D\D.wav", filenames[i]).group(1)
            sentences[i] = sentencelist.index(sentence)
        except:
            None
    return sentences
    

def check_if_works():
    trainfiles, trainlabels, trainints = labelme()
    devfiles, devlabels, devints = labelme("dev")
    testfiles, testlabels, testints = labelme("test")
    testsentences = sentence_spoken("test")
    all_data = {
        "train_labels" : trainlabels, 
        "train_files" : trainfiles,
        "train_intensities" : trainints,
        "dev_labels" : devlabels, 
        "dev_files" : devfiles,
        "dev_intensities" : devints,
        "test_labels" : testlabels,
        "test_files" : testfiles,
        "test_intensities" : testints,
        "test_sentences" : testsentences
        }
    return all_data

if __name__ == "__main__":
    #print(check_if_works())  