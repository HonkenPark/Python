import os
# import eyed3

root_folder = input("Input Path: ")
files = os.listdir(root_folder)
for file in files:
    # audiofile = eyed3.load(file)
    # print(audiofile.tag.title)
    
    if file[-4:] == ".mp3":
        old_path = os.path.join(root_folder, file)
        new_path = os.path.join(root_folder, file[3:])
        os.rename(old_path, new_path)