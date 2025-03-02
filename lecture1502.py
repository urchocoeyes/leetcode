# 1
# https://platform.stratascratch.com/coding/2070-top-three-classes?code_type=1

import pandas as pd

df = online_orders.merge(online_products, on='product_id')

sales = df.groupby('product_class').size().to_frame('sales').reset_index()

sales['rank'] = sales.sales.rank(method='min', ascending=False)

result_df = sales[sales['rank'] <= 3][['product_class']]

result_df