import pandas as pd
import numpy as np
import math
from scipy.stats import mannwhitneyu

chat_id = 1004085803 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    stats, pvalue = mannwhitneyu(x, y)
    if pvalue > alpha:
      return False
    else:
      return True
