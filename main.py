from fastapi import FastAPI, Query
import cx_Oracle

app = FastAPI()

# Database connection configuration
dsn = cx_Oracle.makedsn("host_name", "port", service_name="")
connection = cx_Oracle.connect("schema_name", "password", dsn)


@app.get("/search/{document_title}")
async def search_data(document_title: str):
    """
    Perform a wildcard search in the Oracle database.
    """
    results = []

    # Create a cursor
    with connection.cursor() as cursor:
        # Execute the wildcard query
        cursor.execute("SELECT * FROM documents WHERE document_title LIKE :query", query=f'%{document_title}%')

        # Fetch all results
        for row in cursor.fetchall():
            # Convert the Oracle row to a dictionary
            result = dict(zip([d[0] for d in cursor.description], row))
            results.append(result)

    return {"results": results}
