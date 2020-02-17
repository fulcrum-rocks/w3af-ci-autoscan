# System
import sys

# Modules
import src

# Validattion
if len(sys.argv) < 2:
    print('Error! URL is not specified!')
    exit(1)

url = sys.argv[1]
template = src.getFormatedConfig(url)
src.process(template)