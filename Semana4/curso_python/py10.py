# Use Underlying Operating System Functionality

import os
from datetime import datetime

#print(dir(os))
print(os.getcwd())
os.chdir('/home/alan/Downloads/Sistemas Digitais para Mecatrônica/code/SEII-ALAN-NASCIMENTO-DE-PAULA/Semana4')
print(os.getcwd())
print(os.listdir())

# os.mkdir() criar diretório
# os.makedirs('Teste/Sub-Test') # criar diretório e sub-diretório
# os.removedirs('Teste/Sub-Test') remover diretório

# os.rename('old name', 'new name') # renomear

for dirpath, dirnames, filenames in os.walk('/home/alan/Downloads/Sistemas Digitais para Mecatrônica/code/SEII-ALAN-NASCIMENTO-DE-PAULA/Semana4'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.isdir('/tmp/fgadfadafd'))
print(dir(os.path))