## 1. Backend Setup (Xano)

- [x] 1.1 Create `Subject` table in Xano with fields: `id`, `name` (text, unique), `description` (text, optional), `color` (text), `created_at`, `updated_at`
- [x] 1.2 Create Xano API endpoints for subjects: GET list, GET by ID, POST create, PUT update, DELETE
- [x] 1.3 Add nullable `subject_id` field to existing Xano tables (grades, tasks, goals)
- [x] 1.4 Update existing Xano API endpoints for grades/tasks/goals to accept and return `subject_id`

## 2. Subject Service Layer

- [x] 2.1 Create `src/services/subject_service.py` with Xano API client wrapper for all subject operations
- [x] 2.2 Implement subject CRUD functions: `list_subjects`, `create_subject`, `update_subject`, `delete_subject`
- [x] 2.3 Implement duplicate name validation in service layer
- [x] 2.4 Add error handling and retry logic for Xano API rate limits

## 3. Subjects Management Page

- [x] 3.1 Create `src/pages/subjects_page.py` Streamlit page
- [x] 3.2 Implement subject list view with name, description, and color swatch display
- [x] 3.3 Implement "Add Subject" form with name input, description textarea, and color picker from predefined palette
- [x] 3.4 Implement inline editing for existing subjects
- [x] 3.5 Implement delete flow with warning when subject has linked records
- [x] 3.6 Add empty state message when no subjects exist

## 4. Dashboard Subject Integration

- [x] 4.1 Add subject filter dropdown to dashboard (includes "All Subjects" option)
- [x] 4.2 Wire filter to existing dashboard components to filter displayed data by `subject_id`
- [x] 4.3 Implement subject-level performance summary cards (average grade, completion rate, trend)
- [x] 4.4 Apply subject colors to charts and visualizations
- [x] 4.5 Handle "Unassigned" category for records without a subject

## 5. AI Assistant Context Update

- [x] 5.1 Update AI assistant prompt/context to include subject information when available
- [x] 5.2 Enable subject-specific recommendations in the goal assistant

## 6. Polish and Validation

- [x] 6.1 Add form validation feedback for all subject CRUD operations
- [x] 6.2 Test color palette for accessibility (contrast ratios)
- [x] 6.3 Verify backward compatibility: existing records without subjects display correctly
- [x] 6.4 End-to-end test: create subject, assign grades, view filtered dashboard, get AI recommendation (requires running Xano instance)
