CREATE TABLE `system` (
    `key` TEXT PRIMARY KEY,
    `value` TEXT DEFAULT (NULL)
);

CREATE TABLE `user` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `username` TEXT NOT NULL,
    `password` TEXT NOT NULL
);

CREATE TABLE `profile` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `user_id` TEXT NOT NULL REFERENCES `user`(`id`)
);

CREATE TABLE `profile_role` (
    `id` TEXT PRIMARY KEY,
    `edit` BOOLEAN DEFAULT (0),
    `view` BOOLEAN DEFAULT (1),
    `pending` BOOLEAN DEFAULT (1),
    `profile_id` TEXT NOT NULL REFERENCES `profile`(`id`),
    `user_id` TEXT NOT NULL REFERENCES `user`(`id`),
    `is_default` BOOLEAN DEFAULT (0)
);

CREATE TABLE `profile_transfer` (
    `profile_id` TEXT NOT NULL REFERENCES `profile`(`id`),
    `origin_user_id` TEXT NOT NULL REFERENCES `user`(`id`),
    `destiny_user_id` TEXT NOT NULL REFERENCES `user`(`id`)
);

CREATE TABLE `account` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `profile_id` TEXT NOT NULL REFERENCES `profile`(`id`)
);

CREATE TABLE `card` (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `dueDay` INTEGER NOT NULL,
    `limit` REAL NOT NULL,
    `profile_id` TEXT NOT NULL REFERENCES `profile`(`id`)
);

CREATE TABLE `card_invoice` (
    `id` TEXT PRIMARY KEY,
    `month` INTEGER NOT NULL,
    `year` INTEGER NOT NULL,
    `card_id` TEXT NOT NULL REFERENCES `card`(`id`)
);

CREATE TABLE `registry` (
    `id` TEXT PRIMARY KEY,
    `title` TEXT NOT NULL,
    `value` REAL NOT NULL DEFAULT 0,
    `pending` BOOLEAN NOT NULL DEFAULT 0,
    `in` BOOLEAN NOT NULL DEFAULT 0,
    `category` TEXT,
    `date` DATE NOT NULL,
    `description` TEXT,
    `operationName` TEXT,
    `card_invoice_id` TEXT DEFAULT (NULL) REFERENCES `card_invoice`(`id`),
    `account_id` TEXT DEFAULT (NULL) REFERENCES `account`(`id`)
);