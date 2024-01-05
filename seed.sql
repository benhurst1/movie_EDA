CREATE TABLE "movies" (
  "id" INT PRIMARY KEY,
  "title" varchar,
  "release_year" integer,
  "release_date" date,
  "rating" varchar(10),
  "runtime" integer,
  "box_office" integer
);

CREATE TABLE "persons" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(50) UNIQUE
);

CREATE TABLE "movies_persons" (
  "id" SERIAL PRIMARY KEY,
  "movie_id" integer,
  "person_id" integer,
  "role" varchar(9)
);

CREATE TABLE "genres" (
  "id" SERIAL PRIMARY KEY,
  "genre" varchar(15) UNIQUE
);

CREATE TABLE "movies_genres" (
  "id" SERIAL PRIMARY KEY,
  "movie_id" integer,
  "genre_id" integer
);

ALTER TABLE "movies_genres" ADD FOREIGN KEY ("movie_id") REFERENCES "movies" ("id");

ALTER TABLE "movies_genres" ADD FOREIGN KEY ("genre_id") REFERENCES "genres" ("id");

ALTER TABLE "movies_persons" ADD FOREIGN KEY ("movie_id") REFERENCES "movies" ("id");

ALTER TABLE "movies_persons" ADD FOREIGN KEY ("person_id") REFERENCES "persons" ("id");
