# TR Project Template

## Project Information

Please complete the following before submitting your repository.

**Project Name:**  Vendor Dashboard
**Team Name:**  Team Vendor
**Cohort / Sprint:**  2
**Team Members:**  Katie Baldridge, Lucas Rupp, Hady Elmashhady, Lisa Lopez
                    Lani Love, Arsha Babu Kalleri, Brianna Franklin, Daniel Gallo,
                    Amber Burlet
**Tech Stack:** React + Flask, Python, SQLAlchemy, PostgreSQL

## Project Overview

Provide a short description of your project:

- What problem does it solve?
  An accessible tracker for vendors in the industry to ensure reliable data entry and fraud detection. Removes the need for pen and paper data collection.
  
- Who is the target user?
  Vendors in the industry who are looking for a reliable way to assign work and send invoices.
  
- What core features were completed?
  Login

## Setup & Documentation

### Prerequisites

- Docker and Docker Compose installed on your system
- Git (to clone the repository)

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd TR42-Vendor
   ```

2. **Environment Configuration:**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and set your own `SECRET_KEY` (generate a random string for security)

3. **Build and Run with Docker Compose:**

   ```bash
   docker-compose up --build
   ```

4. **Database Initialization:**
   - The application should automatically create tables on first run
   - If needed, you can manually run the SQL scripts in `backend/resources/ddl/` and `backend/resources/dml/` against the PostgreSQL database

5. **Access the Application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000
   - Database: localhost:5432 (accessible from host for development)

### Development Setup (Without Docker)

If you prefer to run services individually:

#### Backend Setup:

1. Navigate to backend directory:
   ```bash
   cd backend
   ```
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables (copy from .env)
5. Run the backend:
   ```bash
   python run.py
   ```

#### Frontend Setup:

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start development server:
   ```bash
   npm run dev
   ```

#### Database:

- Use the PostgreSQL container from docker-compose, or set up your own PostgreSQL instance

### Required Environment Variables

- `SECRET_KEY`: A secret key for Flask sessions (generate a random string)
- `DATABASE_URL`: PostgreSQL connection string (default: postgresql://postgres:postgres@db:5432/vendor_db)

### API Documentation

- Swagger documentation available at: http://localhost:5000/swagger (if configured)

### Test Credentials

- Default database credentials: postgres/postgres
- Admin user: (configure as needed in your application)

### Deployment

- For production deployment, consider using Docker Compose with appropriate environment variables and secrets management. 

## Notes

List any known limitations, incomplete features, or important technical considerations.

## Development Standards Reminder

All submissions should reflect professional engineering standards:

- Write clean, readable, and modular code  
- Use clear naming conventions  
- Remove unused files, variables, and console logs  
- Follow consistent formatting and linting practices  
- Write meaningful commit messages  
- Keep branches organized and avoid pushing broken code to main  
- Review teammate pull requests respectfully and constructively  

Your repository should be organized, understandable, and demo-ready.

## Intellectual Property Notice

This project was created as part of a Coding Temple Tech Residency. All work produced during the residency is considered the intellectual property of Coding Temple or the sponsoring employer, unless otherwise stated in a signed agreement. By contributing to this project, you acknowledge and agree to these terms.
