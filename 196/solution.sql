DELETE FROM Person p1
USING (
    SELECT Email, MIN(ID) AS MinID
    FROM Person
    GROUP BY Email
) p2
WHERE p1.Email = p2.Email 
AND p1.ID > p2.MinID;

-- Better solution by community
DELETE p from Person p, Person q where p.Id>q.Id AND q.Email=p.Email 