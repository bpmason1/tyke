; ModuleID = "main"

declare i32 @"printf"(i8* %".1", ...)

define i64 @"main"()
{
entry:
  %"x" = alloca i64, i32 1
  store i64 4, i64* %"x"
  br label %"predicate.while.28ae19aa907f5f42160d0d2db098015e"
predicate.while.28ae19aa907f5f42160d0d2db098015e:
  %".4" = load i64, i64* %"x"
  %".5" = icmp sge i64 %".4", 0
  br i1 %".5", label %"entry.while.28ae19aa907f5f42160d0d2db098015e", label %"exit.while.28ae19aa907f5f42160d0d2db098015e"
entry.while.28ae19aa907f5f42160d0d2db098015e:
  %".7" = load i64, i64* %"x"
  %"d" = getelementptr inbounds [4 x i8], [4 x i8]* @"print_call_0", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %"d", i64 %".7")
  %".9" = load i64, i64* %"x"
  %".10" = sub i64 %".9", 1
  store i64 %".10", i64* %"x"
  br label %"predicate.while.28ae19aa907f5f42160d0d2db098015e"
exit.while.28ae19aa907f5f42160d0d2db098015e:
  ret i64 0
}

@"print_call_0" = global [4 x i8] c"%d\0a\00"
