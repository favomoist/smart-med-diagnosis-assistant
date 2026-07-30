# User Stories & MoSCoW Prioritization

Format: `US-##: As a <persona>, I want to <action>, so that <benefit>.`
Copy each story title into a GitHub Issue in your repo, and add the MoSCoW label shown.

Personas: **Patient**, **Clinician**, **Caregiver**, **Admin**

| # | User Story | Persona | MoSCoW |
|---|---|---|---|
| US-01 | As a Patient, I want to create an account and log in securely, so that my health data is protected. | Patient | Must |
| US-02 | As a Patient, I want to enter my symptoms through a guided questionnaire, so that I don't miss important details. | Patient | Must |
| US-03 | As a Patient, I want to see an urgency level (emergency/urgent/self-care) after my symptom check, so that I know how quickly to act. | Patient | Must |
| US-04 | As a Patient, I want to see a list of possible conditions with confidence levels, so that I understand what might be causing my symptoms. | Patient | Must |
| US-05 | As a Patient, I want a clear disclaimer that this isn't a medical diagnosis, so that I don't misuse the tool. | Patient | Must |
| US-06 | As a Patient, I want to view my past symptom checks in a history/timeline, so that I can track changes over time. | Patient | Should |
| US-07 | As a Patient, I want to export or share a summary of my symptoms with a doctor, so that my appointment is more efficient. | Patient | Must |
| US-08 | As a Patient, I want to receive a warning immediately if my symptoms suggest an emergency, so that I can seek immediate care. | Patient | Must |
| US-09 | As a Patient, I want to reset my password, so that I can regain access if I forget it. | Patient | Should |
| US-10 | As a Patient, I want to update my profile (age, sex, known conditions), so that triage results are more accurate. | Patient | Should |
| US-11 | As a Caregiver, I want to create and manage a profile for a dependent (e.g., a parent or child), so that I can log their symptoms too. | Caregiver | Should |
| US-12 | As a Caregiver, I want to switch between profiles I manage, so that I can quickly check on different people. | Caregiver | Could |
| US-13 | As a Caregiver, I want to receive a notification if a dependent's symptom check flags an emergency, so that I can respond quickly. | Caregiver | Should |
| US-14 | As a Clinician, I want to view a structured summary of a patient's reported symptoms and history, so that I can prepare for the consultation. | Clinician | Must |
| US-15 | As a Clinician, I want to see which symptoms triggered a red-flag/emergency classification, so that I can validate the system's reasoning. | Clinician | Should |
| US-16 | As a Clinician, I want to add my own notes to a patient's shared summary, so that I can document my assessment. | Clinician | Could |
| US-17 | As a Clinician, I want role-based access so that I only see summaries shared with me, so that patient privacy is respected. | Clinician | Must |
| US-18 | As an Admin, I want to manage the symptom-condition knowledge base (add/edit/remove entries), so that the triage engine stays accurate. | Admin | Must |
| US-19 | As an Admin, I want to view system usage analytics (active users, completion rates), so that I can measure adoption. | Admin | Should |
| US-20 | As an Admin, I want to manage user accounts and roles, so that I can moderate access to the platform. | Admin | Should |
| US-21 | As an Admin, I want to view system health/monitoring dashboards, so that I can detect downtime or errors quickly. | Admin | Could |
| US-22 | As a Patient, I want the app to work on both web and mobile, so that I can access it from any device. | Patient | Should |
| US-23 | As a Patient, I want the interface to support multiple languages, so that non-English speakers can use it too. | Patient | Won't (this phase) |
| US-24 | As a Patient, I want reminders/follow-up check-ins for ongoing symptoms, so that I don't forget to reassess my condition. | Patient | Could |
| US-25 | As a Developer/Admin, I want the backend containerized with Docker, so that local development and deployment are consistent. | Admin | Must |

## MoSCoW Summary

| Priority | Count | Stories |
|---|---|---|
| **Must Have** | 10 | US-01, 02, 03, 04, 05, 07, 08, 14, 17, 18, 25 *(11 — core MVP)* |
| **Should Have** | 8 | US-06, 09, 10, 11, 13, 15, 19, 20, 22 |
| **Could Have** | 4 | US-12, 16, 21, 24 |
| **Won't Have (this phase)** | 1 | US-23 |

> Note: adjust counts/labels as you finalize scope — the table above is a starting point, not a locked spec.

## How to add these to GitHub Projects / Issues
1. In your repo, go to **Issues → New Issue** for each story (or use the GitHub CLI / bulk import via a CSV in GitHub Projects).
2. Use the story text as the Issue title, and add labels: `must`, `should`, `could`, `wont`, plus a persona label (`patient`, `clinician`, `caregiver`, `admin`).
3. Add all issues to a **GitHub Project (board)** with columns: `Backlog`, `To Do`, `In Progress`, `Done`.
