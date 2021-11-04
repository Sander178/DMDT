UPDATE movies
SET rank = ts_rank(lexemesSummary,plainto_tsquery(
(
SELECT Starring FROM movies WHERE url='star-wars-episode-v---the-empire-strikes-back'
)
));
CREATE TABLE recommendationsBasedOnStarringEmpire10 AS
SELECT url, rank FROM movies WHERE rank > 0.10 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnStarringEmpire10) to '/home/pi/RSL/top50recommendationsStarringEmpire10.csv' WITH csv;
