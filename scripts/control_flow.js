console.log("connected")

// Control Flow
let hot = false;
let temp = 40;

if (true) {
  console.log("I ran")
}

if (temp>80) {
  console.log("temp is good")
}

if (temp>80) {
  hot=true
}

console.log(hot)

if (temp>80) {
  console.log("hot outside")
} else {
  console.log("not hot")
}

if (temp>80) {
  console.log("hot outside")
} else if (temp <= 80 && temp >= 50) {
  console.log("average")
} else if (temp < 50 && temp >= 32) {
  console.log("cold outside")
} else {
  console.log("very cold")
}

let fish = 0;
let milk = 1;

let report = "blank"

if (fish >= 10 && milk >= 10) {
  report = "had great sales"
} else if (fish, milk === 0 ) {
  report = "no sales"
} else {
  report = "sold some items"
}

console.log(report)