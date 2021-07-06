import psycopg2, random, string, time, datetime

conn = psycopg2.connect("dbname={} user={} password={} host={}".format("crawler","crawler","th1sIsNotAGoodPassw0rd","postgres"))


def makeTables():
    with conn.cursor() as curs:
        curs.execute(sql)
        conn.commit()

def writeUrls(urls, token):
    with conn.cursor() as curs:
        for each in urls:
            curs.execute("INSERT INTO urls (url, crawler_id) VALUES (%s, %s)", (each, token))
        conn.commit()

def getToken():
    with conn.cursor() as curs:
        base64 = string.ascii_letters + string.digits + "+/"
        token = "".join(random.choice(base64) for _ in range(16))
        curs.execute("INSERT INTO agents (agent_id, created) VALUES (%s, %s)", (token, datetime.datetime.now()))
        conn.commit()
        return token

sql = """
-- Adminer 4.8.1 PostgreSQL 13.3 (Debian 13.3-1.pgdg100+1) dump

CREATE TABLE "public"."agents" (
    "agent_id" character varying(64) NOT NULL,
    "created" timestamptz NOT NULL,
    CONSTRAINT "agents_id" PRIMARY KEY ("agent_id")
) WITH (oids = false);


CREATE SEQUENCE urls_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 5 CACHE 1;

CREATE TABLE "public"."urls" (
    "id" integer DEFAULT nextval('urls_id_seq') NOT NULL,
    "url" character varying(128) NOT NULL,
    "crawler_id" character varying(64) NOT NULL,
    "completed" boolean DEFAULT false NOT NULL,
    CONSTRAINT "urls_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


ALTER TABLE ONLY "public"."urls" ADD CONSTRAINT "urls_crawler_id_fkey" FOREIGN KEY (crawler_id) REFERENCES agents(agent_id) ON UPDATE RESTRICT NOT DEFERRABLE;

-- 2021-07-06 23:42:23.640861+00
"""
