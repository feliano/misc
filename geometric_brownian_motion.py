import numpy as np
import matplotlib.pyplot as plt


S0 = 25 # initial share price
mu = 0.1 # "percentage drift"
sigma = 0.1 # percentage volatility
N = 100;
dt = 1.0/N;
t = np.linspace(0,1.0,N)

def geometric_bm():
	dW = []
	W = [];
	dW.append(np.sqrt(dt) * np.random.randn());
	W.append(dW[0]); 
	for i in range(1,N):
		dW.append(np.sqrt(dt) * np.random.randn());
		W.append(W[i-1] + dW[i]); # Standard brownian motion / wiener process

	S = S0*np.exp((mu-0.5*sigma**2)*t + (sigma*np.array(W))) # geometric brownian motion
	plt.plot(t,S)

if __name__ == "__main__":
	fig = plt.figure(0)
	fig.canvas.set_window_title('Geometric Brownian Motion')
	plt.title("S0=%d mu=%.2f sigma=%.2f" % (S0,mu,sigma));
	plt.axis([0,1,20,35])
	number_of_paths = 10;
	for i in range(0,number_of_paths):
		geometric_bm();
	plt.show()


