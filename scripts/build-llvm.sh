NAME=${1:-mamba}

# translate IR to bytecode
llvm-as -f ${NAME}.ll

# translate bytecode to assemly
llc ${NAME}.bc

# compile assembly
# g++ -o myApp mamba.s

APP_NAME=$NAME
if [ -f $APP_NAME ]; then
    rm -f ./$APP_NAME
fi

clang -o $APP_NAME -O4 $NAME.s

