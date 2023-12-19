; ModuleID = "main"

declare i32 @"printf"(i8* %".1", ...)

define i64 @"main"()
{
entry:
  call void @"fibonacci"(i64 10)
  ret i64 0
}

define void @"fibonacci"(i64 %".1")
{
entry:
  %"n_minus_2" = alloca i64, i32 1
  %"n_minus_1" = alloca i64, i32 1
  %"n" = alloca i64, i32 1
  store i64 %".1", i64* %"n"
  store i64 1, i64* %"n_minus_1"
  store i64 1, i64* %"n_minus_2"
  %".6" = load i64, i64* %"n"
  %".7" = icmp sge i64 %".6", 1
  br i1 %".7", label %"entry.if", label %"entry.endif"
entry.if:
  %"d" = getelementptr inbounds [3 x i8], [3 x i8]* @"print_call_0", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %"d")
  br label %"entry.endif"
entry.endif:
  %".11" = load i64, i64* %"n"
  %".12" = icmp sge i64 %".11", 2
  br i1 %".12", label %"entry.endif.if", label %"entry.endif.endif"
entry.endif.if:
  %"d.1" = getelementptr inbounds [3 x i8], [3 x i8]* @"print_call_1", i32 0, i32 0
  %".14" = call i32 (i8*, ...) @"printf"(i8* %"d.1")
  br label %"entry.endif.endif"
entry.endif.endif:
  %"cnt" = alloca i64, i32 1
  store i64 3, i64* %"cnt"
  br label %"predicate.while.9c0c1cd4d7cee59b98683dbc0e0a8729"
predicate.while.9c0c1cd4d7cee59b98683dbc0e0a8729:
  %".18" = load i64, i64* %"cnt"
  %".19" = load i64, i64* %"n"
  %".20" = icmp sle i64 %".18", %".19"
  br i1 %".20", label %"entry.while.9c0c1cd4d7cee59b98683dbc0e0a8729", label %"exit.while.9c0c1cd4d7cee59b98683dbc0e0a8729"
entry.while.9c0c1cd4d7cee59b98683dbc0e0a8729:
  %"tmp" = alloca i64, i32 1
  %".22" = load i64, i64* %"n_minus_1"
  %".23" = load i64, i64* %"n_minus_2"
  %".24" = add i64 %".22", %".23"
  store i64 %".24", i64* %"tmp"
  %".26" = load i64, i64* %"tmp"
  %"d.2" = getelementptr inbounds [4 x i8], [4 x i8]* @"print_call_2", i32 0, i32 0
  %".27" = call i32 (i8*, ...) @"printf"(i8* %"d.2", i64 %".26")
  %".28" = load i64, i64* %"n_minus_1"
  store i64 %".28", i64* %"n_minus_2"
  %".30" = load i64, i64* %"tmp"
  store i64 %".30", i64* %"n_minus_1"
  %".32" = load i64, i64* %"cnt"
  %".33" = add i64 %".32", 1
  store i64 %".33", i64* %"cnt"
  br label %"predicate.while.9c0c1cd4d7cee59b98683dbc0e0a8729"
exit.while.9c0c1cd4d7cee59b98683dbc0e0a8729:
  ret void
}

@"print_call_0" = global [3 x i8] c"1\0a\00"
@"print_call_1" = global [3 x i8] c"1\0a\00"
@"print_call_2" = global [4 x i8] c"%d\0a\00"

