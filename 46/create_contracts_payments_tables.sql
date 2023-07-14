CREATE TABLE IF NOT EXISTS contracts (
                        contr_id INTEGER PRIMARY KEY,
                        count_id INTEGER,
                        contr_date text NOT NULL,
                        summ real,
                        subject text NOT NULL,
                        FOREIGN KEY (count_id)  REFERENCES counterparty (count_id)
                        );
                    CREATE TABLE IF NOT EXISTS payments (
                        paym_id INTEGER PRIMARY KEY,
                        contr_id INTEGER,
                        paym_date text NOT NULL,
                        summ real NOT NULL CHECK(summ >=0) DEFAULT 0,
                        rem text NOT NULL,
                        FOREIGN KEY (contr_id)  REFERENCES contracts (contr_id)
                        );