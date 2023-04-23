-- Account
CREATE TABLE IF NOT EXISTS Account
(
    id         serial       NOT NULL PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name  varchar(255) NOT NULL,
    email      varchar(255) NOT NULL
);

-- Posting
CREATE TABLE IF NOT EXISTS Posting
(
    id          serial       NOT NULL PRIMARY KEY,
    name        varchar(255) NOT NULL,
    description text         NOT NULL,
    date        date         NOT NULL,
    a           bool         NOT NULL,
    b           int          NOT NULL,
    c           float        NOT NULL
);


-- PostingFilter
CREATE TABLE IF NOT EXISTS PostingFilter
(
    id      serial       NOT NULL PRIMARY KEY,
    creator int          NOT NULL REFERENCES Account (id) ON DELETE CASCADE,
    name    varchar(255) NOT NULL,
    expires date         NOT NULL,
    a       bool,
    b_lower int,
    b_upper int
        CHECK (b_lower IS NULL OR b_upper IS NOT NULL),
    c_lower float,
    c_upper float
        CHECK (c_lower IS NULL OR c_upper IS NOT NULL)

);
