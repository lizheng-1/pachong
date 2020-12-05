import pandas as pd
dic1 = {'标题列1': ['张三','李四'],
        '标题列2': [80, 90]
        }
df = pd.DataFrame(dic1)

df.to_excel('1.xls', index=False)