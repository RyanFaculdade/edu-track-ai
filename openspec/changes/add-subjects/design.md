## Context

The Student Performance Tracker currently operates without a subject/discipline abstraction. All performance data is treated as a single pool, which limits analytical depth and personalization. The app uses Streamlit for the frontend and Xano (no-code backend) with REST APIs for data persistence.

## Goals / Non-Goals

**Goals:**
- Introduce subjects as a first-class entity with full CRUD support
- Link existing and new performance records to subjects
- Enable subject-filtered views on the dashboard
- Provide subject context to the AI goal assistant
- Maintain backward compatibility with existing data

**Non-Goals:**
- Migration of legacy data (existing records will remain unassigned initially)
- Complex subject hierarchies (e.g., sub-subjects, prerequisites)
- Teacher or class management features

## Decisions

1. **Xano as subject data store**: Use Xano's no-code database to create a `Subject` table with fields: `id`, `name`, `description`, `color` (for UI), `created_at`, `updated_at`. This aligns with the existing backend pattern and avoids introducing new infrastructure.

2. **Subject reference on performance records**: Add a nullable `subject_id` field to existing Xano tables (grades, tasks, goals). Nullable ensures backward compatibility — existing records without a subject assignment continue to work.

3. **Streamlit page structure**: Add a new dedicated page `Subjects` (via `pages/subjects_page.py`) for subject management, keeping the existing dashboard clean. The dashboard gains a subject filter dropdown at the top.

4. **Color-coded subjects**: Each subject gets an assigned color for visual differentiation in charts and tables. Users pick from a predefined palette to ensure accessibility and contrast.

5. **API abstraction layer**: Create a `src/services/subject_service.py` module that wraps all Xano API calls for subjects, following the existing service pattern in the codebase.

## Risks / Trade-offs

- [Xano API rate limits] → Batch subject fetches and cache results in session state; implement retry logic
- [Orphaned subject references] → Xano foreign key constraints or soft-delete subjects with a warning if referenced records exist
- [Dashboard performance degradation with many subjects] → Limit filter dropdown to active subjects; paginate if subject count grows large
- [UI complexity for color selection] → Use a fixed palette of accessible colors rather than free-form color picker to reduce cognitive load
