from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from config import Config
from models import kb_model

kb_bp = Blueprint('kb', __name__)

@kb_bp.route('/kb', methods=['POST'])
def create_kb():
    data = request.form
    file = request.files.get('file')

    upload_url = None
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        upload_url = filepath

    new_kb = {
        'type': data.get('type'),
        'heading': data.get('heading'),
        'content': data.get('content'),
        'upload_url': upload_url,
        'created_by': data.get('created_by')
    }

    kb_id = kb_model.create_kb(new_kb)
    return jsonify({'id': kb_id, 'message': 'Post created'}), 201

@kb_bp.route('/kb', methods=['GET'])
def get_kbs():
    posts = kb_model.get_all_kbs()
    result = []
    for row in posts:
        result.append({
            'id': row[0],
            'type': row[1],
            'heading': row[2],
            'content': row[3],
            'upload_url': row[4],
            'status': row[5],
            'created_by': row[6],
            'created_at': row[7],
            'updated_by': row[8],
            'updated_at': row[9],
        })
    return jsonify(result)
