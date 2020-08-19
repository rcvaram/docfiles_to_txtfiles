import os
import textract
import glob

def get_files(folder, ext):
  if os.path.isdir(folder):
    file_names = "{}/*.{}".format(folder, ext)
    return glob.glob(file_names)
    
def doc_files_2_txt_files(folder_path):
  docx_files = get_files(folder_path,'docx')
  doc_files = get_files(folder_path,'doc')
  files = docx_files + doc_files
  for file in files:
    fname = file.split('.')[0]
    text = textract.process(file)
    text = text.decode("utf-8")
    text = text.replace('\n\n', '\n')
    with open('{}.txt'.format(fname),'w+') as f:
      f.write(text)

