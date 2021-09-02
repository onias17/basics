let x = 1

// while (x < 5) {
//   console.log("x is currently: " + x)

//   if (x === 3) {
//     console.log("x is 3")
//     break;
//   }

//   console.log("x is still less than 5, adding 1 to x");

//   x = x + 1;
// }

while (x <= 10) {
  console.log("current number: " + x);

  if (x % 2 === 0) {
    console.log(x);
  }
  
  x = x + 1;
} 