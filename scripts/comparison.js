// Comparison operators
// >, <, >=, <=

// equality
2 == 2 // true
"2" == 2 // true
"2" === 2 // false
"user" == "user" // true

// inequality
5 != "5" // false
5 !== "5" // true

// 
true == 1 // true
true === 1 // false

// 
null == undefined // true
null === undefined // false
NaN == NaN // false

// Logical Operators
1 === 1 && 2 === 2 // true
1 === 1 && 2 === 2 && 2 === 1 // false
1 === 2 || 2 === 2 // true
!1 === 1 // false
!!1 === 1 // true

// EXERCISES
let x = 1
let y = 2

// 1
"2" == y && x === 1; // true

// 2
x >= 0 || y === "2"; // true

// 3
!(x !== 1) && y === (1 + 1); // true

// 4
y !== "2" && x < 10; // false

// 5
y !== x || y == "2" || x === 3; // true