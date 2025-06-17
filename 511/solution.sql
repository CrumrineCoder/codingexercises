
-- First Try
SELECT a1.player_id, a1.event_date AS first_login
FROM Activity as a1, Activity as a2
WHERE a1.player_id = a2.player_id AND a1.event_date < a2.event_date

-- Second Try
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;