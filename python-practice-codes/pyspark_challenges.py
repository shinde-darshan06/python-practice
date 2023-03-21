'''
+------+--------------+---------------+
| id   | name         | activity      |
+------+--------------+---------------+
| 1    | Jonathan D.  | Eating        |
| 2    | Jade W.      | Singing       |
| 3    | Victor J.    | Singing       |
| 4    | Elvis Q.     | Eating        |
| 5    | Daniel A.    | Eating        |
| 6    | Bob B.       | Horse Riding  |
+------+--------------+---------------+

'''


max_count = df.groupBy("activity").agg(count(col("activity")).alias("act_count"))\
    .agg({"act_count": "max"}).collect()[0]["max(act_count)"]

min_count = df.groupBy("activity").agg(count(col("activity")).alias("act_count"))\
    .agg({"act_count": "min"}).collect()[0]["min(act_count)"]

res = df.groupBy("activity").agg(count(col("activity")).alias("act_count"))\
    .where((col("act_count") != max_count) & (col("act_count") != min_count))

res.show()
