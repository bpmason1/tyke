# Tyke

### Initial setup of the project (only needs to be performed once)
Install python3.11 (project prerequisite)
`./scripts/setup`

### To run antlr
`cd ./src`
`java -Xmx500M -cp ../lib/antlr-4.13.0-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 ./Tyke.g4`

### Commpile and run the example application
```
cd ./example/hello
../../scripts/tykec my-app  # compile the application into an executable named 'my-app'
./bin/my-app  # run the application
```

### Run pytest
`PYTHONPATH=$PWD/src pytest`

### Compiler high-level flow
TODO

### Language Rules
**Declare a variable**
```
let x = 1;
```

**Declare a mutable variable**
```
let mut x = 1;
```

**Define a type structure**
```
type struct Point{x: int, y: int};
type  struct Line{
	pt1: Point,
	pt2: Point
};
```

**Arithmetic**
```
let mut x = (1 + 2) * 3;
x = (x - 1) / 2;
```

**Functions**
```
def add(x: int, y: int) -> int {
	let sum = x + y;
	return sum;
}
```

**Print""
```
print("Hello World!");
```

### Example Program
```
package main;

def main() -> int {
  fibonacci(10);
  return 0;
}

def fibonacci(n: int) -> void {
  let mut n_minus_1 = 1;
  let mut n_minus_2 = 1;

  if n >= 1 {
    print("1");
  }

  if n >= 2 {
    print("1");
  }

  let mut cnt = 3;
  while cnt <= n {
    let tmp = n_minus_1 + n_minus_2;
    print(tmp);
    
    n_minus_2 = n_minus_1;
    n_minus_1 = tmp;
    cnt = cnt + 1;
  }

  return;
}
```

**TODO**
- implement strings (excluding print statements)
- enable declaring values on the heap
- garbage collection

