const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (roads) => {
  rl.question("", (straightRoadsDirections) => {
    rl.question("", (circularRoadsDirections) => {
      straightRoadsDirections = straightRoadsDirections.split(" ");
      if (straightRoadsDirections.length < 2) console.log("NO");
      else {
        const straightRoadTypesAvailable = [
          ...new Set(straightRoadsDirections),
        ];
        if (straightRoadTypesAvailable.length === 2) console.log("YES");
        else console.log('NO')
      }
      rl.close();
    });
  });
});
