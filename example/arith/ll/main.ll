; ModuleID = "main"

declare i32 @"printf"(i8* %".1", ...)

define i64 @"main"()
{
entry:
  %"c" = alloca i64, i32 1
  %"b" = alloca i64, i32 1
  %"a" = alloca i64, i32 1
  %".2" = mul i64 2, 3
  %".3" = add i64 1, %".2"
  store i64 %".3", i64* %"a"
  %".5" = sdiv i64 10, 2
  %".6" = sub i64 20, %".5"
  store i64 %".6", i64* %"b"
  %".8" = load i64, i64* %"b"
  %".9" = sub i64 %".8", 12
  %".10" = load i64, i64* %"a"
  %".11" = add i64 %".10", 1
  %".12" = mul i64 %".9", %".11"
  store i64 %".12", i64* %"c"
  %".14" = load i64, i64* %"c"
  ret i64 %".14"
}

