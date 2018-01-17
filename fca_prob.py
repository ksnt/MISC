// FCA Coursera Week6 Quiz1
// ksnt

from scipy.special import comb
n=10
p_b = 0.09
p_not_b = 0.7

result = []

for k in range(0,10):
    result.append(comb(n,k) * (p_b ** k) * (1 - p_b) ** (n-k) * (1 - p_not_b ** k) )

return(sum(result))
