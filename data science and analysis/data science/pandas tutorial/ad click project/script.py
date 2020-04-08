import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

views_1 = ad_clicks.groupby('utm_source').user_id.nunique().reset_index()
print(views_1)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns = "is_click",
  index = "utm_source",
  values = "user_id"
).reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[False] + clicks_pivot[True])

print(clicks_pivot)

ads = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ads)


clicks_by_ad = ad_clicks.groupby(['is_click','experimental_group']).user_id.count().reset_index()
print(clicks_by_ad)

ads_pivot = clicks_by_ad.pivot(
  columns = "is_click",
  index = "experimental_group",
  values = "user_id"
).reset_index()
print(ads_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
print(type(a_clicks))

a_clicks = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(a_clicks)

a_clicks_pivoted = a_clicks.pivot(
    columns = 'is_click',
    index ='day',
    values = 'user_id').reset_index()

a_clicks_pivoted['daily click %'] = a_clicks_pivoted[True] / (a_clicks_pivoted[True] + a_clicks_pivoted[False])
print(a_clicks_pivoted)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()

b_clicks = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(b_clicks)

b_clicks_pivoted = b_clicks.pivot(
    columns = 'is_click',
    index ='day',
    values = 'user_id').reset_index()

b_clicks_pivoted['daily click %'] = b_clicks_pivoted[True] / (b_clicks_pivoted[True] + b_clicks_pivoted[False])
print(b_clicks_pivoted)


