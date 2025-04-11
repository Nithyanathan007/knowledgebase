from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# DB connectionpi[]
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="knowledgebase",
    user="postgres",
    password="1234"
)
cur = conn.cursor()

@app.route("/api/knowledgebase", methods=["POST"])
def create_post():
    data = request.json
    cur.execute("""
        INSERT INTO knowledgebase (type, heading, content, upload_url, status, created_by, updated_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data["type"],
        data["heading"],
        data["content"],
        data.get("upload_url"),
        data["status"],
        data["created_by"],
        data["updated_by"]
    ))
    conn.commit()
    return jsonify({"message": "Post created successfully!"}), 201

@app.route("/api/knowledgebase", methods=["GET"])
def get_all_posts():
    cur.execute("SELECT * FROM knowledgebase;")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route("/api/knowledgebase", methods=["DELETE"])
def delete_all():
    cur.execute("TRUNCATE TABLE knowledgebase RESTART IDENTITY;")
    conn.commit()
    return jsonify({"message": "All posts deleted!"})
if __name__ == '__main__':
    print("🚀 Flask app is running on http://127.0.0.1:5000")
    app.run(debug=True)