import psycopg2

username = 'HRYHORENKO_VALERII'
password = '111'
database = 'db_lab3_game'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT game_genre.genre, COUNT(game_genre.genre) AS Number_Of_Games FROM game 
LEFT JOIN game_genre ON game.game_id = game_genre.game_id 
GROUP BY genre;
'''

query_2 = '''
SELECT developer.name AS Develop_Name, publisher.name AS Publisher_Name, game.sales, game.name AS Game_Name FROM game 
CROSS JOIN (developer CROSS JOIN publisher) 
WHERE developer.developer_id = publisher.publisher_id 
AND game.game_id = developer.developer_id
AND game.sales >= 20;
'''

query_3 = '''
SELECT game.name AS Game_Name, game.sales, game.series, game.release, game_genre.genre, developer.name AS Developer_Name, publisher.name AS Publisher_Name FROM 
(game CROSS JOIN game_genre) 
CROSS JOIN 
(developer CROSS JOIN publisher) 
WHERE game.game_id = game_genre.game_id 
AND developer.developer_id = publisher.publisher_id 
AND game.game_id = developer.developer_id 
ORDER BY game.sales ASC;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
                       
    print ("Database opened successfully")
    
    cur1 = conn.cursor()     #take method cursor from conn to print one by one strings
    cur1.execute(query_1)

    cur2 = conn.cursor()    
    cur2.execute(query_2)

    cur3 = conn.cursor()     
    cur3.execute(query_3)        

    print('-' * 7 + '1' + '-' * 7)
    for row in cur1.fetchmany(size=20):
        print(row)    
    print()

    print('-' * 7 + '2' + '-' * 7)
    for row in cur2.fetchmany(size=20):
        print(row)    
    print()        

    print('-' * 7 + '3' + '-' * 7)
    for row in cur3.fetchmany(size=20):
        print(row)    
    print()