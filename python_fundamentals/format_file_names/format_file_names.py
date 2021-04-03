from os import listdir
from os import rename

def getFileNames(path):
	return listdir(path)

def renameFiles(path, fileList):
	for file in fileList:
		rename(path + file, path + file.strip('0123456789'))


if __name__ == "__main__":
	path = r"/home/milind/Documents/fsd/format_file_names/file_names/"
	fileList = getFileNames(path)
	renameFiles(path, fileList)