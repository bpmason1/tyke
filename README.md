# Tyke

### To run antlr
`cd ./src`
`java -Xmx500M -cp ../lib/antlr-4.13.0-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 ./Tyke.g4`

### Commpile and run the example application
```
cd ./example/hello
../../scripts/tykec  # compile the application
cd ./bin
./example  # run the application
```

### Compiler high-level flow
