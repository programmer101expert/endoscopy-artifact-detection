import glob, os

# Current directory
#current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = '/home/sibaji/Downloads/Internship/artifact/endoscopy-artefact-detection-_ead_-dataset/darknet/data/obj'
# Directory where the data will reside, relative to 'darknet.exe'
path_data = 'data/obj/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.jpg' + "\n")
    else:
        file_train.write(path_data + title + '.jpg' + "\n")
        counter = counter + 1