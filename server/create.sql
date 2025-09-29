CREATE TABLE `system` (
    `key` TEXT PRIMARY KEY,
    `value` TEXT DEFAULT (NULL)
);

CREATE TABLE `user` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `username` TEXT NOT NULL,
    `password` TEXT NOT NULL
);

CREATE TABLE `third` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `userId` TEXT NOT NULL REFERENCES `user`(`id`)
);

CREATE TABLE `category` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `type` INTEGER NOT NULL,
    `description` TEXT,
    `userId` TEXT NOT NULL REFERENCES `user`(`id`)
);

CREATE TABLE `card` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `userId` TEXT NOT NULL REFERENCES `user`(`id`)
);

CREATE TABLE `registry` (
    `id` TEXT PRIMARY KEY,
    `type` INTEGER NOT NULL,
    `title` TEXT NOT NULL,
    `value` REAL NOT NULL DEFAULT 0,
    `datetime` DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
    `description` TEXT,
    `userId` TEXT NOT NULL REFERENCES `user`(`id`),
    `cardId` TEXT DEFAULT (NULL) REFERENCES `card`(`id`),
    `categoryId` TEXT DEFAULT (NULL) REFERENCES `category`(`id`),
    `thirdId` TEXT DEFAULT (NULL) REFERENCES `third`(`id`)
);