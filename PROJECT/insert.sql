-- Insert random data into Court table
INSERT INTO Court (courtID, CourtName, Capacity, Location)
VALUES
    (1, 'Court A', 100, 'Location A'),
    (2, 'Court B', 150, 'Location B'),
    (3, 'Court C', 120, 'Location C'),
    (4, 'Court D', 200, 'Location D'),
    (5, 'Court E', 180, 'Location E');

-- Insert random data into Championship table
INSERT INTO Championship (ChampionshipID, ChampionshipName, StartDate, EndDate, Description)
VALUES
    (1, 'Championship 1', '2024-01-01', '2024-01-31', 'Description 1');

-- Insert random data into Team table
INSERT INTO Team (TeamID, TeamName, TeamFoundedDate, TeamCoachFname, TeamCoachLname, CourtOwnedID, ChampionshipID)
VALUES
    (1, 'Team A', '2000-01-01', 'Coach A', 'Coach A', 1, 1),
    (2, 'Team B', '2005-01-01', 'Coach B', 'Coach B', 2, 1),
    (3, 'Team C', '2010-01-01', 'Coach C', 'Coach C', 3, 1),
    (4, 'Team D', '2015-01-01', 'Coach D', 'Coach D', 4, 1),
    (5, 'Team E', '2020-01-01', 'Coach E', 'Coach E', 5, 1);

-- Insert random data into Referee table
INSERT INTO Referee (RefereeID, FirstName, LastName, Experience)
VALUES
    (1, 'Referee A', 'Lastname', 5),
    (2, 'Referee B', 'Lastname', 8),
    (3, 'Referee C', 'Lastname', 3),
    (4, 'Referee D', 'Lastname', 6),
    (5, 'Referee E', 'Lastname', 4);

-- Insert random data into Match table
INSERT INTO Match (MatchID, Date, Time, CourtID)
VALUES
    (1, '2024-01-10', '14:00:00', 1),
    (2, '2024-02-15', '16:30:00', 2),
    (3, '2024-03-20', '18:45:00', 3),
    (4, '2024-04-05', '12:00:00', 4),
    (5, '2024-05-15', '15:15:00', 5);

-- Insert random data into Plays table
INSERT INTO Plays (HomeTeamID, GuestTeamID, MatchID)
VALUES
    (1, 2, 1),
    (2, 3, 2),
    (3, 1, 3),
    (4, 5, 4),
    (5, 4, 5);

-- Insert random data into Includes table
INSERT INTO Includes (ChampionshipID, MatchID)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5);

-- Insert random data into Referees table
INSERT INTO Referees (RefereeID, MatchID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

-- Insert random data into Player table
INSERT INTO Player (PlayerID, FirstName, LastName, DateOfBirth, Nationality, Height, Weight, Position, TeamID, JerseyNumber, MatchID)
VALUES
    (1, 'Player A', 'Lastname', '1995-05-20', 'Nationality A', 180, 75, 'Forward', 1, 10, 1),
    (2, 'Player B', 'Lastname', '1990-08-15', 'Nationality B', 175, 70, 'Midfielder', 2, 8, 2),
    (3, 'Player C', 'Lastname', '1998-03-25', 'Nationality C', 185, 80, 'Defender', 3, 5, 3),
    (4, 'Player D', 'Lastname', '1992-12-10', 'Nationality D', 178, 72, 'Goalkeeper', 4, 1, 4),
    (5, 'Player E', 'Lastname', '1996-07-05', 'Nationality E', 182, 78, 'Midfielder', 5, 7, 5);

-- Insert random data into PlayerStats table
INSERT INTO PlayerStats (PlayerID, MatchID, MinutesPlayed, RedCards, YellowCards, GoalsScored, Shots, ShotsOnTarget, Passes, Assists, Offsides, Tackles)
VALUES
    (1, 1, 90, 0, 1, 2, 10, 5, 30, 1, 0, 5),
    (2, 2, 85, 0, 0, 1, 8, 3, 25, 2, 1, 4),
    (3, 3, 88, 0, 1, 0, 5, 2, 20, 0, 0, 6),
    (4, 4, 90, 0, 0, 0, 2, 0, 15, 0, 0, 2),
    (5, 5, 87, 0, 1, 1, 7, 4, 28, 3, 1, 3);

-- Insert random data into Position table
INSERT INTO Position (PlayerID, Position)
VALUES
    (1, 'Forward'),
    (2, 'Midfielder'),
    (3, 'Defender'),
    (4, 'Goalkeeper'),
    (5, 'Midfielder');