// checks how many solution there is to make a square shaped frame from n pieces with dimensions of w * h

import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

const piecesCount = await rl.question("");
const pieces = [];

for (let i = 0; i < piecesCount; i++) {
  const pieceDimension = await rl.question("");
  const [w, h] = pieceDimension.split(" ");
  pieces.push({ w: +w, h: +h });
}

const frameArea = pieces.reduce((acc, curr) => acc + curr.w * curr.h, 0)
const frameSide = Math.sqrt(frameArea)



console.log(frameArea);

rl.close();
