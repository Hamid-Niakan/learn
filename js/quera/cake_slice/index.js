const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function calculateSectorArea(radius, startAngle, endAngle) {
  if (endAngle < startAngle) endAngle + 360;
  // Convert degrees to radians
  const startRadians = (startAngle * Math.PI) / 180;
  const endRadians = (endAngle * Math.PI) / 180;

  // Calculate central angle in radians
  const centralAngleRadians = endRadians - startRadians;

  // Calculate area of sector
  return 0.5 * radius * radius * centralAngleRadians;
}

rl.question("", (guestCount) => {
  rl.question("", (degrees) => {
    const degreesArray = degrees.split(" ").map((degree) => parseFloat(degree));
    degreesArray.sort((a, b) => a - b);
    guestCount = parseInt(guestCount);
    const sectorAreas = [];

    for (let i = 0; i < degreesArray.length; i++) {
      if (i !== degreesArray.length - 1)
        sectorAreas.push(
          calculateSectorArea(1, degreesArray[i], degreesArray[i + 1])
        );
      else
        sectorAreas.push(
          calculateSectorArea(1, degreesArray[i], degreesArray[0])
        );
    }

    const maxSectorArea = Math.max(...sectorAreas);
    const maxSectorPercentage = (maxSectorArea / Math.PI) * 100;

    console.log(parseFloat(maxSectorPercentage.toFixed(3)));

    rl.close();
  });
});
