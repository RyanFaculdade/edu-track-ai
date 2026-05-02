## ADDED Requirements

### Requirement: Subjects table schema
The Xano database SHALL contain a `subjects` table with the following fields:
- `id`: auto-generated unique identifier (primary key)
- `name`: text, optional — the subject name
- `teacher`: text, optional — the teacher/instructor name
- `hours`: integer, optional — total workload hours
- `user_id`: foreign key, required — references the Xano auth `user/users` table

#### Scenario: Table has all fields
- **WHEN** the `subjects` table is inspected in Xano
- **THEN** it contains fields `id`, `name`, `teacher`, `hours`, and `user_id` with the correct types

#### Scenario: ID is auto-generated
- **WHEN** a new subject record is created without specifying `id`
- **THEN** the system automatically generates a unique `id` value

#### Scenario: Name is optional
- **WHEN** a subject record is created without a `name`
- **THEN** the operation succeeds and `name` is stored as null

#### Scenario: Teacher is optional
- **WHEN** a subject record is created without a `teacher`
- **THEN** the operation succeeds and `teacher` is stored as null

#### Scenario: Hours is optional and integer when provided
- **WHEN** a subject record is created without `hours`
- **THEN** the operation succeeds and `hours` is stored as null

#### Scenario: User_id references auth table
- **WHEN** a subject record is created with a `user_id`
- **THEN** the value must reference a valid record in the Xano `user/users` auth table
