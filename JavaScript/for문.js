let arr1 = [0, 1, 2, 3];

for (let i = 0; i < arr1.length; i++) {
  console.log(`for문 : ${i}`);
}

for (i of arr1) {
  console.log(`for of문 : ${i}`);
}

for (i in arr1) {
  console.log(`for in문 배열 : ${i}`);
}

const obj = {
  name: "이름",
  age: "나이",
};

for (i in obj) {
  console.log(
    `for in문 객체 key/value: ${i}/${obj[i]}`
  );
}

arr1.forEach((e) => {
  console.log(e);
});

for (const [
  key,
  value,
] of Object.entries(obj)) {
  console.log(key, value);
}
