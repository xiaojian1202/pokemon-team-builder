# Product Design Document: Project Silph Co. (v1.0)

## 1. Overview & Mission

* **Product:** Project Silph Co.
* **Mission:** To empower competitive Pokémon players to build, analyze, and optimize their teams using data-driven insights.
* **Core Problem:** Team building is often based on guesswork and sifting through forums. There is no single, user-friendly tool that combines a team builder with *live* metagame analytics to help users *immediately* spot their team's statistical flaws and strengths.
* **Target Audience:** "The Competitor"—a player who is active on battle simulators (like Pokémon Showdown) or participates in VGC. They care about optimization, metagame trends, and building the "best" possible team.

## 2. Proposed Core Tech Stack

* **Data Pipeline:** Python (BeautifulSoup/Scrapy), GitHub Actions
* **Database:** PostgreSQL
* **Backend API:** Java (Spring Boot) or Python (Flask/Django)
* **Frontend:** JavaScript (React is recommended)
* **Deployment:** Docker

## 3. Core Product Goals (Agile Epics)

These are the four "must-have" pillars of the MVP.

1.  **Epic 1: The Data Engine:** Establish an automated data pipeline that scrapes, stores, and serves competitive metagame data.
2.  **Epic 2: The User Platform:** Implement a secure user authentication system for saving and managing personal teams.
3.  **Epic 3: The Team Builder:** Create a visual, interactive UI for users to create and customize a 6-Pokémon team.
4.  **Epic 4: The Analytics Engine:** Provide users with *immediate*, actionable feedback on their team's statistical viability.

## 4. MVP Feature Breakdown (User Stories)

### Epic 1: The Data Engine

* **[1.1] Scraper:** As a developer, I need a script that scrapes Smogon stats to get a local, structured copy of the data (Pokemon, usage %, top moves, abilities, items).
* **[1.2] Database:** As a developer, I need a PostgreSQL schema and logic to store the scraped data in a relational database.
* **[1.3] Automation:** As a developer, I want to automate the scraper script (using a GitHub Action) so the database is refreshed daily.

### Epic 2: The User Platform

* **[2.1] Registration:** As a user, I want to create a new account (email/password) so my teams can be saved. (Must include password hashing).
* **[2.2] Login:** As a user, I want to log in to my account so I can access my saved teams. (Must use a secure token like JWT).

### Epic 3: The Team Builder

* **[3.1] View & Select:** As a builder, I want to see a filterable/searchable list of all Pokémon so I can choose them for my team (max 6).
* **[3.2] Customize:** As a builder, I want to customize a team member's moves, ability, and item, with suggestions from the scraped data.
* **[3.3] Save Team:** As a logged-in user, I want to click a 'Save' button to save my current customized team to my profile.

### Epic 4: The Analytics Engine

* **[4.1] Type Weakness:** As a builder, I want to see a real-time chart of my team's collective type weaknesses as I add/remove Pokémon.
* **[4.2] Metagame Suggestions:** As a builder, I want to see the top-used moves/items for a Pokémon when I add it to my team.

## 5. Future Enhancements (Backlog)

* Team Sharing (generate a unique URL).
* Advanced Analytics (Speed Tier calculator, Threat List).
* Import/Export from Pokémon Showdown text format.
* Team Ratings (give the team a "Metagame Score").
