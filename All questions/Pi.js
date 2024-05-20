function Pi() {
  let pi = 0;
  let sign = 1; // This alternates between 1 and -1
  let denominator = 1; // Starts with 1 and increments by 2 each iteration
  let iterations = 0;
  const maxIterations = 1000000; // A big number of iterations for better accuracy

  while (iterations < maxIterations) {
    pi += sign * (4 / denominator);
    denominator += 2;
    sign *= -1; // Alternate the sign
    iterations++;
  }

  return pi.toFixed(4);
}

console.log(Pi());
