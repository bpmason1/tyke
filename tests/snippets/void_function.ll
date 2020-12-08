; ModuleID = "main"

define void @"abyss"() 
{
entry:
  ret void
}

define void @"vanish"(i64 %".1", double %".2") 
{
entry:
  %"y" = alloca double
  %"x" = alloca i64
  store i64 %".1", i64* %"x"
  store double %".2", double* %"y"
  ret void
}

define i64 @"doAssign"(i64 %".1") 
{
entry:
  %"newVal" = alloca i64, i32 1
  %"data" = alloca i64
  store i64 %".1", i64* %"data"
  %".4" = load i64, i64* %"data"
  store i64 %".4", i64* %"newVal"
  %".6" = load i64, i64* %"newVal"
  ret i64 %".6"
}