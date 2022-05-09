CREATE TABLE [IF NOT EXISTS] Book (
    TitleID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Synopsis TEXT NOT NULL,
    CountryCode INTEGER NOT NULL,
    FOREIGN KEY (CountryCode) references Country (Code) 
);

CREATE TABLE [IF NOT EXISTS] Author (
    TitleID TEXT NOT NULL,
    AuthorID INTEGER NOT NULL,
    FOREIGN KEY (AuthorID) references AuthorDetails (AuthorID)
);

CREATE TABLE [IF NOT EXISTS] AuthorDetails (
    AuthorID INTEGER NOT NULL PRIMARY KEY
    Name TEXT NOT NULL
);

CREATE TABLE [IF NOT EXISTS] Song (
  SongID INTEGER NOT NULL PRIMARY KEY,
  Name INTEGER NOT NULL,
  CountryCode INTEGER NOT NULL,
  FOREIGN KEY (CountryCode) references Country (CountryCode)  
);

CREATE TABLE [IF NOT EXISTS] Artist (
    SongID INTEGER NOT NULL PRIMARY KEY,
    ArtistID INTEGER NOT NULL,
    FOREIGN KEY (ArtistID) references ArtistDetails (ArtistID)
);

CREATE TABLE [IF NOT EXISTS] ArtistDetails (
    ArtistID INTEGER NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL
);

CREATE TABLE [IF NOT EXISTS] Country (
    Code TEXT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL
);