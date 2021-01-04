from main import run as main_run
from colorama import Fore, Style
import os
from nose.tools import assert_equal

assert_equal.__self__.maxDiff = None

def getExpected(file_name_no_ext):
    with open(file_name_no_ext + '.ll', 'r') as fd:
        return fd.read()

def getActual(file_name_no_ext):
    mambaFileList = [file_name_no_ext + '.mamba']
    packageDictLL = main_run(mambaFileList)
    mainLL = packageDictLL['main']
    # print(mainLL)
    return str(mainLL)

def runOne(file_name_no_ext):
    msg = f"Testing file {file_name_no_ext}.mamba"
    print(Fore.GREEN + msg + Style.RESET_ALL)

    actual = getActual(file_name_no_ext).strip()
    expected = getExpected(file_name_no_ext).strip()

    assert_equal(actual, expected)

def getBaseFileNameList(snippetDir):
    all_file_list = os.listdir(snippetDir)
    file_names_no_ext = []
    for fName in all_file_list:
        if fName.endswith('.mamba'):
            dir_name = os.path.join(snippetDir, fName[:-6])
            file_names_no_ext.append(dir_name)

    return file_names_no_ext

def runAll():
    cur_dir = os.path.dirname(__file__)
    snippetDir = os.path.join(cur_dir, 'snippets')

    for fName in getBaseFileNameList(snippetDir):
        runOne(fName)

if __name__ == '__main__':
    runAll()
