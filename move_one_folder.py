import os

source_dir = 'Images'
target_dir = 'new'
count=1
for folder in os.listdir(source_dir):
	folder_path = os.path.join(source_dir,folder)
	for file in os.listdir(folder_path):
		if not os.path.isfile(os.path.join(target_dir,file)):
			os.rename(os.path.join(folder_path,file),os.path.join(target_dir,"chinaman"+str(count)+".jpg"))
			count+=1
		# else:
		# 	os.remove(os.path.join(folder_path,file))
