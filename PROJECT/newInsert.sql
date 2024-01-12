-- Insert data into Court table
INSERT INTO Court VALUES
    (1, 'Court A', 500, 'Location A'),
    (2, 'Court B', 450, 'Location B');

-- Insert data into Championship table
INSERT INTO Championship VALUES
    (1, 'Championship 2024', '2024-01-01', '2024-02-01', 'Description');

-- Insert data into Team table
INSERT INTO Team VALUES
    (1, 'Team 1', '2020-01-01', 'Coach 1', 'Coach Last 1', 1, 1),
    (2, 'Team 2', '2020-02-01', 'Coach 2', 'Coach Last 2', 2, 1),
    (3, 'Team 3', '2020-03-01', 'Coach 3', 'Coach Last 3', 1, 1),
    (4, 'Team 4', '2020-04-01', 'Coach 4', 'Coach Last 4', 2, 1),
    (5, 'Team 5', '2020-05-01', 'Coach 5', 'Coach Last 5', 1, 1),
    (6, 'Team 6', '2020-06-01', 'Coach 6', 'Coach Last 6', 2, 1),
    (7, 'Team 7', '2020-07-01', 'Coach 7', 'Coach Last 7', 1, 1),
    (8, 'Team 8', '2020-08-01', 'Coach 8', 'Coach Last 8', 2, 1);

-- Insert data into Match table (Group Phase)
INSERT INTO Match VALUES
    (1, '2024-01-10', '08:00:00', 1, 'Group A'),
    (2, '2024-01-10', '10:00:00', 1, 'Group A'),

    (3, '2024-01-10', '12:00:00', 1, 'Group A'),
    (4, '2024-01-10', '14:00:00', 1, 'Group A'),
    
    (5, '2024-01-10', '16:00:00', 1, 'Group A'),
    (6, '2024-01-10', '18:00:00', 1, 'Group A'),

    (7, '2024-01-11', '08:00:00', 1, 'Group A'),
    (8, '2024-01-11', '10:00:00', 1, 'Group A'),
    
    (9, '2024-01-11', '12:00:00', 1, 'Group A'),
    (10, '2024-01-11', '14:00:00', 1, 'Group A'),
    
    (11, '2024-01-11', '16:00:00', 1, 'Group A'),
    (12, '2024-01-11', '18:00:00', 1, 'Group A'),

    (13, '2024-01-10', '08:00:00', 2, 'Group B'),
    (14, '2024-01-10', '10:00:00', 2, 'Group B'),

    (15, '2024-01-10', '12:00:00', 2, 'Group B'),
    (16, '2024-01-10', '14:00:00', 2, 'Group B'),

    (17, '2024-01-10', '16:00:00', 2, 'Group B'),
    (18, '2024-01-10', '18:00:00', 2, 'Group B'),

    (19, '2024-01-11', '08:00:00', 2, 'Group B'),
    (20, '2024-01-11', '10:00:00', 2, 'Group B'),

    (21, '2024-01-11', '12:00:00', 2, 'Group B'),
    (22, '2024-01-11', '14:00:00', 2, 'Group B'),

    (23, '2024-01-11', '16:00:00', 2, 'Group B'),
    (24, '2024-01-11', '18:00:00', 2, 'Group B');

-- Create two more matches in the knockout phase
-- Knockouts 4
INSERT INTO Match VALUES
    (25, '2024-02-01', '14:00:00', 1, 'Knockouts 4'),
    (26, '2024-02-01', '18:00:00', 2, 'Knockouts 4');

-- Knockouts 2
INSERT INTO Match VALUES
    (27, '2024-02-10', '15:00:00', 1, 'Knockouts 2');

-- Insert data into Includes table (Group Phase)
INSERT INTO Includes VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (1, 11);

-- Insert data into Player table
-- (You need to insert players for each team)

-- Insert data into PlayerStats table
-- (You need to insert stats for each player in each match)

-- Insert data into Position table
-- (You need to insert player positions)

-- After determining the top two teams from each group based on goals scored,
-- you can proceed to the Knockouts phase and update the Match table accordingly.
-- (The same applies to Includes table and other relevant tables.)

-- Insert data into Player table for Team 1A
INSERT INTO Player VALUES
    (1, 'John', 'Doe', '1990-01-01', 'CountryA', 180, 75, 'Forward', 1, 10, 1),
    (2, 'Jane', 'Smith', '1992-03-15', 'CountryB', 175, 68, 'Midfielder', 1, 8, 1),
    (3, 'Michael', 'Johnson', '1993-05-20', 'CountryC', 185, 82, 'Defender', 1, 5, 1),
    (4, 'Emily', 'Williams', '1991-07-10', 'CountryD', 178, 70, 'Forward', 1, 9, 1),
    (5, 'David', 'Brown', '1994-09-25', 'CountryE', 182, 77, 'Midfielder', 1, 7, 1),
    (6, 'Sophia', 'Miller', '1996-11-30', 'CountryF', 187, 85, 'Defender', 1, 6, 1),
    (7, 'Daniel', 'Wilson', '1992-02-15', 'CountryG', 175, 72, 'Forward', 1, 11, 1),
    (8, 'Olivia', 'Anderson', '1995-04-20', 'CountryH', 183, 78, 'Midfielder', 1, 15, 1),
    (9, 'Matthew', 'Thomas', '1993-06-10', 'CountryI', 180, 76, 'Defender', 1, 3, 1),
    (10, 'Isabella', 'Taylor', '1994-08-25', 'CountryJ', 172, 65, 'Forward', 1, 20, 1),
    (11, 'Liam', 'Moore', '1996-10-30', 'CountryK', 188, 88, 'Midfielder', 1, 18, 1);

-- Insert data into Player table for Team 2A
INSERT INTO Player VALUES
    (12, 'Ethan', 'Brown', '1991-01-02', 'CountryA', 179, 76, 'Forward', 2, 11, 1),
    (13, 'Ava', 'Johnson', '1993-03-16', 'CountryB', 174, 67, 'Midfielder', 2, 9, 1),
    (14, 'William', 'Miller', '1995-05-21', 'CountryC', 184, 81, 'Defender', 2, 6, 1),
    (15, 'Mia', 'Smith', '1992-07-11', 'CountryD', 177, 69, 'Forward', 2, 10, 1),
    (16, 'James', 'Davis', '1994-09-26', 'CountryE', 181, 76, 'Midfielder', 2, 8, 1),
    (17, 'Emma', 'Jones', '1996-12-01', 'CountryF', 186, 84, 'Defender', 2, 5, 1),
    (18, 'Alexander', 'Taylor', '1993-02-16', 'CountryG', 176, 71, 'Forward', 2, 7, 1),
    (19, 'Sophia', 'Williams', '1995-04-21', 'CountryH', 182, 77, 'Midfielder', 2, 14, 1),
    (20, 'Benjamin', 'Anderson', '1994-06-11', 'CountryI', 179, 75, 'Defender', 2, 4, 1),
    (21, 'Olivia', 'Thomas', '1995-08-26', 'CountryJ', 173, 64, 'Forward', 2, 19, 1),
    (22, 'Henry', 'Moore', '1997-11-01', 'CountryK', 187, 87, 'Midfielder', 2, 12, 1);


    -- Insert data into Player table for Team 3A
INSERT INTO Player VALUES
    (23, 'Logan', 'Wilson', '1991-01-03', 'CountryA', 178, 74, 'Forward', 3, 9, 1),
    (24, 'Grace', 'Martinez', '1993-03-17', 'CountryB', 173, 66, 'Midfielder', 3, 11, 1),
    (25, 'Lucas', 'Lopez', '1995-05-22', 'CountryC', 183, 80, 'Defender', 3, 7, 1),
    (26, 'Lily', 'Garcia', '1992-07-12', 'CountryD', 176, 68, 'Forward', 3, 10, 1),
    (27, 'Noah', 'Hernandez', '1994-09-27', 'CountryE', 180, 75, 'Midfielder', 3, 8, 1),
    (28, 'Zoe', 'Perez', '1996-12-02', 'CountryF', 185, 83, 'Defender', 3, 6, 1),
    (29, 'Mason', 'Rodriguez', '1993-02-17', 'CountryG', 175, 70, 'Forward', 3, 12, 1),
    (30, 'Aiden', 'Smith', '1995-04-22', 'CountryH', 181, 76, 'Midfielder', 3, 15, 1),
    (31, 'Chloe', 'Davis', '1994-06-12', 'CountryI', 178, 74, 'Defender', 3, 3, 1),
    (32, 'Elijah', 'Jones', '1995-08-27', 'CountryJ', 172, 63, 'Forward', 3, 20, 1),
    (33, 'Avery', 'Thomas', '1997-11-02', 'CountryK', 186, 86, 'Midfielder', 3, 18, 1);


    -- Insert data into Player table for Team 4A
INSERT INTO Player VALUES
    (34, 'Mia', 'Brown', '1991-01-04', 'CountryA', 177, 73, 'Forward', 4, 11, 1),
    (35, 'Elijah', 'Johnson', '1993-03-18', 'CountryB', 172, 65, 'Midfielder', 4, 9, 1),
    (36, 'Ava', 'Miller', '1995-05-23', 'CountryC', 182, 79, 'Defender', 4, 6, 1),
    (37, 'Logan', 'Smith', '1992-07-13', 'CountryD', 175, 67, 'Forward', 4, 10, 1),
    (38, 'Liam', 'Davis', '1994-09-28', 'CountryE', 179, 74, 'Midfielder', 4, 8, 1),
    (39, 'Emma', 'Martinez', '1996-12-03', 'CountryF', 184, 82, 'Defender', 4, 5, 1),
    (40, 'Oliver', 'Taylor', '1993-02-18', 'CountryG', 174, 69, 'Forward', 4, 7, 1),
    (41, 'Sophia', 'Williams', '1995-04-23', 'CountryH', 180, 75, 'Midfielder', 4, 14, 1),
    (42, 'Jackson', 'Anderson', '1994-06-13', 'CountryI', 177, 73, 'Defender', 4, 4, 1),
    (43, 'Amelia', 'Thomas', '1995-08-28', 'CountryJ', 171, 62, 'Forward', 4, 19, 1),
    (44, 'Lucas', 'Moore', '1997-11-03', 'CountryK', 185, 85, 'Midfielder', 4, 12, 1);

    -- Insert data into Player table for Team 1B
INSERT INTO Player VALUES
    (45, 'Liam', 'Johnson', '1991-01-05', 'CountryA', 176, 72, 'Forward', 5, 9, 1),
    (46, 'Olivia', 'Smith', '1993-03-19', 'CountryB', 171, 64, 'Midfielder', 5, 11, 1),
    (47, 'Noah', 'Miller', '1995-05-24', 'CountryC', 181, 78, 'Defender', 5, 6, 1),
    (48, 'Emma', 'Jones', '1992-07-14', 'CountryD', 174, 66, 'Forward', 5, 10, 1),
    (49, 'Sophia', 'Davis', '1994-09-29', 'CountryE', 178, 73, 'Midfielder', 5, 8, 1),
    (50, 'Mason', 'Martinez', '1996-12-04', 'CountryF', 183, 81, 'Defender', 5, 5, 1),
    (51, 'Ava', 'Rodriguez', '1993-02-19', 'CountryG', 173, 68, 'Forward', 5, 7, 1),
    (52, 'Jackson', 'Anderson', '1995-04-24', 'CountryH', 179, 74, 'Midfielder', 5, 14, 1),
    (53, 'Ella', 'Thomas', '1994-06-14', 'CountryI', 176, 72, 'Defender', 5, 3, 1),
    (54, 'Lucas', 'Jones', '1995-08-29', 'CountryJ', 170, 61, 'Forward', 5, 20, 1),
    (55, 'Lily', 'Moore', '1997-11-04', 'CountryK', 184, 84, 'Midfielder', 5, 18, 1);

-- Insert data into Player table for Team 2B
INSERT INTO Player VALUES
    (56, 'Ethan', 'Garcia', '1991-01-06', 'CountryA', 175, 71, 'Forward', 6, 11, 1),
    (57, 'Ava', 'Rodriguez', '1993-03-20', 'CountryB', 170, 63, 'Midfielder', 6, 9, 1),
    (58, 'Mia', 'Perez', '1995-05-25', 'CountryC', 180, 77, 'Defender', 6, 6, 1),
    (59, 'Liam', 'Martinez', '1992-07-15', 'CountryD', 173, 65, 'Forward', 6, 10, 1),
    (60, 'Olivia', 'Lopez', '1994-09-30', 'CountryE', 177, 72, 'Midfielder', 6, 8, 1),
    (61, 'Noah', 'Brown', '1996-12-05', 'CountryF', 182, 80, 'Defender', 6, 5, 1),
    (62, 'Isabella', 'Taylor', '1993-02-20', 'CountryG', 172, 67, 'Forward', 6, 7, 1),
    (63, 'Jackson', 'Smith', '1995-04-25', 'CountryH', 178, 73, 'Midfielder', 6, 14, 1),
    (64, 'Emma', 'Anderson', '1994-06-15', 'CountryI', 175, 71, 'Defender', 6, 4, 1),
    (65, 'Elijah', 'Thomas', '1995-08-30', 'CountryJ', 169, 60, 'Forward', 6, 19, 1),
    (66, 'Sophia', 'Moore', '1997-11-05', 'CountryK', 183, 83, 'Midfielder', 6, 18, 1);

-- Insert data into Player table for Team 3B
INSERT INTO Player VALUES
    (67, 'Mason', 'Taylor', '1991-01-07', 'CountryA', 174, 70, 'Forward', 7, 9, 1),
    (68, 'Ava', 'Brown', '1993-03-21', 'CountryB', 169, 62, 'Midfielder', 7, 11, 1),
    (69, 'Liam', 'Davis', '1995-05-26', 'CountryC', 179, 76, 'Defender', 7, 6, 1),
    (70, 'Emma', 'Miller', '1992-07-16', 'CountryD', 172, 64, 'Forward', 7, 10, 1),
    (71, 'Noah', 'Jones', '1994-10-01', 'CountryE', 176, 71, 'Midfielder', 7, 8, 1),
    (72, 'Olivia', 'Martinez', '1996-12-06', 'CountryF', 181, 79, 'Defender', 7, 5, 1),
    (73, 'Sophia', 'Rodriguez', '1993-02-21', 'CountryG', 171, 66, 'Forward', 7, 7, 1),
    (74, 'Jackson', 'Williams', '1995-04-26', 'CountryH', 177, 72, 'Midfielder', 7, 14, 1),
    (75, 'Ella', 'Anderson', '1994-06-16', 'CountryI', 174, 70, 'Defender', 7, 4, 1),
    (76, 'Elijah', 'Thomas', '1995-08-31', 'CountryJ', 168, 59, 'Forward', 7, 19, 1),
    (77, 'Chloe', 'Moore', '1997-11-06', 'CountryK', 182, 82, 'Midfielder', 7, 18, 1);

-- Insert data into Player table for Team 4B
INSERT INTO Player VALUES
    (78, 'Oliver', 'Garcia', '1991-01-08', 'CountryA', 173, 69, 'Forward', 8, 11, 1),
    (79, 'Sophia', 'Rodriguez', '1993-03-22', 'CountryB', 168, 61, 'Midfielder', 8, 9, 1),
    (80, 'Jackson', 'Perez', '1995-05-27', 'CountryC', 178, 75, 'Defender', 8, 6, 1),
    (81, 'Ava', 'Martinez', '1992-07-17', 'CountryD', 171, 63, 'Forward', 8, 10, 1),
    (82, 'Liam', 'Lopez', '1994-10-02', 'CountryE', 175, 72, 'Midfielder', 8, 8, 1),
    (83, 'Emma', 'Brown', '1996-12-07', 'CountryF', 180, 80, 'Defender', 8, 5, 1),
    (84, 'Mia', 'Taylor', '1993-02-22', 'CountryG', 170, 67, 'Forward', 8, 7, 1),
    (85, 'Noah', 'Smith', '1995-04-27', 'CountryH', 176, 73, 'Midfielder', 8, 14, 1),
    (86, 'Isabella', 'Anderson', '1994-06-17', 'CountryI', 173, 69, 'Defender', 8, 4, 1),
    (87, 'Elijah', 'Thomas', '1995-09-01', 'CountryJ', 167, 58, 'Forward', 8, 19, 1),
    (88, 'Lily', 'Moore', '1997-11-07', 'CountryK', 181, 81, 'Midfielder', 8, 18, 1);

-- Insert data into Position table with two positions for some players
INSERT INTO Position VALUES
    (1, 'Forward'),
    (2, 'Midfielder'),
    (3, 'Defender'),
    (4, 'Forward'),
    (5, 'Midfielder'),
    (6, 'Defender'),
    (7, 'Forward'),
    (8, 'Midfielder'),
    (9, 'Defender'),
    (10, 'Forward'),
    (11, 'Midfielder'),
    (12, 'Defender'),
    (13, 'Forward'),
    (14, 'Midfielder'),
    (15, 'Defender'),
    (16, 'Forward'),
    (17, 'Midfielder'),
    (18, 'Defender'),
    (19, 'Forward'),
    (20, 'Midfielder'),
    (21, 'Defender'),
    (22, 'Forward'),
    (23, 'Midfielder'),
    (24, 'Defender'),
    (25, 'Forward'),
    (26, 'Midfielder'),
    (27, 'Defender'),
    (28, 'Forward'),
    (29, 'Midfielder'),
    (30, 'Defender'),
    (31, 'Forward'),
    (32, 'Midfielder'),
    (33, 'Defender'),
    (34, 'Forward'),
    (35, 'Midfielder'),
    (36, 'Defender'),
    (37, 'Forward'),
    (38, 'Midfielder'),
    (39, 'Defender'),
    (40, 'Forward'),
    (41, 'Midfielder'),
    (42, 'Defender'),
    (43, 'Forward'),
    (44, 'Midfielder'),
    (45, 'Defender'),
    (46, 'Forward'), 
    (46, 'Midfielder'), -- Two positions for Player 46
    (47, 'Midfielder'),
    (48, 'Defender'),
    (48, 'Midfielder'), -- Two positions for Player 48
    (49, 'Forward'),
    (50, 'Midfielder'),
    (51, 'Defender'),
    (51, 'Forward'), -- Two positions for Player 51
    (52, 'Forward'),
    (53, 'Midfielder'),
    (54, 'Defender'),
    (54, 'Midfielder'), -- Two positions for Player 54
    (55, 'Forward'),
    (55, 'Midfielder'), -- Two positions for Player 55
    (56, 'Midfielder'),
    (57, 'Defender'),
    (57, 'Forward'), -- Two positions for Player 57
    (58, 'Forward'),
    (59, 'Midfielder'),
    (60, 'Defender'),
    (60, 'Midfielder'), -- Two positions for Player 60
    (61, 'Forward'),
    (61, 'Defender'), -- Two positions for Player 61
    (62, 'Midfielder'),
    (63, 'Defender'),
    (63, 'Midfielder'), -- Two positions for Player 63
    (64, 'Forward'),
    (65, 'Midfielder'),
    (66, 'Defender'),
    (66, 'Forward'), -- Two positions for Player 66
    (67, 'Forward'),
    (68, 'Midfielder'),
    (69, 'Defender'),
    (69, 'Midfielder'), -- Two positions for Player 69
    (70, 'Forward'),
    (71, 'Midfielder'),
    (72, 'Defender'),
    (72, 'Forward'), -- Two positions for Player 72
    (73, 'Forward'),
    (73, 'Defender'), -- Two positions for Player 73
    (74, 'Midfielder'),
    (75, 'Defender'),
    (75, 'Midfielder'), -- Two positions for Player 75
    (76, 'Forward'),
    (77, 'Midfielder'),
    (78, 'Defender'),
    (78, 'Forward'), -- Two positions for Player 78
    (79, 'Forward'),
    (80, 'Midfielder'),
    (81, 'Defender'),
    (82, 'Forward'),
    (83, 'Midfielder'),
    (84, 'Defender'),
    (85, 'Forward'),
    (86, 'Midfielder'),
    (87, 'Defender'),
    (88, 'Forward');

INSERT INTO Plays VALUES
    (1, 2, 1),
    (3, 4, 2),

    (1, 3, 3),
    (2, 4, 4),

    (1, 4, 5),
    (2, 3, 6),

    (2, 1, 7),
    (4, 3, 8),

    (3, 1, 9),
    (4, 2, 10),

    (4, 1, 11),
    (3, 2, 12),

    (5, 6, 13),
    (7, 8, 14),

    (5, 7, 15),
    (6, 8, 16),

    (5, 8, 17),
    (6, 7, 18),

    (6, 5, 19),
    (8, 7, 20),

    (7, 5, 21),
    (8, 6, 22),

    (8, 5, 23),
    (7, 6, 24);

-- Match 1
INSERT INTO PlayerStats VALUES
    (1, 1, 90, 0, 0, 1, 4, 3, 50, 1, 0, 2);

INSERT INTO PlayerStats VALUES
    (12, 1, 90, 0, 1, 2, 3, 1, 45, 0, 0, 3);

-- Match 2
INSERT INTO PlayerStats VALUES
    (23, 2, 90, 0, 1, 1, 6, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (34, 2, 90, 0, 0, 1, 3, 2, 55, 0, 0, 4);

-- Match 3
INSERT INTO PlayerStats VALUES
    (1, 3, 90, 0, 0, 1, 5, 1, 40, 2, 0, 2);

INSERT INTO PlayerStats VALUES
    (23, 3, 90, 0, 1, 0, 2, 2, 55, 0, 0, 3);

-- Match 4
INSERT INTO PlayerStats VALUES
    (12, 4, 90, 0, 0, 2, 4, 3, 50, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (34, 4, 90, 0, 1, 3, 3, 1, 60, 0, 0, 4);

-- Match 5
INSERT INTO PlayerStats VALUES
    (1, 5, 90, 0, 0, 1, 4, 3, 50, 1, 0, 2);

INSERT INTO PlayerStats VALUES
    (34, 5, 90, 0, 1, 2, 3, 1, 45, 0, 0, 3);

-- Match 6
INSERT INTO PlayerStats VALUES
    (12, 6, 90, 0, 1, 1, 6, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (23, 6, 90, 0, 0, 1, 3, 2, 55, 0, 0, 4);

-- Match 7
INSERT INTO PlayerStats VALUES
    (12, 7, 90, 0, 0, 1, 5, 1, 40, 2, 0, 2);

INSERT INTO PlayerStats VALUES
    (1, 7, 90, 0, 1, 0, 2, 2, 55, 0, 0, 3);

-- Match 8
INSERT INTO PlayerStats VALUES
    (34, 8, 90, 0, 0, 2, 4, 3, 50, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (23, 8, 90, 0, 1, 3, 3, 1, 60, 0, 0, 4);

-- Match 9
INSERT INTO PlayerStats VALUES
    (23, 9, 90, 0, 0, 1, 4, 3, 50, 1, 0, 2);

INSERT INTO PlayerStats VALUES
    (1, 9, 90, 0, 1, 2, 3, 1, 45, 0, 0, 3);

-- Match 10
INSERT INTO PlayerStats VALUES
    (34, 10, 90, 0, 1, 1, 6, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (12, 10, 90, 0, 0, 1, 3, 2, 55, 0, 0, 4);

-- Match 11
INSERT INTO PlayerStats VALUES
    (34, 11, 90, 0, 0, 1, 5, 1, 40, 2, 0, 2);

INSERT INTO PlayerStats VALUES
    (1, 11, 90, 0, 1, 0, 2, 2, 55, 0, 0, 3);

-- Match 12
INSERT INTO PlayerStats VALUES
    (23, 12, 90, 0, 0, 2, 4, 3, 50, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (12, 12, 90, 0, 1, 3, 3, 1, 60, 0, 0, 4);

-- Group B Matches
-- Match 13
INSERT INTO PlayerStats VALUES
    (45, 13, 90, 0, 1, 1, 4, 2, 55, 1, 0, 2);

INSERT INTO PlayerStats VALUES
    (56, 13, 90, 0, 0, 2, 3, 3, 40, 0, 0, 3);

-- Match 14
INSERT INTO PlayerStats VALUES
    (67, 14, 90, 0, 1, 1, 6, 1, 50, 2, 0, 1);

INSERT INTO PlayerStats VALUES
    (78, 14, 90, 0, 0, 1, 3, 2, 55, 0, 0, 4);

-- Match 15
INSERT INTO PlayerStats VALUES
    (45, 15, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (67, 15, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 16
INSERT INTO PlayerStats VALUES
    (56, 16, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (78, 16, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 17
INSERT INTO PlayerStats VALUES
    (45, 17, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (78, 17, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 18
INSERT INTO PlayerStats VALUES
    (56, 18, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (67, 18, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 19
INSERT INTO PlayerStats VALUES
    (56, 19, 90, 0, 1, 1, 4, 2, 55, 1, 0, 2);

INSERT INTO PlayerStats VALUES
    (45, 19, 90, 0, 0, 2, 3, 3, 40, 0, 0, 3);

-- Match 20
INSERT INTO PlayerStats VALUES
    (78, 20, 90, 0, 1, 1, 6, 1, 50, 2, 0, 1);

INSERT INTO PlayerStats VALUES
    (67, 20, 90, 0, 0, 1, 3, 2, 55, 0, 0, 4);

-- Match 21
INSERT INTO PlayerStats VALUES
    (67, 21, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (45, 21, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 22
INSERT INTO PlayerStats VALUES
    (78, 22, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (56, 22, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 23
INSERT INTO PlayerStats VALUES
    (78, 23, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (45, 23, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Match 24
INSERT INTO PlayerStats VALUES
    (67, 24, 90, 0, 1, 2, 5, 2, 60, 1, 0, 1);

INSERT INTO PlayerStats VALUES
    (56, 24, 90, 0, 0, 2, 4, 3, 50, 0, 0, 2);

-- Insert data into Referee table
INSERT INTO Referee VALUES
    (1, 'John', 'Doe', 5),
    (2, 'Jane', 'Smith', 8),
    (3, 'Michael', 'Johnson', 7),
    (4, 'Emily', 'Williams', 6);

-- Insert data into Referees table for matches 1-24
INSERT INTO Referees VALUES
    (1, 1),
    (2, 2),

    (3, 3),
    (4, 4),

    (1, 5),
    (2, 6),

    (3, 7),
    (4, 8),

    (1, 9),
    (2, 10),

    (3, 11),
    (4, 12),

    (1, 13),
    (2, 14),

    (3, 15),
    (4, 16),

    (1, 17),
    (2, 18),

    (3, 19),
    (4, 20),

    (1, 21),
    (2, 22),

    (3, 23),
    (4, 24);
