SELECT w2.id 
FROM Weather AS w1, Weather AS w2 
WHERE  w1.recordDate + INTERVAL '1 day' = w2.recordDate
AND w1.temperature < w2.temperature;