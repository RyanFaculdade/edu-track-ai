## ADDED Requirements

### Requirement: Create subject
The system SHALL allow users to create a new subject with a name, optional description, and a color from a predefined palette.

#### Scenario: Successful subject creation
- **WHEN** user provides a valid subject name and selects a color
- **THEN** the system creates the subject in Xano and displays a success confirmation

#### Scenario: Duplicate subject name rejection
- **WHEN** user attempts to create a subject with a name that already exists
- **THEN** the system displays an error message and does not create the subject

#### Scenario: Missing name validation
- **WHEN** user attempts to create a subject without providing a name
- **THEN** the system displays a validation error and does not submit the form

### Requirement: View subjects list
The system SHALL display a list of all subjects with their name, description, and color indicator.

#### Scenario: Display subjects list
- **WHEN** user navigates to the Subjects page
- **THEN** the system displays all subjects with their name, description, and color

#### Scenario: Empty subjects list
- **WHEN** no subjects have been created
- **THEN** the system displays a message prompting the user to create their first subject

### Requirement: Edit subject
The system SHALL allow users to modify the name, description, and color of an existing subject.

#### Scenario: Successful subject update
- **WHEN** user edits subject fields and saves changes
- **THEN** the system updates the subject in Xano and reflects the changes in the list

#### Scenario: Duplicate name on edit
- **WHEN** user changes a subject name to match an existing subject name
- **THEN** the system displays an error and does not save the change

### Requirement: Delete subject
The system SHALL allow users to delete a subject, with a warning if performance records are linked to it.

#### Scenario: Delete subject with no linked records
- **WHEN** user confirms deletion of a subject that has no linked grades, tasks, or goals
- **THEN** the system removes the subject from Xano and updates the list

#### Scenario: Delete subject with linked records
- **WHEN** user attempts to delete a subject that has linked grades, tasks, or goals
- **THEN** the system displays a warning listing affected records and requires explicit confirmation before deletion

### Requirement: Assign subject to performance records
The system SHALL allow users to associate grades, tasks, and goals with a subject via a subject selector dropdown.

#### Scenario: Assign subject to a new grade
- **WHEN** user creates a new grade record and selects a subject from the dropdown
- **THEN** the grade is saved with the selected `subject_id` reference in Xano

#### Scenario: Leave subject unassigned
- **WHEN** user creates a new grade record without selecting a subject
- **THEN** the grade is saved with a null `subject_id` and appears in the "Unassigned" category
