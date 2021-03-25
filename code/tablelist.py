# note for max value for each attribute
# -- mId: 459488
# -- homepage: 138
# -- title: 86
# -- tagLine: approximation
# -- voteCount: 13752
# -- releaseDate: length of MM/DD/YYYY = 10
# -- runTime: 338
# -- budget: 380000000
# -- revenue: 2787965087
# -- popularity: 875.581305
# -- overview: 1000
# -- originalTitle: 86
movie = ["""CREATE TABLE Movie (
                budget int,
                homepage varchar(150),
                mId mediumint NOT NULL DEFAULT 0,
                originalLanguage varCHAR(2),
                title varchar(100),
                tagline varchar(300),
                voteAverage float,
                voteCount int,
                status set('Released', 'Rumored', 'Post Production'),
                releaseDate varchar(10),
                runTime mediumint DEFAULT 0,
                revenue bigint, 
                popularity float,
                overview varchar(1000),
                originalTitle varchar(100),
                primary key (mId))"""]

# max value for ID: 10770
genre = ["""CREATE TABLE Genre (
                id smallint,
                name varchar(20),
                primary key (id));"""]

# Spoken Language
spokenLanguage = ["""CREATE TABLE SpokenLanguage (
                        iso_639_1 varchar(5),
                        name varchar(20),
                        primary key (iso_639_1));"""]

# Production country
production_country = ["""CREATE TABLE ProductionCountries (
                            iso_3166_1 varchar(5),
                            name varchar(50),
                            primary key (iso_3166_1));"""]

# max id for production_companies: 95063
production_company = ["""CREATE TABLE ProductionCompanies (
                            id mediumint,
                            name varchar(80),
                            primary key (id));"""]

# max value for keywords id: 238222
keyword = ["""CREATE TABLE Keywords (
                id mediumint,
                name varchar(50),
                primary key (id));"""]

# join table between production_country and movie
from_country = ["""CREATE TABLE FromCountry (
                mId mediumint,
                cId varchar(5),
                foreign key(mId) references Movie(mId),
                foreign key(cId) references ProductionCountries(iso_3166_1));
                """]

# join table between production_company and movie
from_company = ["""CREATE TABLE FromCompany (
                    mId mediumint,
                    cId mediumint,
                    foreign key(mId) references Movie(mId),
                    foreign key(cId) references ProductionCompanies(id));"""]

# join table between keywords and movie
has_keyword = ["""CREATE TABLE HasKeyword (
                    mId mediumint,
                    kId mediumint,
                    foreign key(mId) references Movie(mId),
                    foreign key(kId) references Keywords(id));"""]

# join table between genre and movie
has_genre = ["""CREATE TABLE HasGenre (
                    mId mediumint,
                    gId smallint,
                    foreign key(mId) references Movie(mId),
                    foreign key(gId) references Genre(id));"""]

# join table between spoken_language and movie
languages = ["""CREATE TABLE HasLanguages (
                    mId mediumint,
                    lId varchar(5),
                    foreign key(mId) references Movie(mId),
                    foreign key(lId) references SpokenLanguage(iso_639_1));"""]

table_list = []
table_list += movie + genre + spokenLanguage + production_company
table_list += production_country + keyword
table_list += from_company + from_country + has_genre + has_keyword + languages

drop_list = ["DROP TABLE IF EXISTS FromCountry"]
drop_list += ["DROP TABLE IF EXISTS HasKeyword"]
drop_list += ["DROP TABLE IF EXISTS FromCompany"]
drop_list += ["DROP TABLE IF EXISTS HasGenre"]
drop_list += ["DROP TABLE IF EXISTS HasLanguages"]
drop_list += ["DROP TABLE IF EXISTS Movie"]
drop_list += ["DROP TABLE IF EXISTS Genre"]
drop_list += ["DROP TABLE IF EXISTS SpokenLanguage"]
drop_list += ["DROP TABLE IF EXISTS ProductionCountries"]
drop_list += ["DROP TABLE IF EXISTS ProductionCompanies"]
drop_list += ["DROP TABLE IF EXISTS Keywords"]

movie_attribute_list = ["budget",
                        "homepage",
                        "id",
                        "original_language",
                        "title",
                        "tagline",
                        "vote_average",
                        "vote_count",
                        "status",
                        "release_date",
                        "runtime",
                        "revenue",
                        "popularity",
                        "overview",
                        "original_title"]

movie_int_list = ["budget", "vote_count"]
movie_float_list = ["vote_average", "runtime", "revenue", "popularity"]