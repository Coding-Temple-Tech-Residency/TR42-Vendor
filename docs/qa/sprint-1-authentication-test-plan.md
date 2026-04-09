# Sprint 1 – Authentication test plan

**Project:** TR42-Vendor (local path: repository root)  
**Based on:** `docs/qa/test-plan-template.md`  
**Fill in:** Document control table (author, date, reviewer), bug tracker URL, and environment if your team differs.

---

## 1. Document control

| Field | Value |
|--------|--------|
| **Feature / sprint** | Sprint 1 – Environment setup & authentication QA |
| **Version** | 1.0 |
| **Author** | *[Your name]* |
| **Date** | *[YYYY-MM-DD]* |
| **Reviewers** | *[Mentor / lead]* |

---

## 2. Purpose and scope

**Purpose:** Validate authentication-related behavior for Sprint 1: API contracts for user login and registration, and manual behavior of login/registration UI, plus clear feedback on requirement clarity and testability.

**In scope:**

- Backend: `POST /users/login`, `POST /users/` (user creation / registration at API level)
- Frontend routes: `/register`, `/profile-setup`, `/success`, `/login` (manual validation, navigation, client-side rules)
- Negative and edge cases as listed in section 11
- Defects filed to team bug tracker with standard format

**Out of scope (unless team expands scope):**

- Full E2E automation (no Jest/Cypress suite in repo for auth at time of plan)
- Non-auth endpoints (vendors, addresses, etc.) except where they block login/register
- Production / staging deployment (not defined in repo)

---

## 3. References

| Type | Link or path |
|------|----------------|
| Repository | TR42-Vendor (this repo) |
| User routes | `backend/app/blueprints/user/controller/routes.py` |
| Login / create logic | `backend/app/blueprints/user/services/user_service.py` |
| User model | `backend/app/blueprints/user/model.py` |
| User table DDL | `backend/resources/ddl/create_tables.sql` (`"user"` table) |
| Frontend auth UI | `frontend/src/features/auth/`, `frontend/src/LoginPageTest.tsx`, `frontend/src/App.tsx` |
| Client validation | `frontend/src/features/auth/utils/authValidation.ts` |
| Bug tracker | *[GitHub Issues URL for your team repo]* |
| Wireframes | *Not present in repo – cite external Figma/link or “test vs implemented UI”* |

**Backend URL prefix:** Flask registers user blueprint at `/users` (see `backend/app/__init__.py`).

---

## 4. Test strategy

| Layer | Approach | Tools |
|--------|-----------|--------|
| API | Request happy path, validation failures, auth failures; record status codes and bodies | Postman or Insomnia |
| UI | Manual scripted cases + light exploration on register flow and login page | Chromium/Firefox/Safari as required |
| Automated | Optional: `npm run lint` (frontend); `pytest` exists under `backend/app/tests/` for other modules—not auth-specific | ESLint, pytest |

---

## 5. Environment

| Item | Value (default from repo) |
|------|----------------------------|
| Frontend | Vite dev server (commonly `http://localhost:5173` – confirm in terminal after `npm run dev`) |
| Backend | `http://localhost:5002` (`backend/run.py`) |
| Database | PostgreSQL; `backend/app/config.py` uses `postgresql://postgres:postgres@127.0.0.1:5432/mydb` unless changed—**must match your local DB** |
| Schema | Apply `backend/resources/ddl/create_tables.sql` before API tests that persist users |

---

## 6. Entry and exit criteria

**Entry**

- PostgreSQL running; schema applied; backend starts without fatal errors
- Frontend installs with `npm install` and `npm run dev` serves the app
- Postman/Insomnia installed

**Exit**

- All test cases in section 11 executed or marked **Blocked** with reason
- Results recorded in test log (spreadsheet or tool)
- Failures logged as issues (steps, expected, actual)
- Short written note: requirements clarity & testability (section 12)

---

## 7. Risks and assumptions

| Risk / assumption | Impact | Mitigation |
|-------------------|--------|------------|
| Registration UI saves to `localStorage` and does not call `POST /users/` | UI “register” ≠ API user creation | Test API with Postman; test UI separately; document integration gap if expected |
| Login page (`LoginPageTest.tsx`) may not submit to API | No true E2E login via UI | Test login via Postman; UI cases focus on form behavior and labels |
| Login API expects **username**, login UI placeholder says **Email** | Confusion or wrong manual tests | Align test data; file bug/UX issue if product should match |
| No dedicated **logout** HTTP route in user blueprint | “Logout” is client-side token discard or not implemented | Define expected behavior with team; test what exists |
| `UserRepository.create` default `type` may not match DB enum | Create user may fail with invalid enum | Use explicit `type`: `operator`, `vendor`, or `contractor` in API payloads |

---

## 8. API quick reference (for Postman)

| Method | Path | Body (JSON) | Notes |
|--------|------|-------------|--------|
| POST | `/users/login` | `{"username": "<string>", "password": "<string>"}` | Success: 200 + `token` and user fields (see service) |
| POST | `/users/` | User fields per model/DB: e.g. `username`, `email`, `password` (hashed server-side), `first_name`, `last_name`, `type`, `created_by`, `updated_by`, etc. | Success: 201; align with DDL NOT NULL columns |

Exact JSON for create should match what `User` / `UserRepository.create` expect and what the database allows (see `create_tables.sql`).

---

## 9. Requirement clarity & testability (Sprint deliverable)

Use this subsection as your written feedback to the team/mentor.

**Clarity**

- *[After review, state whether auth requirements are clear, ambiguous, or only clear from code.]*
- Note: separation between **vendor registration** (`/vendors/register`) and **user** creation (`POST /users/`) if both exist in the product.

**Testability**

- **API:** Testable with Postman once DB and schema are up; cases are deterministic if data is controlled.
- **UI:** Testable for validation messages, navigation, and accessibility basics; full E2E auth depends on frontend calling the backend and defined logout behavior.

---

## 10. Test log

Maintain a spreadsheet (or copy the table below) with columns:  
`ID | Area | Title | Steps | Test data | Expected | Actual | Pass/Fail | Notes | Issue #`

---

## 11. Test cases (checklist)

### API – User registration (`POST /users/`)

| ID | Title | Summary |
|----|--------|---------|
| A-01 | Register happy path | Valid JSON; user persisted; 201; password not returned in plain text in response |
| A-02 | Missing required field | Omit one NOT NULL field (e.g. `email`, `username`, `first_name`); document status/body |
| A-03 | Duplicate username | Create same `username` twice |
| A-04 | Duplicate email | Create same `email` twice |
| A-05 | Invalid `type` | Value outside `operator` / `vendor` / `contractor` |
| A-06 | Edge – very short password | e.g. 1 character; note policy if none |
| A-07 | Edge – invalid email format | Malformed `email` string |
| A-08 | Edge – special characters | Unicode, quotes, `<script>`-like strings in fields (document handling) |

### API – Login (`POST /users/login`)

| ID | Title | Summary |
|----|--------|---------|
| A-10 | Login happy path | Valid `username` + password; 200; `token` present |
| A-11 | Wrong password | Valid user, bad password |
| A-12 | Unknown username | Nonexistent user |
| A-13 | Missing username or password | Empty or omitted keys |
| A-14 | Edge – empty JSON body | Malformed or `{}` |
| A-15 | Edge – wrong `Content-Type` | e.g. form-urlencoded instead of JSON |

### API / product – Logout

| ID | Title | Summary |
|----|--------|---------|
| A-20 | Logout behavior | If no server endpoint: document expected client behavior; verify or mark N/A |

### UI – Registration flow

| ID | Title | Summary |
|----|--------|---------|
| U-01 | Register step 1 valid | All fields valid → navigates to `/profile-setup`; data survives refresh if specified by design |
| U-02 | Register invalid | Missing/invalid fields per `authValidation.ts`; errors shown; no navigation |
| U-03 | Edge – short password | Below minimum if defined |
| U-04 | Edge – invalid email | Bad format |
| U-05 | Edge – special characters | Names/username/password |
| U-06 | Profile setup valid | Completes to `/success`; `registerData` cleared per implementation |
| U-07 | Profile setup invalid | Required company/address fields; errors shown |
| U-08 | Deep link `/profile-setup` without step 1 | Expected redirect or error |

### UI – Login

| ID | Title | Summary |
|----|--------|---------|
| U-10 | Login page layout | Fields, labels, button behavior |
| U-11 | Login submit | Actual behavior (API call or none); document as pass/fail vs expectation |

### UI – Logout

| ID | Title | Summary |
|----|--------|---------|
| U-15 | Logout | If UI control exists: session/token cleared and redirect; else N/A |

---

## 12. Defect template (reminder)

1. Steps to reproduce  
2. Expected result  
3. Actual result  
4. Environment + screenshots/logs  
5. Link from test log row to issue number  

---

## 13. Sign-off (optional)

| Role | Name | Date |
|------|------|------|
| QA | | |
| Mentor | | |
