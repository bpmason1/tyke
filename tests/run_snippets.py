from main import processCodeStr
from colorama import Fore, Style
import os
from nose.tools import assert_equal

assert_equal.__self__.maxDiff = None

def getExpected(file_name_no_ext):
    with open(file_name_no_ext + '.ll', 'r') as fd:
        return fd.read()

def getActual(file_name_no_ext):
    with open(file_name_no_ext + '.mamba', 'r') as fd:
        srcCode = fd.read()

    packageDictLL = processCodeStr(srcCode)
    mainLL = packageDictLL['main']
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
            file_names_no_ext.append(snippetDir + fName[:-6])

    return file_names_no_ext

def runAll():
    snippetDir = './snippets/'

    for fName in getBaseFileNameList(snippetDir):
        runOne(fName)

if __name__ == '__main__':
    runAll()
