# https://leetcode.com/problems/rank-scores/
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # score: ascending = False 
    # 1 -> 3, 2 -> 3 = > two ids should be displayed
    # 1 -> 3, 2 -> 3,    no gap   , 4 -> 2
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    result = scores.sort_values(by=['score', 'rank'], 
                                ascending=False)
    return result[['score', 'rank']]
    