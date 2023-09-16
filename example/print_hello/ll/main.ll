; ModuleID = "main"

declare i32 @"printf"(i8* %".1", ...)

define i64 @"main"()
{
entry:
  %"d" = getelementptr inbounds [14 x i8], [14 x i8]* @"print_call_0", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"d")
  ret i64 0
}

@"print_call_0" = global [14 x i8] c"Hello World!\0a\00"

