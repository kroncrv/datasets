import os
import shutil

def clean_dir(path):
    shutil.rmtree(path)
    os.mkdir(path)