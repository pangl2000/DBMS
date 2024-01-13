-- Create Court table
CREATE TABLE Court (
    courtID INT PRIMARY KEY,
    CourtName VARCHAR(255),
    Capacity INT,
    Location VARCHAR(255)
);

-- Create Championship table
CREATE TABLE Championship (
    ChampionshipID INT PRIMARY KEY,
    ChampionshipName VARCHAR(255),
    StartDate DATE,
    EndDate DATE,
    Description VARCHAR(255)
);

-- Create Team table
CREATE TABLE Team (
    TeamID INT PRIMARY KEY,
    TeamName VARCHAR(255),
    TeamFoundedDate DATE,
    TeamCoachFname VARCHAR(255),
    TeamCoachLname VARCHAR(255),
    CourtOwnedID INT,
    ChampionshipID INT,
    FOREIGN KEY (CourtOwnedID) REFERENCES Court(courtID),
    FOREIGN KEY (ChampionshipID) REFERENCES Championship(ChampionshipID)
);

-- Create Referee table
CREATE TABLE Referee (
    RefereeID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Experience INT
);

-- Create Match table
CREATE TABLE Match (
    MatchID INT PRIMARY KEY,
    Date DATE,
    Time TIME,
    CourtID INT,
    Phase VARCHAR(255),
    FOREIGN KEY (CourtID) REFERENCES Court(courtID)
);

-- Create Plays table
CREATE TABLE Plays (
    HomeTeamID INT,
    GuestTeamID INT,
    MatchID INT,
    PRIMARY KEY (HomeTeamID, GuestTeamID, MatchID),
    FOREIGN KEY (HomeTeamID) REFERENCES Team(TeamID),
    FOREIGN KEY (GuestTeamID) REFERENCES Team(TeamID),
    FOREIGN KEY (MatchID) REFERENCES Match(MatchID)
);

-- Create Plays table
CREATE TABLE CompetesIn (
    PlayerID INT,
    MatchID INT,
    PRIMARY KEY (PlayerID, MatchID),
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (MatchID) REFERENCES Match(MatchID)
);

-- Create Includes table
CREATE TABLE Includes (
    ChampionshipID INT,
    MatchID INT,
    PRIMARY KEY (ChampionshipID, MatchID),
    FOREIGN KEY (ChampionshipID) REFERENCES Championship(ChampionshipID),
    FOREIGN KEY (MatchID) REFERENCES Match(MatchID)
);

-- Create Referees table
CREATE TABLE Referees (
    RefereeID INT,
    MatchID INT,
    PRIMARY KEY (RefereeID, MatchID),
    FOREIGN KEY (RefereeID) REFERENCES Referee(RefereeID),
    FOREIGN KEY (MatchID) REFERENCES Match(MatchID)
);

-- Create Player table
CREATE TABLE Player (
    PlayerID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Nationality VARCHAR(255),
    Height FLOAT,
    Weight FLOAT,
    Position VARCHAR(255),
    TeamID INT,
    JerseyNumber INT,
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
);

-- Create PlayerStats table
CREATE TABLE PlayerStats (
    PlayerID INT,
    MatchID INT,
    MinutesPlayed INT,
    RedCards INT,
    YellowCards INT,
    GoalsScored INT,
    Shots INT,
    ShotsOnTarget INT,
    Passes INT,
    Assists INT,
    Offsides INT,
    Tackles INT,
    PRIMARY KEY (PlayerID, MatchID),
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (MatchID) REFERENCES Match(MatchID)
);

-- Create Position table
CREATE TABLE Position (
    PlayerID INT,
    Position VARCHAR(255),
    PRIMARY KEY (PlayerID, Position),
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID)
);
