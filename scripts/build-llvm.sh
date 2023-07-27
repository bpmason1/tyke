#! /usr/bin/bash

TMP_LLVM_DIR=$1

if [ ! -d $TMP_LLVM_DIR ]; then
  tput setaf 1
  echo "Missing temp build directory: ${TMP_LLVM_DIR}"
  tput sgr0
  exit 1
fi
cd $TMP_LLVM_DIR

# if no filename is given use "tyke" as the default
NAME=${2:-tyke}

# translate IR to bytecode
llvm-as-11 -f ${NAME}.ll

# translate bytecode to assemly
llc-11 ${NAME}.bc

# compile assembly
# g++ -o myApp tyke.s

APP_NAME=$NAME
if [ -f $APP_NAME ]; then
    rm -f ./$APP_NAME
fi

clang -o $APP_NAME -O4 $NAME.s

