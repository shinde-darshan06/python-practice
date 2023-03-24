# Question 1

# Write a sql query which will return box id with 3 consecutive empty boxes

# solution 1:

select box_id, is_empty_box from (
select box_id, is_empty_box,
lag(is_empty_box, 1) over(order by rowid) as prev_1,
lag(is_empty_box, 2) over(order by rowid) as prev_2,
lead(is_empty_box, 1) over(order by rowid) as next_1,
lead(is_empty_box, 2) over(order by rowid) as next_2
from box)
where is_empty_box='Yes' and prev_1='Yes' and prev_2='Yes'
or (is_empty_box='Yes' and prev_1='Yes' and next_1='Yes')
or (is_empty_box='Yes' and next_1='Yes' and next_2='Yes');

# solution 1:
with cte as(
select box_id, is_empty_box,
((row_number() over(order by rowid)) - (row_number() over(partition by is_empty_box order by rowid))) as diff
from box),
cte2 as
(select box_id, is_empty_box,
 count(diff) over(partition by diff) cnt
 from cte)
select box_id
from cte2
where cnt>=3 and is_empty_box='Yes';

# ---------------------------------------------------------------------------------------------------
#Question 2

# Write a pysaprk code which will create below dataframes
'''
three_consecutive_df - box id with 3 consecutive empty boxes
four_consecutive_df - box id with 4 consecutive empty boxes
two_consecutive_df - box id with 2 consecutive empty boxes
'''
# Q.2.1 three_consecutive_df - box id with 3 consecutive empty boxes

win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'))

df_box.withColumn('RN', monotonically_increasing_id() + 1)\
    .withColumn('RN1', row_number().over(win1))\
    .withColumn('diff',col('RN')-col('RN1'))\
    .withColumn('cnt',count('diff').over(win2))\
    .filter((col('cnt')>=3) & (col('is_empty_box').isin('Yes')))\
    .select(col('box_id'))\
    .show()

# Q.2.2 four_consecutive_df - box id with 4 consecutive empty boxes

win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'))

df_box.withColumn('RN', monotonically_increasing_id() + 1)\
    .withColumn('RN1', row_number().over(win1))\
    .withColumn('diff',col('RN')-col('RN1'))\
    .withColumn('cnt',count('diff').over(win2))\
    .filter((col('cnt')>=4) & (col('is_empty_box').isin('Yes')))\
    .select(col('box_id'))\
    .show()