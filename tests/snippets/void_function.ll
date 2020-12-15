; ModuleID = "main"

define void @"abyss"() 
{
entry:
  ret void
}

define void @"vanish"(i64 %".1", double %".2") 
{
entry:
  %"y" = alloca double, i32 1
  %"x" = alloca i64, i32 1
  store i64 %".1", i64* %"x"
  store double %".2", double* %"y"
  ret void
}

define i64 @"doAssign"(i64 %".1") 
{
entry:
  %"newVal" = alloca i64, i32 1
  %"data" = alloca i64, i32 1
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
  %"second" = alloca i64, i32 1
  %"first" = alloca i64, i32 1
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

define i64 @"returnCalcResult"(i64 %".1", i64 %".2") 
{
entry:
  %"second" = alloca i64, i32 1
  %"first" = alloca i64, i32 1
  store i64 %".1", i64* %"first"
  store i64 %".2", i64* %"second"
  %".6" = load i64, i64* %"first"
  %".7" = add i64 %".6", 6
  %".8" = load i64, i64* %"second"
  %".9" = add i64 %".8", 5
  %".10" = mul i64 2, %".9"
  %".11" = add i64 %".7", %".10"
  ret i64 %".11"
}

define i1 @"retBool"(i64 %".1", i64 %".2") 
{
entry:
  %"isLessThan" = alloca i1, i32 1
  %"y" = alloca i64, i32 1
  %"x" = alloca i64, i32 1
  store i64 %".1", i64* %"x"
  store i64 %".2", i64* %"y"
  %".6" = load i64, i64* %"x"
  %".7" = load i64, i64* %"y"
  %".8" = icmp slt i64 %".6", %".7"
  store i1 %".8", i1* %"isLessThan"
  %".10" = load i1, i1* %"isLessThan"
  ret i1 %".10"
}

define i64 @"one"() 
{
entry:
  ret i64 1
}

define i64 @"floor_zero"(i64 %".1", i64 %".2") 
{
entry:
  %"y" = alloca i64, i32 1
  %"x" = alloca i64, i32 1
  store i64 %".1", i64* %"x"
  store i64 %".2", i64* %"y"
  %".6" = load i64, i64* %"x"
  %".7" = icmp slt i64 %".6", 0
  br i1 %".7", label %"entry.if", label %"entry.endif"
entry.if:
  ret i64 0
entry.endif:
  %".10" = load i64, i64* %"x"
  ret i64 %".10"
}

define i64 @"either_or"(i64 %".1", i64 %".2") 
{
entry:
  %"y" = alloca i64, i32 1
  %"x" = alloca i64, i32 1
  store i64 %".1", i64* %"x"
  store i64 %".2", i64* %"y"
  %".6" = load i64, i64* %"x"
  %".7" = icmp slt i64 %".6", 0
  br i1 %".7", label %"entry.if", label %"entry.else"
entry.if:
  %".9" = load i64, i64* %"x"
  ret i64 %".9"
entry.else:
  %".11" = load i64, i64* %"y"
  ret i64 %".11"
entry.endif:
  ret i64 0
}

define i64 @"if_elif_else_chain"(i64 %".1", i64 %".2") 
{
entry:
  %"y" = alloca i64, i32 1
  %"x" = alloca i64, i32 1
  store i64 %".1", i64* %"x"
  store i64 %".2", i64* %"y"
  %".6" = load i64, i64* %"x"
  %".7" = icmp eq i64 %".6", 0
  br i1 %".7", label %"entry.if", label %"entry.else"
entry.if:
  ret i64 1
entry.else:
  %".10" = load i64, i64* %"y"
  %".11" = icmp eq i64 %".10", 0
  br i1 %".11", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ret i64 0
entry.else.if:
  ret i64 2
entry.else.else:
  %".14" = load i64, i64* %"x"
  %".15" = icmp sgt i64 %".14", 1
  br i1 %".15", label %"entry.else.else.if", label %"entry.else.else.else"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  ret i64 3
entry.else.else.else:
  %".18" = load i64, i64* %"y"
  %".19" = icmp eq i64 %".18", 1
  br i1 %".19", label %"entry.else.else.else.if", label %"entry.else.else.else.else"
entry.else.else.endif:
  br label %"entry.else.endif"
entry.else.else.else.if:
  ret i64 4
entry.else.else.else.else:
  ret i64 7
entry.else.else.else.endif:
  br label %"entry.else.else.endif"
}
