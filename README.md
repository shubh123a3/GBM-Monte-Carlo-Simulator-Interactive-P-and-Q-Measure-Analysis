# GBM Monte Carlo Simulator: Interactive P and Q Measure Analysis

## Overview


https://github.com/user-attachments/assets/d5bcd800-a5e1-465e-a594-b1b459cb9788


This project provides an interactive Streamlit application for simulating and visualizing Geometric Brownian Motion (GBM) under both the risk-neutral (Q) and real-world (P) measures. It's a powerful tool for understanding and exploring key concepts in financial modeling and option pricing.

## Features

- Monte Carlo simulation of stock price paths using GBM
- Comparison of Q-measure (risk-neutral) and P-measure (real-world) simulations
- Interactive parameter adjustment via Streamlit sidebar
- Real-time visualization of simulation results
- Educational descriptions of input parameters

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/gbm-monte-carlo-simulator.git
   cd gbm-monte-carlo-simulator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
# GBM Monte Carlo Simulator: Interactive P and Q Measure Analysis

## Overview

This project provides an interactive Streamlit application for simulating and visualizing Geometric Brownian Motion (GBM) under both the risk-neutral (Q) and real-world (P) measures. It's a powerful tool for understanding and exploring key concepts in financial modeling and option pricing.

## Features

- Monte Carlo simulation of stock price paths using GBM
- Comparison of Q-measure (risk-neutral) and P-measure (real-world) simulations
- Interactive parameter adjustment via Streamlit sidebar
- Real-time visualization of simulation results
- Educational descriptions of input parameters

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/gbm-monte-carlo-simulator.git
   cd gbm-monte-carlo-simulator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```


This will open the application in your default web browser. Use the sidebar to adjust simulation parameters and click "Run Simulation" to generate new results.

## Parameters

- **Number of Paths**: The number of simulated stock price paths.
- **Number of Steps**: The number of time steps in each path.
- **Initial Stock Price (S_0)**: The starting price of the stock.
- **Risk-free Rate (r)**: The risk-free interest rate used in the Q-measure simulation.
- **Drift (mu)**: The expected return of the stock used in the P-measure simulation.
- **Volatility (sigma)**: The standard deviation of the stock's returns.
- **Time Horizon (T)**: The total time period for the simulation in years.

## Theory

The application simulates Geometric Brownian Motion under two measures:

1. **Q-measure (Risk-Neutral)**: 
   $dS_t = rS_t dt + \sigma S_t dW_t^Q$

2. **P-measure (Real-World)**:
   $dS_t = \mu S_t dt + \sigma S_t dW_t^P$

Where:
- $S_t$ is the stock price at time $t$
- $r$ is the risk-free rate
- $\mu$ is the drift (expected return)
- $\sigma$ is the volatility
- $W_t^Q$ and $W_t^P$ are Wiener processes under Q and P measures respectively

## Contributing

Contributions to improve the application or extend its functionality are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original code concept by Lech A. Grzelak
- Streamlit for providing an excellent framework for interactive Python applications

## Contact

For any queries or discussions related to this project, please open an issue in the GitHub repository.
