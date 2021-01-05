CREATE TABLE IF NOT EXISTS payments (
    id INT NOT NULL PRIMARY KEY,
    user_id INT NOT NULL,
    iban VARCHAR(36) NOT NULL,
    amount INT NOT NULL,
    reference TEXT NOT NULL,
    created_date DATETIME NOT NULL DEFAULT (datetime('now','localtime'))
);

INSERT OR IGNORE INTO payments(id, user_id, iban, amount, reference) VALUES(99901, 1001, 'GB4370445677787654', 109923, 'Council Tax');
INSERT OR IGNORE INTO payments(id, user_id, iban, amount, reference) VALUES(99902, 1001, 'GB4370445677787654', 2953, 'Mobile payment');
INSERT OR IGNORE INTO payments(id, user_id, iban, amount, reference) VALUES(99903, 1002, 'RU7622334957432737462', 1000000000, 'Personal transfer');
