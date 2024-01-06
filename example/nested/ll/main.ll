; ModuleID = "main"

declare i32 @"printf"(i8* %".1", ...)

define i64 @"main"()
{
entry:
  %"x" = alloca i64, i32 1
  store i64 2, i64* %"x"
  br label %"predicate.while.d292f2b0bb97ee1c72c5fe4a30ec16cb"
predicate.while.d292f2b0bb97ee1c72c5fe4a30ec16cb:
  %".4" = load i64, i64* %"x"
  %".5" = icmp sge i64 %".4", 0
  br i1 %".5", label %"entry.while.d292f2b0bb97ee1c72c5fe4a30ec16cb", label %"exit.while.d292f2b0bb97ee1c72c5fe4a30ec16cb"
entry.while.d292f2b0bb97ee1c72c5fe4a30ec16cb:
  %"y" = alloca i64, i32 1
  store i64 2, i64* %"y"
  br label %"predicate.while.a5cb548d313b6a5fcae378065fe42b53"
exit.while.d292f2b0bb97ee1c72c5fe4a30ec16cb:
  ret i64 0
predicate.while.a5cb548d313b6a5fcae378065fe42b53:
  %".9" = load i64, i64* %"y"
  %".10" = icmp sge i64 %".9", 0
  br i1 %".10", label %"entry.while.a5cb548d313b6a5fcae378065fe42b53", label %"exit.while.a5cb548d313b6a5fcae378065fe42b53"
entry.while.a5cb548d313b6a5fcae378065fe42b53:
  %".12" = load i64, i64* %"x"
  %".13" = load i64, i64* %"y"
  %".14" = icmp eq i64 %".12", %".13"
  br i1 %".14", label %"entry.while.a5cb548d313b6a5fcae378065fe42b53.if", label %"entry.while.a5cb548d313b6a5fcae378065fe42b53.endif"
exit.while.a5cb548d313b6a5fcae378065fe42b53:
  %".29" = load i64, i64* %"x"
  %".30" = sub i64 %".29", 1
  store i64 %".30", i64* %"x"
  br label %"predicate.while.d292f2b0bb97ee1c72c5fe4a30ec16cb"
entry.while.a5cb548d313b6a5fcae378065fe42b53.if:
  %"d" = getelementptr inbounds [9 x i8], [9 x i8]* @"print_call_0", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"d")
  br label %"entry.while.a5cb548d313b6a5fcae378065fe42b53.endif"
entry.while.a5cb548d313b6a5fcae378065fe42b53.endif:
  %"d.1" = getelementptr inbounds [2 x i8], [2 x i8]* @"print_call_1", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %"d.1")
  %".19" = load i64, i64* %"x"
  %"d.2" = getelementptr inbounds [3 x i8], [3 x i8]* @"print_call_2", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %"d.2", i64 %".19")
  %"d.3" = getelementptr inbounds [2 x i8], [2 x i8]* @"print_call_3", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %"d.3")
  %".22" = load i64, i64* %"y"
  %"d.4" = getelementptr inbounds [3 x i8], [3 x i8]* @"print_call_4", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %"d.4", i64 %".22")
  %"d.5" = getelementptr inbounds [3 x i8], [3 x i8]* @"print_call_5", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %"d.5")
  %".25" = load i64, i64* %"y"
  %".26" = sub i64 %".25", 1
  store i64 %".26", i64* %"y"
  br label %"predicate.while.a5cb548d313b6a5fcae378065fe42b53"
}

@"print_call_0" = global [9 x i8] c"same -> \00"
@"print_call_1" = global [2 x i8] c"(\00"
@"print_call_2" = global [3 x i8] c"%d\00"
@"print_call_3" = global [2 x i8] c",\00"
@"print_call_4" = global [3 x i8] c"%d\00"
@"print_call_5" = global [3 x i8] c")\0a\00"

