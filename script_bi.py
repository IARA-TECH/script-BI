from dotenv import load_dotenv
from os import getenv
import gspread
import psycopg2
from oauth2client.service_account import ServiceAccountCredentials

def clean_int(value):
    return int(value) if str(value).isdigit() else None

def clean_value(value):
    if value in ("", None):
        return None
    return value

load_dotenv()

# --- Autenticação Google Sheets ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    getenv("CREDENTIALS_PATH"),
    scope
)
client = gspread.authorize(creds)

# Abrir planilha
sheet = client.open("Abacus Info").worksheet("dados_forms")
rows = sheet.get_all_records()

conn = psycopg2.connect(
    dbname=getenv("DB_NAME"),
    user=getenv("DB_USER"),
    password=getenv("DB_PASSWORD"),
    host=getenv("DB_HOST"),
    port=getenv("DB_PORT")
)
cur = conn.cursor()

# --- Inserir dados ---
for row in rows:
    # Inserir ou atualizar survey pelo e-mail
    cur.execute("""
        INSERT INTO abacus_survey (
            email,
            age,
            job_responsibilities,
            state,
            abacus_counting_importance,
            abacus_counting_time,
            has_problems,
            technology_acceptance,
            can_use_mobile,
            is_signal_quality_satisfactory,
            photo_without_interference,
            lighting_quality,
            would_use_or_recommend,
            problems_quantity
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (email) DO UPDATE SET
            age = EXCLUDED.age,
            job_responsibilities = EXCLUDED.job_responsibilities,
            state = EXCLUDED.state,
            abacus_counting_importance = EXCLUDED.abacus_counting_importance,
            abacus_counting_time = EXCLUDED.abacus_counting_time,
            has_problems = EXCLUDED.has_problems,
            technology_acceptance = EXCLUDED.technology_acceptance,
            can_use_mobile = EXCLUDED.can_use_mobile,
            is_signal_quality_satisfactory = EXCLUDED.is_signal_quality_satisfactory,
            photo_without_interference = EXCLUDED.photo_without_interference,
            lighting_quality = EXCLUDED.lighting_quality,
            would_use_or_recommend = EXCLUDED.would_use_or_recommend,
            problems_quantity = EXCLUDED.problems_quantity
        RETURNING id
    """, (
        row.get("email"),
        row.get("age"),
        row.get("job_responsibilities"),
        row.get("state"),
        row.get("abacus_counting_importance"),
        row.get("abacus_counting_time"),
        row.get("has_problems"),
        clean_int(row.get("technology_acceptance")),
        clean_value(row.get("can_use_mobile")),
        clean_value(row.get("is_signal_quality_satisfactory")),
        clean_value(row.get("photo_without_interference")),
        clean_int(row.get("lighting_quality")),
        row.get("would_use_or_recommend"),
        row.get("problems_quantity")
    ))
    
    # pegar o ID gerado no abacus_survey
    survey_id = cur.fetchone()[0]

    # se a planilha tiver uma coluna "issues" com valores separados por ","
    issues_str = row.get("issues")
    if issues_str:
        for issue in issues_str.split(","):
            cur.execute("""
                INSERT INTO issues (survey_id, issue_description)
                VALUES (%s, %s)
                ON CONFLICT (survey_id, issue_description) DO NOTHING
            """, (survey_id, issue.strip().capitalize()))

conn.commit()
cur.close()
conn.close()
