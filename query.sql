
--Request First
SELECT game_genre.genre, COUNT(game_genre.genre) AS Number_Of_Games FROM game 
LEFT JOIN game_genre ON game.game_id = game_genre.game_id 
GROUP BY genre;

-- Request Second
SELECT developer.name AS Develop_Name, publisher.name AS Publisher_Name, game.sales, game.name AS Game_Name FROM game 
CROSS JOIN (developer CROSS JOIN publisher) 
WHERE developer.developer_id = publisher.publisher_id 
AND game.game_id = developer.developer_id
AND game.sales >= 20;

--Requesst Third
SELECT game.name AS Game_Name, game.sales, game.series, game.release, game_genre.genre, developer.name AS Developer_Name, publisher.name AS Publisher_Name FROM 
(game CROSS JOIN game_genre) 
CROSS JOIN 
(developer CROSS JOIN publisher) 
WHERE game.game_id = game_genre.game_id 
AND developer.developer_id = publisher.publisher_id 
AND game.game_id = developer.developer_id 
ORDER BY game.sales ASC;

