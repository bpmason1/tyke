; ModuleID = "main"

declare i32 @"printf"(i8* %".1", ...)

define i64 @"main"()
{
entry:
  %"x" = alloca i64, i32 1
  store i64 5, i64* %"x"
  br label %"predicate.while.635db1d4369930b51ec7188e2e5c5a23"
predicate.while.635db1d4369930b51ec7188e2e5c5a23:
  %".4" = load i64, i64* %"x"
  %".5" = icmp sgt i64 %".4", 0
  br i1 %".5", label %"entry.while.635db1d4369930b51ec7188e2e5c5a23", label %"exit.while.635db1d4369930b51ec7188e2e5c5a23"
entry.while.635db1d4369930b51ec7188e2e5c5a23:
  %".7" = load i64, i64* %"x"
  %".8" = sub i64 %".7", 1
  store i64 %".8", i64* %"x"
  %".10" = load i64, i64* %"x"
  %".11" = icmp sgt i64 %".10", 2
  br i1 %".11", label %"entry.while.635db1d4369930b51ec7188e2e5c5a23.if", label %"entry.while.635db1d4369930b51ec7188e2e5c5a23.endif"
exit.while.635db1d4369930b51ec7188e2e5c5a23:
  ret i64 0
entry.while.635db1d4369930b51ec7188e2e5c5a23.if:
  br label %"predicate.while.635db1d4369930b51ec7188e2e5c5a23"
entry.while.635db1d4369930b51ec7188e2e5c5a23.endif:
  %".14" = load i64, i64* %"x"
  %"d" = getelementptr inbounds [4 x i8], [4 x i8]* @"print_call_0", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %"d", i64 %".14")
  br label %"predicate.while.635db1d4369930b51ec7188e2e5c5a23"
}

@"print_call_0" = global [4 x i8] c"%d\0a\00"

