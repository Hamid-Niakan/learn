const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('', (firstRow) => {
  rl.question('', (secondRow) => {
    firstRow = firstRow.split(' ')
    secondRow = secondRow.split(' ')

    let activePairsCount = 0

    for (let i = 0; i < firstRow.length; i++) {
      if (firstRow[i] === '1' && firstRow[i] === secondRow[i]) activePairsCount++
    }

    console.log(activePairsCount)

    rl.close()
  })
})