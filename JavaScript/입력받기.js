const fs = require("fs");
let inputOneLine = fs
  // .readFileSync("dev/stdin")
  .readFileSync("./dev/1.txt", "utf8")
  .toString()
  .trim();

console.log(inputOneLine);

let inputMultiLine = fs
  // .readFileSync("dev/stdin")
  .readFileSync("./dev/2.txt", "utf8")
  .toString()
  .trim()
  .split("\n");

console.log(inputMultiLine);

/* 입력 파일 형태
5 8 3
2 4 5 4 6
*/

const input = fs
  .readFileSync("./dev/3.txt")
  .toString()
  .trim()
  .split("\n"); //줄바꿈 처리 추가

let [nums, arr] = input;
console.log(nums, arr); //5 8 3 2 4 5 4 6

let [n, m, k] = nums
  .split(" ")
  .map((value) => +value); //공백 날리고 숫자로 변경
arr = arr
  .split(" ")
  .map((value) => +value);
console.log(n, m, k); //5 8 3
console.log(arr); //[2, 4, 5, 4, 6]
