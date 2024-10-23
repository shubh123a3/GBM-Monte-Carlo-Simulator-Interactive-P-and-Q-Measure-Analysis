import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def GeneratePathsGBM(NoOfPaths, NoOfSteps, T, r, sigma, S_0):
    Z = np.random.normal(0.0, 1.0, [NoOfPaths, NoOfSteps])
    X = np.zeros([NoOfPaths, NoOfSteps + 1])
    S = np.zeros([NoOfPaths, NoOfSteps + 1])
    time = np.zeros([NoOfSteps + 1])

    X[:, 0] = np.log(S_0)

    dt = T / float(NoOfSteps)
    for i in range(0, NoOfSteps):
        if NoOfPaths > 1:
            Z[:, i] = (Z[:, i] - np.mean(Z[:, i])) / np.std(Z[:, i])

        X[:, i + 1] = X[:, i] + (r - 0.5 * sigma * sigma) * dt + sigma * np.power(dt, 0.5) * Z[:, i]
        time[i + 1] = time[i] + dt

    S = np.exp(X)
    paths = {"time": time, "S": S}
    return paths


def MainCode(NoOfPaths, NoOfSteps, S_0, r, mu, sigma, T):
    M = lambda t: np.exp(r * t)

    pathsQ = GeneratePathsGBM(NoOfPaths, NoOfSteps, T, r, sigma, S_0)
    S_Q = pathsQ["S"]
    pathsP = GeneratePathsGBM(NoOfPaths, NoOfSteps, T, mu, sigma, S_0)
    S_P = pathsP["S"]
    time = pathsQ["time"]

    S_Qdisc = np.zeros([NoOfPaths, NoOfSteps + 1])
    S_Pdisc = np.zeros([NoOfPaths, NoOfSteps + 1])
    for i, ti in enumerate(time):
        S_Qdisc[:, i] = S_Q[:, i] / M(ti)
        S_Pdisc[:, i] = S_P[:, i] / M(ti)

    fig1, ax1 = plt.subplots(figsize=(16, 5))
    ax1.set_title('Monte Carlo Simulation of Geometric Brownian Motion under Q Measure')
    ax1.grid()
    ax1.set_xlabel("time")
    ax1.set_ylabel("S(t)")
    eSM_Q = lambda t: S_0 * np.exp(r * t) / M(t)
    ax1.plot(time, eSM_Q(time), 'r--')
    ax1.plot(time, np.transpose(S_Qdisc), 'blue')
    ax1.legend(['E^Q[S(t)/M(t)]', 'paths S(t)/M(t)'])

    fig2, ax2 = plt.subplots(figsize=(16, 5))
    ax2.set_title('Monte Carlo Simulation of Geometric Brownian Motion under P Measure')
    ax2.grid()
    ax2.set_xlabel("time")
    ax2.set_ylabel("S(t)")
    eSM_P = lambda t: S_0 * np.exp(mu * t) / M(t)
    ax2.plot(time, eSM_P(time), 'r--')
    ax2.plot(time, np.transpose(S_Pdisc), 'blue')
    ax2.legend(['E^P[S(t)/M(t)]', 'paths S(t)/M(t)'])

    return fig1, fig2


st.title('Monte Carlo Simulation of Geometric Brownian Motion')

st.sidebar.header('Input Parameters')
NoOfPaths = st.sidebar.slider('Number of Paths', 1, 50, 8)
NoOfSteps = st.sidebar.slider('Number of Steps', 100, 2000, 1000)
S_0 = st.sidebar.number_input('Initial Stock Price (S_0)', 0.1, 100.0, 1.0, 0.1)
r = st.sidebar.slider('Risk-free Rate (r)', 0.0, 0.2, 0.05, 0.01)
mu = st.sidebar.slider('Drift (mu)', 0.0, 0.3, 0.15, 0.01)
sigma = st.sidebar.slider('Volatility (sigma)', 0.01, 0.5, 0.1, 0.01)
T = st.sidebar.slider('Time Horizon (T)', 1, 20, 10)

if st.sidebar.button('Run Simulation'):
    fig1, fig2 = MainCode(NoOfPaths, NoOfSteps, S_0, r, mu, sigma, T)
    st.pyplot(fig1)
    st.pyplot(fig2)

st.sidebar.markdown("""
## Parameter Descriptions:
- **Number of Paths**: The number of simulated price paths.
- **Number of Steps**: The number of time steps in each path.
- **Initial Stock Price (S_0)**: The starting price of the stock.
- **Risk-free Rate (r)**: The risk-free interest rate.
- **Drift (mu)**: The expected return of the stock under the real-world measure.
- **Volatility (sigma)**: The standard deviation of the stock's returns.
- **Time Horizon (T)**: The total time period for the simulation in years.
""")