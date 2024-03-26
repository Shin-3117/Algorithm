const fibo = (idx, memo = {}) => {
  if (idx <= 2) return 1;
  if (idx in memo) return memo[idx];
  memo[idx] =
    fibo(idx - 1, memo) +
    fibo(idx - 2, memo);
  return memo[idx];
};
const sol = fibo(10);
console.log(sol);
