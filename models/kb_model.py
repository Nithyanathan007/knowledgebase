import psycopg2
from config import Config

def get_connection():
    return psycopg2.connect(**Config.DB_CONFIG)

def create_kb(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO knowledgebase (type, heading, content, upload_url, created_by)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
    """, (data['type'], data['heading'], data['content'], data['upload_url'], data['created_by']))
    
    kb_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return kb_id

def get_all_kbs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM knowledgebase ORDER BY created_at DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
