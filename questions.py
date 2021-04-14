"""
Question types to ask users.
"""
import numpy as np

def ask_binary_qx(qx):
    ans = ""
    while not ((ans == "a") | (ans == "b")):
        ans = input(qx)
        if ans == "a":
            pass
        elif ans == "b":
            pass
        else:
            print("Please enter either a or b")
    return ans

# evaluate results
def gen_sharpe(returns, rfr=0, freq=252):
    """
    returns is a vector of returns of consistent periodicity
     rfr is the stated annual risk-free rate OR it can be a
      vector of stated annual risk-free rates of equivalent
      size as that of returns
     freq is the frequency of returns periodicity per year
      eg. freq is 252 if returns are daily (even if the length
      of returns is much less or greater), freq is 12 for
      monthly returns, and freq is 1 for yearly returns
    """
    k = np.sqrt(freq)
    rfr_period = (1 + rfr)**(1 / freq) - 1
    ret = float(np.mean(returns.values - rfr_period))
    std = np.std(returns.values)
    if (std == 0):
        if (ret > 0):
            sharpe = np.inf
        elif (ret == 0):
            sharpe = 0
        elif (ret < 0):
            sharpe = -np.inf
    else:
        sharpe = k * (ret / std)

    return sharpe
