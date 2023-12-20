import psycopg2
import json
from RunSVM import getDept
from Sentiment import Get_Senti
from SVMClassifier import depclass


conn = psycopg2.connect(
    host="10.0.0.123",
    port="5432",
    user="postgres",
    password="sarguru",
    database="news"
)

cursor = conn.cursor()

source_table_name = "unclassified_youtube"
destination_table_name = "backend_classified_all"
while True:
    cursor.execute(f"SELECT * FROM {source_table_name} WHERE is_processed = false;")
    rows = cursor.fetchall()

    for row in rows:
        json_data = row[2]
        print(json_data)
        headline = (json_data).get("content_en")

        # Inference From Model
        department = getDept(headline)
        tonality = Get_Senti(headline)
        json_data = json.dumps(json_data)
        try:
            is_govt, tonality, department = depclass(headline)
            if is_govt.lower() == 'Yes' or is_govt.lower() == 'Positive' or is_govt.lower() == 'true':
                cursor.execute(
                    f"INSERT INTO {destination_table_name} (created_at, json_data, tonality, department, modality) "
                    f"VALUES (current_timestamp, %s, %s, %s, 'Website');",
                    (json_data, tonality, department)
                )
                print(2)

                cursor.execute(f"UPDATE {source_table_name} SET is_processed = true WHERE id = %s;", (row[0],))
        except:
            cursor.execute(
                    f"INSERT INTO {destination_table_name} (created_at, json_data, tonality, department, modality) "
                    f"VALUES (current_timestamp, %s, %s, %s, 'Website');",
                    (json_data, tonality, department)
                )
            print(2)

            cursor.execute(f"UPDATE {source_table_name} SET is_processed = true WHERE id = %s;", (row[0],))


    conn.commit()

cursor.close()
conn.close()
