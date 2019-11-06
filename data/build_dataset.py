import os
import random 

projdir = os.getcwd() #start out in data folder
path = projdir + "/AudioWAV/" 
os.chdir(path) 

filenames = os.listdir() 
filenames.sort()
random.seed(204)
'''
Note: these files are not independent, so randomly shuffling the files to put
them into 3 data sets will bias your results.
To create a train, dev, and test set, you first need to
group files with the same voices in them together so that all of them can be in one
set.
If you change this to shuffle the participant numbers, i.e. the first four digits of the
filenames, and then put all filenames with that prefix into the correct set, then this 
will work.
'''
random.shuffle(filenames)

devsplitpoint = int(0.8*len(filenames))
testsplitpoint = int(0.9*len(filenames))

train_filenames = filenames[0:devsplitpoint]
dev_filenames = filenames[devsplitpoint : testsplitpoint]
test_filenames = filenames[testsplitpoint:]


#create folders for our split sets and move them in
os.mkdir("train")
os.mkdir("dev")
os.mkdir("test")
    
print(os.getcwd())

for f in train_filenames:
    os.rename(path+f, path+"train/"+f)

for f in dev_filenames:
    os.rename(path+f, path+"dev/"+f)

for f in test_filenames:
    os.rename(path+f, path+"test/"+f)
