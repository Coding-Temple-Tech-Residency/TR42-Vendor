# Authentication test plan

**Project:** TR42-Vendor (local path: repository root)  
**Based on:** `docs/qa/test-plan-template.md`  
**Fill in:** Document control table (author, date, reviewer), bug tracker URL, and environment if your team differs.

**Revision 1.1 (sync with current repo):** User API is under **`/api/users`**; login accepts **`email` + `password`** (not username). Login UI (`LoginForm`) calls **`POST /api/users/login`** and navigates to **`/vendor/dashboard`** on success. Auth routes live under **`/vendor/...`** via `AppRouter`. **`ForgotPasswordPage`** exists at `/vendor/forgot-password`. Registration step 1 still uses **`localStorage`** then **`/vendor/profile-setup`**. Backend default port in `run.py` is **5001**. Re-review after future merges.

---

## 1. Document control

| Field | Value |
|--------|--------|
| **Feature / sprint** | Sprint 1 – Environment setup & authentication QA |
| **Version** | 1.1 |
| **Author** | *[Your name]* |
| **Date** | *[YYYY-MM-DD]* |
| **Reviewers** | *[Mentor / lead]* |

---

## 2. Purpose and scope

**Purpose:** Validate authentication-related behavior for Sprint 1: API contracts for user login and registration, and manual behavior of login/registration UI, plus clear feedback on requirement clarity and testability.

**In scope:**

- Backend: `POST /api/users/login`, `POST /api/users/` (user creation / registration at API level)
- Frontend routes (manual): `/vendor/register`, `/vendor/profile-setup`, `/vendor/success`, `/vendor/login`, `/vendor/forgot-password`
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
| User routes | `backend/app/blueprints/user/controller/user_routes.py` |
| Login / create logic | `backend/app/blueprints/user/services/user_services.py` |
| User model | `backend/app/blueprints/user/model.py` |
| User table DDL | `backend/resources/ddl/create_tables.sql` (`"user"` table) |
| Frontend routing | `frontend/src/routes/AppRouter.tsx`, `frontend/src/App.tsx` |
| Login form (API integration) | `frontend/src/features/auth/forms/LoginForm.tsx` |
| Frontend auth UI | `frontend/src/features/auth/` |
| Client validation | `frontend/src/features/auth/utils/authValidation.ts` |
| Bug tracker | *[GitHub Issues URL for your team repo]* |
| Wireframes | *Not present in repo – cite external Figma/link or “test vs implemented UI”* |

**Backend URL prefix:** Flask registers the user blueprint at **`/api/users`** (see `backend/app/__init__.py`).

---

## 4. Test strategy

| Layer | Approach | Tools |
|--------|-----------|--------|
| API | Request happy path, validation failures, auth failures; record status codes and bodies | Postman or Insomnia |
| UI | Manual scripted cases + light exploration on register flow and login page | Chromium/Firefox/Safari as required |
| Automated | Optional: `npm run lint` (frontend); `pytest` includes `backend/app/tests/user/` | ESLint, pytest |

---

## 5. Environment

| Item | Value (default from repo) |
|------|----------------------------|
| Frontend | Vite dev server: `http://localhost:5173` (`frontend/vite.config.ts`; proxies **`/api`** to the backend) |
| Backend | `http://localhost:5001` (`backend/run.py`) |
| Docker note | Vite proxy `target` may be `http://backend:5001` (Compose service name). For **local** backend on the host, ensure proxy target matches where Flask listens (team may use env override). |
| Database | PostgreSQL—**match** `DATABASE_URL` / app config your team uses |
| Schema | Apply `backend/resources/ddl/create_tables.sql` (or team migrations) before API tests that persist users |

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
| Registration UI saves to `localStorage` and does not call `POST /api/users/` | UI “register” ≠ API user creation | Test API with Postman; test UI separately; document integration gap if expected |
| Login UI calls **`POST /api/users/login`** with **email** + password | E2E login is now testable when backend + proxy are up | Use browser Network tab + Postman; confirm proxy reaches Flask |
| **Forgot password** page may be UI-only until backend exists | Flow may be incomplete | Test links/navigation; document blocked cases |
| No dedicated **logout** HTTP route | “Logout” is often client-side token discard | Define expected behavior with team; test what exists |
| Create-user payload must match **`user_schema`** / DB | Validation errors or 400/500 | Use `POST /api/users/` with valid schema; read `user_schema` and tests under `app/tests/user/` |

---

## 8. API quick reference (for Postman)

Base URL examples:

- Direct to Flask: `http://localhost:5001`
- Through Vite (browser): requests to **`/api/...`** on port **5173** are proxied to the backend (see `vite.config.ts`).

| Method | Path | Body (JSON) | Notes |
|--------|------|-------------|--------|
| POST | `/api/users/login` | `{"email": "<string>", "password": "<string>"}` | Success: 200 + `token` and user fields (see `UserService.login`) |
| POST | `/api/users/` | Per **`user_schema.load`** — see routes/tests | Success: 201; validation errors may return 400 with `errors` |

Exact JSON for create should match `user_schema` and `UserService.create_user` (see `user_routes.py` and `backend/app/tests/user/`).

---

## 9. Requirement clarity & testability (Sprint deliverable)

Use this subsection as your written feedback to the team/mentor.

**Clarity**

- *[After review, state whether auth requirements are clear, ambiguous, or only clear from code.]*
- Note: separation between **vendor registration** (`/vendors/register`) and **user** creation (`POST /users/`) if both exist in the product.

**Testability**

- **API:** Testable with Postman once DB and schema are up; cases are deterministic if data is controlled.
- **UI:** Login is testable end-to-end **when** dev server + backend are running and the Vite proxy reaches Flask. Registration flow remains testable for client validation + navigation; API registration is still separate unless the UI is wired to `POST /api/users/`.

---

## 10. Test log

Maintain a spreadsheet (or copy the table below) with columns:  
`ID | Area | Title | Steps | Test data | Expected | Actual | Pass/Fail | Notes | Issue #`

---

## 11. Test cases (checklist)

### API – User registration (`POST /api/users/`)

| ID | Title | Summary |
|----|--------|---------|
| A-01 | Register happy path | Valid JSON; user persisted; 201; password not returned in plain text in response |
| A-02 | Missing required field | Omit required field per schema; document status/body (`errors` or `error`) |
| A-03 | Duplicate username | Create same `username` twice (if unique constraint) |
| A-04 | Duplicate email | Create same `email` twice |
| A-05 | Invalid `user_type` (or equivalent) | Value outside allowed enum |
| A-06 | Edge – very short password | e.g. 1 character; note policy if none |
| A-07 | Edge – invalid email format | Malformed `email` string |
| A-08 | Edge – special characters | Unicode, quotes, `<script>`-like strings in fields (document handling) |

### API – Login (`POST /api/users/login`)

| ID | Title | Summary |
|----|--------|---------|
| A-10 | Login happy path | Valid **`email`** + password; 200; `token` present |
| A-11 | Wrong password | Valid user, bad password |
| A-12 | Unknown email | Nonexistent email |
| A-13 | Missing email or password | Empty or omitted keys |
| A-14 | Edge – empty JSON body | No body → 400 `No input data provided` (see route) |
| A-15 | Edge – wrong `Content-Type` | e.g. form-urlencoded instead of JSON |

### API / product – Logout

| ID | Title | Summary |
|----|--------|---------|
| A-20 | Logout behavior | If no server endpoint: document expected client behavior; verify or mark N/A |

### UI – Registration flow

| ID | Title | Summary |
|----|--------|---------|
| U-01 | Register step 1 valid | All fields valid → navigates to **`/vendor/profile-setup`**; `registerData` in `localStorage` |
| U-02 | Register invalid | Missing/invalid fields per `authValidation.ts`; errors shown; no navigation |
| U-03 | Edge – short password | Below minimum if defined |
| U-04 | Edge – invalid email | Bad format |
| U-05 | Edge – special characters | Names/username/password |
| U-06 | Profile setup valid | Completes to **`/vendor/success`**; `registerData` cleared per implementation |
| U-07 | Profile setup invalid | Required company/address fields; errors shown |
| U-08 | Deep link **`/vendor/profile-setup`** without step 1 | Expected empty state or error |

### UI – Login

| ID | Title | Summary |
|----|--------|---------|
| U-10 | Login page layout | Fields, labels, loading state, error display |
| U-11 | Login submit – success | Valid credentials → **`/vendor/dashboard`** (see `LoginForm`); token in response (verify storage if implemented) |
| U-12 | Login submit – API error | Invalid credentials → error message; no navigation |

### UI – Forgot password

| ID | Title | Summary |
|----|--------|---------|
| U-13 | Forgot password page | Open **`/vendor/forgot-password`**; links, form behavior, any API wiring |

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
