; ModuleID = "main"

%"Point" = type {i64, i64}
%"Line" = type {%"Point", %"Point"}
%"Rect" = type {i64, i64, i64}
declare i32 @"printf"(i8* %".1", ...) 

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

define i64 @"pow"(i64 %".1", i64 %".2") 
{
entry:
  %"exp" = alloca i64, i32 1
  %"num" = alloca i64, i32 1
  store i64 %".1", i64* %"num"
  store i64 %".2", i64* %"exp"
  %".6" = load i64, i64* %"exp"
  %".7" = icmp eq i64 %".6", 0
  br i1 %".7", label %"entry.if", label %"entry.endif"
entry.if:
  ret i64 1
entry.endif:
  %"counter" = alloca i64, i32 1
  %"total" = alloca i64, i32 1
  store i64 1, i64* %"total"
  %".11" = load i64, i64* %"exp"
  store i64 %".11", i64* %"counter"
  br label %"predicate.while.2c185b73965a07d55805e616d7ab4ce8"
predicate.while.2c185b73965a07d55805e616d7ab4ce8:
  %".14" = load i64, i64* %"counter"
  %".15" = icmp sgt i64 %".14", 0
  br i1 %".15", label %"entry.while.2c185b73965a07d55805e616d7ab4ce8", label %"exit.while.2c185b73965a07d55805e616d7ab4ce8"
entry.while.2c185b73965a07d55805e616d7ab4ce8:
  %".17" = load i64, i64* %"total"
  %".18" = load i64, i64* %"num"
  %".19" = mul i64 %".17", %".18"
  store i64 %".19", i64* %"total"
  %".21" = load i64, i64* %"counter"
  %".22" = sub i64 %".21", 1
  store i64 %".22", i64* %"counter"
  br label %"predicate.while.2c185b73965a07d55805e616d7ab4ce8"
exit.while.2c185b73965a07d55805e616d7ab4ce8:
  %".25" = load i64, i64* %"total"
  ret i64 %".25"
}

define i64 @"rise"(%"Line" %".1") 
{
entry:
  %"y2" = alloca i64, i32 1
  %"y1" = alloca i64, i32 1
  %"line" = alloca %"Line", i32 1
  store %"Line" %".1", %"Line"* %"line"
  %".4" = getelementptr inbounds %"Line", %"Line"* %"line", i32 0, i32 0, i32 1
  %".5" = load i64, i64* %".4"
  store i64 %".5", i64* %"y1"
  %".7" = getelementptr inbounds %"Line", %"Line"* %"line", i32 0, i32 1, i32 1
  %".8" = load i64, i64* %".7"
  store i64 %".8", i64* %"y2"
  %".10" = load i64, i64* %"y2"
  %".11" = load i64, i64* %"y1"
  %".12" = sub i64 %".10", %".11"
  ret i64 %".12"
}

define %"Line" @"newLine"(i64 %".1", i64 %".2", i64 %".3", i64 %".4") 
{
entry:
  %"line" = alloca %"Line", i32 1
  %"point2" = alloca %"Point", i32 1
  %"y2" = alloca i64, i32 1
  %"x2" = alloca i64, i32 1
  %"y1" = alloca i64, i32 1
  %"x1" = alloca i64, i32 1
  store i64 %".1", i64* %"x1"
  store i64 %".2", i64* %"y1"
  store i64 %".3", i64* %"x2"
  store i64 %".4", i64* %"y2"
  %".10" = load i64, i64* %"x2"
  %".11" = load i64, i64* %"y2"
  %".12" = getelementptr inbounds %"Point", %"Point"* %"point2", i32 0, i32 0
  store i64 %".10", i64* %".12"
  %".14" = getelementptr inbounds %"Point", %"Point"* %"point2", i32 0, i32 1
  store i64 %".11", i64* %".14"
  %".16" = load i64, i64* %"x1"
  %".17" = load i64, i64* %"y1"
  %".18" = load %"Point", %"Point"* %"point2"
  %".19" = getelementptr inbounds %"Line", %"Line"* %"line", i32 0, i32 0
  %".20" = getelementptr inbounds %"Point", %"Point"* %".19", i32 0, i32 0
  store i64 %".16", i64* %".20"
  %".22" = getelementptr inbounds %"Point", %"Point"* %".19", i32 0, i32 1
  store i64 %".17", i64* %".22"
  %".24" = getelementptr inbounds %"Line", %"Line"* %"line", i32 0, i32 1
  store %"Point" %".18", %"Point"* %".24"
  %".26" = load %"Line", %"Line"* %"line"
  ret %"Line" %".26"
}

define %"Point" @"swap"(%"Point" %".1") 
{
entry:
  %"tmpX" = alloca i64, i32 1
  %"pt" = alloca %"Point", i32 1
  store %"Point" %".1", %"Point"* %"pt"
  %".4" = getelementptr inbounds %"Point", %"Point"* %"pt", i32 0, i32 0
  %".5" = load i64, i64* %".4"
  store i64 %".5", i64* %"tmpX"
  %".7" = getelementptr inbounds %"Point", %"Point"* %"pt", i32 0, i32 1
  %".8" = load i64, i64* %".7"
  %".9" = getelementptr inbounds %"Point", %"Point"* %"pt", i32 0, i32 0
  store i64 %".8", i64* %".9"
  %".11" = load i64, i64* %"tmpX"
  %".12" = getelementptr inbounds %"Point", %"Point"* %"pt", i32 0, i32 1
  store i64 %".11", i64* %".12"
  %".14" = load %"Point", %"Point"* %"pt"
  ret %"Point" %".14"
}

define i64 @"make_point"() 
{
entry:
  %"point" = alloca %"Point", i32 1
  %".2" = getelementptr inbounds %"Point", %"Point"* %"point", i32 0, i32 0
  store i64 3, i64* %".2"
  %".4" = getelementptr inbounds %"Point", %"Point"* %"point", i32 0, i32 1
  store i64 5, i64* %".4"
  %".6" = getelementptr inbounds %"Point", %"Point"* %"point", i32 0, i32 1
  %".7" = load i64, i64* %".6"
  ret i64 %".7"
}

define i64 @"fibonacci"(i64 %".1") 
{
entry:
  %"n" = alloca i64, i32 1
  store i64 %".1", i64* %"n"
  %".4" = load i64, i64* %"n"
  %".5" = icmp sle i64 %".4", 2
  br i1 %".5", label %"entry.if", label %"entry.endif"
entry.if:
  ret i64 1
entry.endif:
  %"n_minus_2" = alloca i64, i32 1
  %"n_minus_1" = alloca i64, i32 1
  %".8" = load i64, i64* %"n"
  %".9" = sub i64 %".8", 1
  store i64 %".9", i64* %"n_minus_1"
  %".11" = load i64, i64* %"n"
  %".12" = sub i64 %".11", 2
  store i64 %".12", i64* %"n_minus_2"
  %".14" = load i64, i64* %"n_minus_1"
  %".15" = call i64 @"fibonacci"(i64 %".14")
  %".16" = load i64, i64* %"n_minus_2"
  %".17" = call i64 @"fibonacci"(i64 %".16")
  %".18" = add i64 %".15", %".17"
  ret i64 %".18"
}
