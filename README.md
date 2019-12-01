# mamba

### To run antlr
`cd ./src`
`java -Xmx500M -cp ~/jars/antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 ./Mamba.g4`

### To run application
`cd ./src`
`python main.py 2>&1 | grep -v VAR_TYPE`

