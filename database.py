
import sqlite3

def create_database():

    conn = sqlite3.connect("business_plans.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_idea TEXT,
            question TEXT,
            generated_plan TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_plan(business_idea, question, generated_plan):

    conn = sqlite3.connect("business_plans.db")

    conn.execute("""
        INSERT INTO plans (
            business_idea,
            question,
            generated_plan
        )
        VALUES (?, ?, ?)
    """, (
        business_idea,
        question,
        generated_plan
    ))

    conn.commit()
    conn.close()


def get_plans():

    conn = sqlite3.connect("business_plans.db")

    cursor = conn.execute("""
        SELECT id, business_idea, question,
               generated_plan, created_at
        FROM plans
        ORDER BY id DESC
    """)

    plans = cursor.fetchall()

    conn.close()

    return plans
