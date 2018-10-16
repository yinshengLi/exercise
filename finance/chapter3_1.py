#__author:iruyi
#date:2018/10/10

#Analytical Black-Scholes-Merton(BSM) Formula

def bsm_call_value(S0, K, T, r, sigma):
    '''
    Valuation of European call option in BSM model.
    Analytical formula
    :param S0: float
    initial stock/index level
    :param K:  float
    strike price
    :param T:
    maturity date
    :param r:
    constant risk-free short rate
    :param sigma:
    volatility factor in diffusion term
    :return: float
    present value of the European call option
    '''
    from math import log, sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 =(log(S0/K) + (r + 0.5 * sigma**2) * T)/(sigma * sqrt(T))
    d2 =(log(S0/K) + (r - 0.5 * sigma**2) * T)/(sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) -
             K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))

    return value