# mamba

### To run antlr
`cd ./src`
`java -Xmx500M -cp ../lib/antlr-4.9-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 ./Mamba.g4`

### To run application
```
mkdir ./tmp
cd ./src
python main.py 2> /dev/null > ../tmp/hello.ll
cd ../tmp
../scripts/build-llvm.sh hello
```
