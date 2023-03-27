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
with cte as (
select box_id, is_empty_box,
(row_number() over(order by rowid) - (row_number() over(partition by is_empty_box order by rowid))) as diff
from box),
cte2 as(
select box_id, is_empty_box,
count(diff) over(partition by diff) as cnt
from cte
)
select box_id, is_empty_box from cte2
where cnt=3 and is_empty_box='Yes';

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
    .filter((col('cnt')==3) & (col('is_empty_box').isin('Yes')))\
    .select(col('box_id'))\
    .show()

# Q.2.2 four_consecutive_df - box id with 4 consecutive empty boxes

win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'))

df_box.withColumn('RN', monotonically_increasing_id() + 1)\
    .withColumn('RN1', row_number().over(win1))\
    .withColumn('diff',col('RN')-col('RN1'))\
    .withColumn('cnt',count('diff').over(win2))\
    .filter((col('cnt')==4) & (col('is_empty_box').isin('Yes')))\
    .select(col('box_id'))\
    .show()

# Q.2.3 two_consecutive_df - box id with 2 consecutive empty boxes

win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'),col("is_empty_box"))

df_box.withColumn('RN', monotonically_increasing_id() + 1)\
    .withColumn('RN1', row_number().over(win1))\
    .withColumn('diff',col('RN')-col('RN1'))\
    .withColumn('cnt',count('diff').over(win2))\
    .filter((col('cnt')==2) & (col('is_empty_box').isin('Yes')))\
    .select(col('box_id'))\
    .show()

# ----------------------------------------------------------------------------------------------------

# -- 3.1  Calculate volume of boxes which are empty

# method 1:-using sql
with cte as(
select b.box_id, b.is_empty_box, d.height, d.width, d.length
from box b
inner join box_dim d
on b.box_id=d.box_id
where b.is_empty_box='Yes')
select box_id, (height*width*length) as vol
from cte;

# method 2: using pyspark

df_box.join(df_box_dim, df_box.box_id == df_box_dim.box_id, "inner")\
  .where(col('is_empty_box') == 'Yes')\
  .select(df_box.box_id, (col('height')*col('width')*col('length')).alias('volume'))\
  .show()

# -- 3.2 calculate volume for 3 consecutive empty boxes

# using SQL

with cte as(
SELECT box_id, is_empty_box,
(row_number() over(order by rowid) -(row_number() over(partition by is_empty_box order by rowid))) diff
from box
),
cte2 as(
select box_id, is_empty_box,
count(diff) over(partition by diff) cnt
from cte
), cte3 as (
select box_id
from cte2
where cnt=3 and is_empty_box='Yes')
select b.box_id, (d.height*d.width*d.length) as vol
from cte3 b
inner join box_dim d
on b.box_id=d.box_id;

# using PySpark:
win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'),col("is_empty_box"))

three_consecutive_df = df_box.withColumn('RN', monotonically_increasing_id() + 1)\
                    .withColumn('RN1', row_number().over(win1))\
                    .withColumn('diff',col('RN')-col('RN1'))\
                    .withColumn('cnt',count('diff').over(win2))\
                    .filter((col('cnt')==3) & (col('is_empty_box').isin('Yes')))\
                    .select(col('box_id'))

empty_box_vol_df = df_box.join(df_box_dim, df_box.box_id == df_box_dim.box_id, "inner")\
                         .where(col('is_empty_box') == 'Yes')\
                         .select(df_box.box_id, (col('height')*col('width')*col('length')).alias('volume'))

vol_three_consecutive_df= three_consecutive_df.join(empty_box_vol_df\
                            ,three_consecutive_df.box_id==empty_box_vol_df.box_id,'inner')\
                        .select(three_consecutive_df.box_id,empty_box_vol_df.volume).show()

# -- 3.2 calculate volume for  2 consecutive empty boxes.

# using SQL

with cte as(
SELECT box_id, is_empty_box,
(row_number() over(order by rowid) -(row_number() over(partition by is_empty_box order by rowid))) diff
from box
),
cte2 as(
select box_id, is_empty_box,
count(diff) over(partition by diff, is_empty_box) cnt
from cte
), cte3 as (
select box_id
from cte2
where cnt=2 and is_empty_box='Yes')
select b.box_id, (d.height*d.width*d.length) as vol
from cte3 b
inner join box_dim d
on b.box_id=d.box_id;

# using PySpark

win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'),col("is_empty_box"))

three_consecutive_df = df_box.withColumn('RN', monotonically_increasing_id() + 1)\
                    .withColumn('RN1', row_number().over(win1))\
                    .withColumn('diff',col('RN')-col('RN1'))\
                    .withColumn('cnt',count('diff').over(win2))\
                    .filter((col('cnt')==2) & (col('is_empty_box').isin('Yes')))\
                    .select(col('box_id'))

empty_box_vol_df = df_box.join(df_box_dim, df_box.box_id == df_box_dim.box_id, "inner")\
                         .where(col('is_empty_box') == 'Yes')\
                         .select(df_box.box_id, (col('height')*col('width')*col('length')).alias('volume'))

vol_three_consecutive_df= three_consecutive_df.join(empty_box_vol_df\
                            ,three_consecutive_df.box_id==empty_box_vol_df.box_id,'inner')\
                        .select(three_consecutive_df.box_id,empty_box_vol_df.volume).show()

# -- 3.2  calculate volume for 4 consecutive empty boxes

# using SQL
with cte as(
SELECT box_id, is_empty_box,
(row_number() over(order by rowid) -(row_number() over(partition by is_empty_box order by rowid))) diff
from box
),
cte2 as(
select box_id, is_empty_box,
count(diff) over(partition by diff, is_empty_box) cnt
from cte
), cte3 as (
select box_id
from cte2
where cnt=4 and is_empty_box='Yes')
select b.box_id, (d.height*d.width*d.length) as vol
from cte3 b
inner join box_dim d
on b.box_id=d.box_id;

# using pyspark:
win1 = Window.partitionBy('is_empty_box').orderBy('RN')
win2 = Window.partitionBy(col('diff'),col("is_empty_box"))

three_consecutive_df = df_box.withColumn('RN', monotonically_increasing_id() + 1)\
                    .withColumn('RN1', row_number().over(win1))\
                    .withColumn('diff',col('RN')-col('RN1'))\
                    .withColumn('cnt',count('diff').over(win2))\
                    .filter((col('cnt')==4) & (col('is_empty_box').isin('Yes')))\
                    .select(col('box_id'))

empty_box_vol_df = df_box.join(df_box_dim, df_box.box_id == df_box_dim.box_id, "inner")\
                         .where(col('is_empty_box') == 'Yes')\
                         .select(df_box.box_id, (col('height')*col('width')*col('length')).alias('volume'))

vol_three_consecutive_df= three_consecutive_df.join(empty_box_vol_df\
                            ,three_consecutive_df.box_id==empty_box_vol_df.box_id,'inner')\
                        .select(three_consecutive_df.box_id,empty_box_vol_df.volume).show()