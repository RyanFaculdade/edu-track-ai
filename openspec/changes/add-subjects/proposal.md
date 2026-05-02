## Why

The application currently tracks student performance but lacks the ability to organize data by subjects or courses. Without subject management, students cannot categorize their grades, tasks, or goals by discipline, limiting the usefulness of performance analytics and the AI assistant's guidance.

## What Changes

- Add subject creation, editing, and deletion capabilities
- Integrate subjects as a core entity linked to existing performance data
- Update the dashboard to display subject-level metrics and filtering
- Enable the AI assistant to provide subject-specific recommendations

## Capabilities

### New Capabilities

- `subject-management`: CRUD operations for subjects (create, read, update, delete), including subject name, description, and metadata
- `subject-analytics`: Subject-level performance aggregation and filtering on the dashboard

### Modified Capabilities

<!-- No existing specs to modify -->

## Impact

- **Data model**: New Subject entity, relationships with existing performance records
- **Xano backend**: New database table and API endpoints for subjects
- **Frontend (Streamlit)**: New page or section for subject management, updated dashboard with subject filters
- **AI assistant**: Context enriched with subject data for targeted recommendations
