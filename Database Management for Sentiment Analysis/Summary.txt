===============================
📘 Project Summary: Sentiment Analysis on Social Media
===============================

Social media is a dynamic two-way communication platform connecting customers and brands/events. 
With its growing popularity, it has become a powerful source to gauge public sentiment and perception.

Sentiment analysis allows businesses and organizations to extract opinions from social media data. 
This helps in optimizing products, services, and campaigns. Beyond commercial applications, sentiment 
analysis is also valuable in law enforcement, research, education, journalism, and entertainment.

By leveraging Natural Language Processing (NLP), Machine Learning (ML), and text classification techniques, 
social media posts are categorized into Positive, Negative, or Neutral sentiments.

🔍 **Project Scope:**
This project implements a relational database system that supports:
- Efficient storage and organization of high-volume social media data.
- High-performance querying and analytics.
- Cross-platform analysis and real-time sentiment insights.

=======================
📊 Database Design
=======================

🗂️ **Main Dimension Tables:**
1. **Users** – Information about social media users (anonymous identifiers).
2. **Posts** – Raw social media posts (text content + metadata).
3. **Platforms** – List of social media platforms (Twitter, Facebook, etc.).
4. **Hashtags** – Tracks hashtags used in posts.
5. **Keywords** – Stores keywords for sentiment extraction.
6. **Sentiment_Scores** – Stores sentiment analysis results (score: -1 to +1).
7. **Languages** – Supported languages for posts.
8. **Locations** – Geographical origin of each post.

📈 **Fact Tables:**
1. **Post_Analytics** – Aggregates post data (likes, shares, comments, views).
2. **Sentiment_Trends** – Tracks sentiment trends over time (daily sentiment averages by platform).

===========================
🧠 Technologies Used:
===========================
- **SQL Server 2012**
- **NLP & ML-based sentiment classification (conceptual)**
- **ER modeling**
- **Views, Triggers, Stored Procedures, UDFs, Cursors**

This structured backend empowers data-driven sentiment insights, helping stakeholders make smarter decisions.
