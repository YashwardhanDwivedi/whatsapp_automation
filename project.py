int NthRoot(int n, int m) {
  // Write your code here.

  int i = 1;
  int j = m;

  while (i <= j) {
    int mid = (i + j) / 2;

    double maal = pow(mid, n);

    if (maal == m) {
      return mid;
    } else if (maal < m) {
      i = mid + 1;
    } else {
      j = mid - 1;
    }
  }

  return -1;

}