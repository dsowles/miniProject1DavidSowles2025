# INF601 - Advanced Programming in Python
# Project:          MiniProject1

# Filename:         miniProject1DavidSowles2025.py
# Author:           David A. Sowles
# Creation Date:    09/14/2025
# Last Updated:     09/14/2025

'''
INF601 - Programming in Python
Assignment miniProject1

I,     David Sowles    , affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. 
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. 
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined 
by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''


NVIDIA_TICKER_SYM = "NVDA"
INTEL_TICKER_SYM = "INTC"
AMD_TICKER_SYM = "AMD"
MS_TICKER_SYM = "MSFT"
GOOGLE_TICKER_SYM = "GOOG"


import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import os

#Make directory for charts
os.makedirs("charts", exist_ok=True)

def main():

    days = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

    # Obtain ticker objects for the five stocks.
    nvidiaTicker = yf.Ticker(NVIDIA_TICKER_SYM)
    intelTicker = yf.Ticker(INTEL_TICKER_SYM)
    amdTicker = yf.Ticker(AMD_TICKER_SYM)
    msTicker = yf.Ticker(MS_TICKER_SYM)
    googTicker = yf.Ticker(GOOGLE_TICKER_SYM)\

    # Obtain the stock history
    nvidiaHist = nvidiaTicker.history(period="10d")
    intelHist = intelTicker.history(period="10d")
    amdHist = amdTicker.history(period="10d")
    msHist = msTicker.history(period="10d")
    googHist = googTicker.history(period="10d")
    

    # Obtain plot data for nvidia
    plotData = np.array([d for d in nvidiaHist["Close"]])

    # Setup plot for nvidia stock
    plt.title(NVIDIA_TICKER_SYM + " - Last 10 Days")
    plt.ylabel("Price")
    plt.xlabel("Days Ago")
    plt.plot(days, plotData)
    plt.show()
    plt.savefig("charts/" + NVIDIA_TICKER_SYM + ".png")

    # Obtain plot data for nvidia
    plotData = np.array([d for d in intelHist["Close"]])

    # Setup plot for nvidia stock
    plt.title(INTEL_TICKER_SYM + " - Last 10 Days")
    plt.ylabel("Price")
    plt.xlabel("Days Ago")
    plt.plot(days, plotData)
    plt.show()
    plt.savefig("charts/" + INTEL_TICKER_SYM + ".png")

    # Obtain plot data for nvidia
    plotData = np.array([d for d in amdHist["Close"]])

    # Setup plot for nvidia stock
    plt.title(AMD_TICKER_SYM + " - Last 10 Days")
    plt.ylabel("Price")
    plt.xlabel("Days Ago")
    plt.plot(days, plotData)
    plt.show()
    plt.savefig("charts/" + AMD_TICKER_SYM + ".png")

    # Obtain plot data for nvidia
    plotData = np.array([d for d in msHist["Close"]])

    # Setup plot for nvidia stock
    plt.title(MS_TICKER_SYM + " - Last 10 Days")
    plt.ylabel("Price")
    plt.xlabel("Days Ago")
    plt.plot(days, plotData)
    plt.show()
    plt.savefig("charts/" + MS_TICKER_SYM + ".png")

    # Obtain plot data for nvidia
    plotData = np.array([d for d in googHist["Close"]])

    # Setup plot for nvidia stock
    plt.title(GOOGLE_TICKER_SYM + " - Last 10 Days")
    plt.ylabel("Price")
    plt.xlabel("Days Ago")
    plt.plot(days, plotData)
    plt.show()
    plt.savefig("charts/" + GOOGLE_TICKER_SYM + ".png")

main()