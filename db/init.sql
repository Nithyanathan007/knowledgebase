CREATE TABLE knowledgebase (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20),
    heading TEXT NOT NULL,
    content TEXT,
    upload_url TEXT,
    status VARCHAR(20) DEFAULT 'active',
    created_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
