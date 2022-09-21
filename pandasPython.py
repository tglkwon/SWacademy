import pandas as pd
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')
tips.iloc[0,0]
tips['size']
tips[['size', 'sex']]

# np.s_[2::2] # slice의 단축표현을 만들어준다
