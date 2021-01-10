BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(64) NOT NULL, 
	email VARCHAR(128) NOT NULL, 
	password_hash VARCHAR(128), 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO users VALUES(1,'admin','a@b.com','pbkdf2:sha256:150000$gtHKW0Ch$40000b781d68cbff87928ed022aca0d07ec4a87d56b70c3e61df4a46eb8a9172');
INSERT INTO users VALUES(2,'testing','testing@testing.com','pbkdf2:sha256:150000$UeqTx6CQ$768bf159bc7ff26440acd6f0b3c235de731af2340135df45bb92e0fdc36e86af');
INSERT INTO users VALUES(3,'joybot','joy@bot.com','pbkdf2:sha256:150000$UVIwyulK$c4df6557abbdfe992b3121ed3523134f711a1e06281b16d763b804e8b7c80552');
CREATE TABLE entry (
	id INTEGER NOT NULL, 
	date TIMESTAMP NOT NULL, 
	author_id INTEGER NOT NULL, 
	mood_rate INTEGER NOT NULL, 
	title TEXT, 
	journal TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author_id) REFERENCES users (id)
);
INSERT INTO entry VALUES(1,'2020-12-27 17:31:08.751311',2,3,'','');
INSERT INTO entry VALUES(2,'2020-12-27 17:31:08.751311',2,2,'123','');
INSERT INTO entry VALUES(9,'2020-12-27 18:10:53.864217',2,1,'testing','');
INSERT INTO entry VALUES(10,'2020-12-28 15:31:13.396165',2,5,replace('testing\r','\r',chr(13)),'entry');
INSERT INTO entry VALUES(11,'2020-12-28 15:31:13.396165',3,5,replace('joybot\r','\r',chr(13)),'entry #1');
INSERT INTO entry VALUES(12,'2020-12-28 15:31:13.396165',3,3,'entry #2','');
INSERT INTO entry VALUES(13,'2020-12-30 15:11:58.454048',1,5,replace('Title\r','\r',chr(13)),'Body text');
INSERT INTO entry VALUES(14,'2020-12-30 15:11:58.454048',1,3,replace('Title 2\r','\r',chr(13)),'Body 2');
INSERT INTO entry VALUES(15,'2021-01-04 11:40:28.353044',2,3,'','');
CREATE UNIQUE INDEX ix_user_username ON users (username);
COMMIT;
