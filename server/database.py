import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.init_db()

    def init_db(self):
        cursor = self.conn.cursor()
        # create user table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id TEXT PRIMARY KEY)''')
        #create post table
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                            title TEXT PRIMARY KEY, text TEXT, video_url TEXT, 
                            image_url TEXT, author TEXT, score INTEGER, state INTEGER, 
                            publication_date TEXT)''')
        # create comment table
        cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                                text TEXT PRIMARY KEY, author TEXT, score INTEGER, 
                                state INTEGER, publication_date TEXT, post_id TEXT)''')   
        #create subreddits table
        cursor.execute('''CREATE TABLE IF NOT EXISTS subreddits (
                            name TEXT PRIMARY KEY, visibility INTEGER, tags TEXT)''')
        self.conn.commit()


    def add_post(self, title, text, video_url, image_url, author, score, state, publication_date):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO posts (title, text, video_url, image_url, author, score, state, publication_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                           (title, text, video_url, image_url, author, score, state, publication_date))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def add_comment(self, text, author, score, state, publication_date, post_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO comments (text, author, score, state, publication_date, post_id) VALUES (?, ?, ?, ?, ?, ?)", 
                           (text, author, score, state, publication_date, post_id))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def add_subreddit(self, name, visibility, tags):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO subreddits (name, visibility, tags) VALUES (?, ?, ?)", 
                           (name, visibility, ','.join(tags)))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    def post_exists(self, title):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM posts WHERE title = ?", (title,))
        return cursor.fetchone() is not None

    def user_exists(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None

    def comment_exists(self, text):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM comments WHERE text = ?", (text,))
        return cursor.fetchone() is not None

    def subreddit_exists(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM subreddits WHERE name = ?", (name,))
        return cursor.fetchone() is not None

    def update_post_score(self, title, score_change):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE posts SET score = score + ? WHERE title = ?", (score_change, title))
        self.conn.commit()
        return cursor.rowcount > 0

    def update_comment_score(self, text, score_change):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE comments SET score = score + ? WHERE text = ?", (score_change, text))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def get_post(self, title):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title = ?", (title,))
        row = cursor.fetchone()
        if row:
            return post_pb2.Post(
                title=row[0], text=row[1], video_url=row[2], image_url=row[3],
                author=row[4], score=row[5], state=row[6], 
                publication_date=row[7])
        return None