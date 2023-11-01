
from cx_Freeze import setup,Executable
# Mettre ce fichier et Lab3_12.py dans c:Python36
# Écrire python setup.py build
# L'exécutable est dans le dossier build dans python36
setup(
    name='Lab3_12',
    version='1.0',
    url='lmiot.fr',
    license='CopyLeft',
    author='Denis RÉANT',
    author_email='denis.reant@baloubou.com',
    description="Ce programme permet donner n'importe quelle table de muliplication.",
    executables=[Executable("Lab3_12.py")])
