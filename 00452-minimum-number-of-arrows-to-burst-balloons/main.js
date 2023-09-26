/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function (points) {
  const ranges = points.map(([x0, x1]) => ({ start: x0, end: x1 }));
  return findMaxInter(ranges);
};
function isInRange(x, ran) {
  let x0 = ran.start;
  let x1 = ran.end;
  return x0 <= x && x <= x1;
}

function findMaxInter(points) {
  let ans = 1;
  points.sort((a, b) => a.start - b.start);
  console.log(points);
  let currentRange = points[0];
  for (let i = 1; i < points.length; i++) {
    let x0 = points[i].start;
    let x1 = points[i].end;
    if (isInRange(x0, currentRange)) {
      currentRange = {
        start: Math.max(currentRange.start, x0),
        end: Math.min(currentRange.end, x1),
      };
    } else {
      currentRange = { start: x0, end: x1 };
      ans++;
    }
    console.log("current range", currentRange);
  }
  return ans;
}

const points = [
  [3, 9],
  [7, 12],
  [3, 8],
  [6, 8],
  [9, 10],
  [2, 9],
  [0, 9],
  [3, 9],
  [0, 6],
  [2, 8],
];
const ans = findMaxInter(points);
console.log("ans", ans);
