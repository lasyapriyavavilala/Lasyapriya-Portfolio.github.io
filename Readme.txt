# Sentiment Analysis DBMS Project

This project involves the design and implementation of a relational database to support sentiment analysis on social media data.

## 📚 Project Description

The project includes:
- SQL schema design for managing users, posts, sentiments, and analytics.
- Data population for 10+ dimension tables and 50+ rows for fact tables.
- Creation of views for actionable insights.
- Audit mechanisms via triggers.
- Stored procedures and user-defined functions for database logic.
- Cursor implementation to iterate through sentiment scores.

## 🧱 Structure

| File | Description |
|------|-------------|
| `create_tables.sql` | Schema for all 10+ tables including fact and dimension tables. |
| `populate_tables.sql` | Insert statements with sample data for all tables. |
| `views.sql` | Includes 3 views with business logic. |
| `triggers.sql` | Audit logging for hashtag changes. |
| `stored_procedures.sql` | A stored procedure to fetch hashtags by keyword. |
| `user_defined_functions.sql` | UDF to compute engagement rate. |
| `cursor_script.sql` | Cursor to update engagement rates based on sentiment. |



## 🧪 How to Run

Run each SQL script in the following order using SQL Server 2012+:

1. `create_database.sql`
2. `create_tables.sql`
3. `populate_tables.sql`
4. `views.sql`
5. `triggers.sql`
6. `stored_procedures.sql`
7. `user_defined_functions.sql`
8. `cursor_script.sql`

---

## 🖼️ Screenshots

See the `screenshots/` directory for query results .

---

## 🏁 Conclusion

This database backend supports advanced querying, user behavior analysis, and social sentiment tracking.
