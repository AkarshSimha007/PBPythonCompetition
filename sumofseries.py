def seriessum(terms):
  return sum([i*(i+1)/2 for i in range(1, n + 1)]);
terms=int(input())
print(seriessum(terms))