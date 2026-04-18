# Test plan template

Reusable shell for each sprint or major feature. We can copy the file, rename it (e.g. `sprint-N-feature-test-plan.md`), then replace all `[bracketed placeholders]`.

---

## 1. Document control

| Field | Value |
|--------|--------|
| **Feature / sprint** | [e.g. Sprint 2 – Vendor profile] |
| **Version** | [e.g. 1.0] |
| **Author** | [Name] |
| **Date** | [YYYY-MM-DD] |
| **Reviewers** | [Names] |

---

## 2. Purpose and scope

**Purpose:** Summarize why this test effort exists and what quality goals matter (functional correctness, security basics, UX, regression).

**In scope:**

- [Bullet: areas to test]

**Out of scope:**

- [Bullet: explicitly not tested this round]

---

## 3. References

| Type | Link or path |
|------|----------------|
| Repository | [URL or path] |
| API / contract | [OpenAPI, README, or `backend/.../routes.py`] |
| Design / wireframes | [Figma, PDF, or “N/A – test vs implemented UI”] |
| Bug tracker | [GitHub Issues / Jira project URL] |
| Related stories / tickets | [Links or IDs] |

---

## 4. Test strategy

| Layer | Approach | Tools |
|--------|-----------|--------|
| API | [e.g. Postman collections, negative cases] | Postman / Insomnia |
| UI | [e.g. manual exploratory + scripted cases] | Browser |
| Automated | [e.g. pytest, lint, E2E – or “none this sprint”] | [Tooling] |

**Test types used this cycle:** [smoke / regression / acceptance / edge / security smoke – check applicable]

---

## 5. Environment

| Item | Value |
|------|--------|
| Frontend URL | [e.g. http://localhost:5173] |
| Backend base URL | [e.g. http://localhost:5002] |
| Database | [e.g. PostgreSQL local, DB name] |
| Branch / commit | [branch name or SHA] |

---

## 6. Entry and exit criteria

**Entry (testing may start when):**

- [e.g. Application builds and runs locally per team README]
- [e.g. Critical endpoints deployed or available on agreed URL]

**Exit (this test cycle complete when):**

- [e.g. All planned cases executed or explicitly blocked with reason]
- [e.g. Defects logged; P0/P1 triaged with team]

---

## 7. Risks and assumptions

| Risk / assumption | Impact | Mitigation |
|-------------------|--------|------------|
| [e.g. UI not wired to API] | [E2E auth blocked] | [Test API and UI separately; document gap] |
| [Add rows as needed] | | |

---

## 8. Test case format (for spreadsheets or tools)

Recommended columns:

`ID | Area (API / UI / Other) | Title | Preconditions | Steps | Test data | Expected result | Actual result | Pass/Fail | Notes | Linked issue`

---

## 9. Defect reporting

File issues in: **[tracker name]**

Each report should include:

1. **Steps to reproduce** (numbered)
2. **Expected result**
3. **Actual result**
4. **Environment** (browser, OS, branch, build)
5. **Screenshots or logs** (if applicable)

---

## 10. Sign-off (optional)

| Role | Name | Date | Comments |
|------|------|------|----------|
| QA | | | |
| Product / mentor | | | |
