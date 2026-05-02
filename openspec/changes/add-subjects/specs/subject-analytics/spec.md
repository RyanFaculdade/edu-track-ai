## ADDED Requirements

### Requirement: Filter dashboard by subject
The system SHALL provide a subject filter control on the dashboard that limits displayed metrics to the selected subject.

#### Scenario: Filter dashboard to a single subject
- **WHEN** user selects a subject from the dashboard filter dropdown
- **THEN** all dashboard metrics, charts, and tables update to show data only for that subject

#### Scenario: Reset filter to all subjects
- **WHEN** user selects the "All Subjects" option in the filter dropdown
- **THEN** the dashboard displays aggregated data across all subjects

#### Scenario: Dashboard with no subjects
- **WHEN** no subjects exist and the dashboard loads
- **THEN** the filter dropdown is hidden and all data displays without subject filtering

### Requirement: Display subject-level performance summary
The system SHALL calculate and display per-subject performance metrics including average grade, completion rate, and trend.

#### Scenario: Show subject summary card
- **WHEN** user views the dashboard with at least one subject having associated records
- **THEN** a summary card displays for each subject showing average grade, task completion rate, and grade trend

#### Scenario: Subject with no data
- **WHEN** a subject exists but has no grades, tasks, or goals linked to it
- **THEN** the subject summary card displays "No data yet" placeholders for all metrics

### Requirement: Color-coded subject visualization
The system SHALL use each subject's assigned color in charts, tables, and UI elements for visual differentiation.

#### Scenario: Color in grade chart
- **WHEN** dashboard renders a grade distribution chart with data from multiple subjects
- **THEN** each subject's data points are rendered using the subject's assigned color

#### Scenario: Color in subject list
- **WHEN** user views the Subjects page
- **THEN** each subject entry displays a color swatch matching the subject's assigned color
