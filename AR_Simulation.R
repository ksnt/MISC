# Simulation of AR model
set.seed(2016);
N=1000;
X=NULL;
phi = .2;
Z = rnorm(N,0,1);
X[1] = Z[1];
for (t in 2:N) {
  X[t] = Z[t] + phi*X[t-1] ;
}
X.ts = ts(X)
par(mfrow=c(2,1))
plot(X.ts,main="AR(1) Time Series on White Noise, phi=.2")
X.acf = acf(X.ts, main="AR(1) Time Series on White Noise, phi=.2")