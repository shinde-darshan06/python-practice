--Create table query

create table box (box_id int ,is_empty_box varchar(10));

--Insert Query

Table Name - box
insert into box values
(17333,'Yes')
,(2354,'No')
,(5732,'Yes')
,(11320,'No')
,(16036,'No')
,(12838,'No')
,(12356,'Yes')
,(17405,'Yes')
,(19180,'Yes')
,(4783,'Yes')
,(9261,'No')
,(1567,'Yes')
,(7633,'No')
,(8829,'No')
,(3254,'No')
,(14681,'Yes')
,(17704,'Yes')
,(6877,'Yes')
,(2385,'No')
,(17886,'No')

--Question 1

-- Write a sql query which will return box id with 3 consecutive empty boxes

----------------------------------------------------------------------------------------
--Question 2

-- Write a pysaprk code which will create below dataframes

three_consecutive_df - box id with 3 consecutive empty boxes
four_consecutive_df - box id with 4 consecutive empty boxes
two_consecutive_df - box id with 2 consecutive empty boxes

------------------------------------------------------------------------------------------

--Question 3

Table Name -> box_dim

box_id	height	width	length
17333	4	10	2
2354	2	6	5
5732	2	3	6
11320	5	5	8
16036	4	10	3
12838	4	4	1
12356	10	2	7
17405	7	6	6
19180	8	5	5
4783	2	1	3
9261	6	8	8
1567	4	2	4
7633	6	4	9
8829	7	1	5
3254	5	6	7
14681	4	4	2
17704	8	4	8
6877	9	3	4
2385	1	8	6
17886	7	7	10

Note -> Write SQL and Pysaprk code for below

3.1  Calculate volume of boxes which are empty

3.2  calculate volume for 3 consecutive empty boxes , 2 consecutive empty boxes , 4 consecutive empty boxes

---------------------------------------------------------------------------------------------
Question 4

item

item_id	box_id	Volume
1575	17333	610
1208	19180	34
1656	17886	330
1132	11320	62
1841	16036	200
1284	12838	330
1530	16036	134
1739	17405	230
1740	19180	59
1673	4783	540
1146	9261	220
1095	17333	130
1742	7633	240
1576	17886	123
1692	3254	44
1722	16036	5700
1600	17704	13
1192	6877	550
1314	16036	42
1442	17886	350

Note -> Write SQL and Pysaprk code for below

4.1 Calculate number of itmes that will overflow
4.2 Add column which will indicate that  is allocation is correct or not .( is yes add Y else N)
 -> If  --> box volume  < ( volume of all boxes) it tells us allocation is not correct
4.3 Rellocate items to boxes
4.4 How do you handle outliers?

--------------------------------------------------------------------------------------------------
Question 5

Here some stats about number of rows in each table

Case 1 :

box - 10000
box_dim - 10000
item - 1400000

Which spark join you will use here
5.1 Rewrite your solution to question 4.1 considering above data

Case 2:

box - 10000000
box_dim - 10000000
item - 1400000

Which spark join you will use here
5.1 Rewrite your solution to question 4.1 considering above data
5.2 How can denormlise these three tables , share schema here with reasoning ? Is it really required ?
5.3 Rewrite 3 and 4 the question after denormlisation ? Will it improve performace ?

--------------------------------------------------------------------------------------------------
Question 6

As per business need data you created after allocation in 4.3 we need to colour code it with below rules

occpied_percent < 50 --> Green
50 > occpied_percent < 75 --> Yellow
occpied_percent > 75  --> RED

Write pysaprk code and sql query to do the colour coding

--------------------------------------------------------------------------------------------------------
Question 7:
7.1  Every day there are new items are getting added in catlog , so its degrading the performace of above
queries,can you suggest few ways to improve performace
7.2 What should be partition column all the three tables in question , support your  answer with reasoning
-----------------------------------------------------------------------------------------------------------

