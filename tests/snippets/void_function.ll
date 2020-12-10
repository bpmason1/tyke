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

define i64 @"assignMultiply"() 
{
entry:
  %"calc" = alloca i64, i32 1
  %".2" = mul i64 3, 9
  store i64 %".2", i64* %"calc"
  %".4" = load i64, i64* %"calc"
  ret i64 %".4"
}

define i64 @"arithMultiGroup"(i64 %".1", i64 %".2") 
{
entry:
  %"calc" = alloca i64, i32 1
  %"second" = alloca i64
  %"first" = alloca i64
  store i64 %".1", i64* %"first"
  store i64 %".2", i64* %"second"
  %".6" = load i64, i64* %"first"
  %".7" = add i64 %".6", 6
  %".8" = load i64, i64* %"second"
  %".9" = add i64 %".8", 5
  %".10" = mul i64 %".7", %".9"
  %".11" = add i64 %".10", 1
  store i64 %".11", i64* %"calc"
  %".13" = load i64, i64* %"calc"
  ret i64 %".13"
}