import duckdb

conn = duckdb.connect(r"C:\InvestmentPerformanceTrackerV2\data\dev.duckdb")

# Check schemas
schemas = conn.execute("SELECT schema_name FROM information_schema.schemata").fetchall()
print("Schemas:", schemas)

# Check tables in bronze schema
tables = conn.execute(
    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'bronze'"
).fetchall()
print("Bronze tables:", tables)

# Query your table
result = conn.execute("SELECT * FROM bronze.trades LIMIT 5").fetchall()
print(result)
