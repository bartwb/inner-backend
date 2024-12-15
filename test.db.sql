BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
CREATE TABLE IF NOT EXISTS "battery" (
	"id"	INTEGER NOT NULL,
	"serial_number"	VARCHAR NOT NULL,
	"build_year"	VARCHAR NOT NULL,
	"battery_type_id"	INTEGER,
	"customer_id"	INTEGER,
	"total_distance"	INTEGER,
	"main_reason"	VARCHAR,
	"comment"	VARCHAR,
	UNIQUE("build_year"),
	PRIMARY KEY("id"),
	UNIQUE("serial_number"),
	CONSTRAINT "fk_battery_type" FOREIGN KEY("battery_type_id") REFERENCES "battery_type"("id"),
	CONSTRAINT "fk_customer" FOREIGN KEY("customer_id") REFERENCES "customer"("id")
);
CREATE TABLE IF NOT EXISTS "battery_finding" (
	"id"	INTEGER NOT NULL,
	"battery_id"	INTEGER NOT NULL,
	"annotation"	JSON NOT NULL,
	PRIMARY KEY("id"),
	CONSTRAINT "fk_battery_id" FOREIGN KEY("battery_id") REFERENCES "battery"("id")
);
CREATE TABLE IF NOT EXISTS "battery_log" (
	"id"	INTEGER NOT NULL,
	"battery_id"	INTEGER NOT NULL,
	"timestamp"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id"),
	CONSTRAINT "fk_battery_id" FOREIGN KEY("battery_id") REFERENCES "battery"("id")
);
CREATE TABLE IF NOT EXISTS "battery_type" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	"serial_number"	VARCHAR NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "customer" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	"street_name"	VARCHAR,
	"house_number"	VARCHAR,
	"city"	VARCHAR,
	"country"	VARCHAR,
	"phone_number"	VARCHAR,
	"email_address"	VARCHAR NOT NULL,
	"customer_type_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	CONSTRAINT "fk_customer_type" FOREIGN KEY("customer_type_id") REFERENCES "customer_type"("id")
);
CREATE TABLE IF NOT EXISTS "customer_type" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "image" (
	"id"	INTEGER NOT NULL,
	"battery_id"	INTEGER NOT NULL,
	"slide"	INTEGER NOT NULL,
	"file_name"	VARCHAR NOT NULL,
	"blob_url"	VARCHAR NOT NULL,
	PRIMARY KEY("id"),
	CONSTRAINT "fk_battery_id" FOREIGN KEY("battery_id") REFERENCES "battery"("id")
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR NOT NULL,
	"email"	VARCHAR NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("username")
);
INSERT INTO "alembic_version" VALUES ('e14d5170df65');
INSERT INTO "battery" VALUES (1,'Broken','Tesla',NULL,NULL,NULL,NULL,NULL);
INSERT INTO "user" VALUES (1,'Dono','donovankhoun@gmail.com');
COMMIT;
