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

"""
WITH cte AS (
  SELECT activity, COUNT(activity) AS act_count
  FROM activity
  GROUP BY activity
)
SELECT activity
FROM cte
WHERE act_count NOT IN (
  SELECT MAX(act_count) FROM cte
  UNION
  SELECT MIN(act_count) FROM cte
);"""
