# Write your MySQL query statement below
Select name
From Customer
Where IFNULL(referee_id,0) <> 2

# referee_id != 2 OR referee_id is NULL
# COALESCE(referee_id, 0) <> 2