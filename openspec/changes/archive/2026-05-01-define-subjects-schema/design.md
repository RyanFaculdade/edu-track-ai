## Context

The edu-track system currently lacks a structured way to store academic subject information. This change introduces a `subjects` table in Xano to represent subjects (disciplinas/materias) that users are enrolled in.

## Goals / Non-Goals

**Goals:**
- Define the `subjects` table schema with `id` and `user_id` as required fields, and `name`, `teacher`, `hours` as optional
- Establish a foreign key relationship between `subjects` and the Xano auth `user/users` table
- Ensure the schema supports future API and frontend work

**Non-Goals:**
- No API endpoints will be created in this change
- No CRUD operations or service layer
- No frontend/UI components
- No validation or business logic rules beyond the schema itself

## Decisions

1. **Field naming**: `user_id` follows the convention of suffixing FK references with `_id`
2. **Hours as integer**: `hours` stores total workload as an integer (e.g., 60 for a 60-hour subject), avoiding time-format complexity
3. **Xano auth table reference**: `user_id` references Xano's built-in auth `user/users` table, not a custom users table

## Risks / Trade-offs

- [No teacher email/contact field] → Only teacher name is stored. If contact info is needed later, a new field must be added.
- [No subject status] → Subjects have no active/archived state. All records are implicitly active.
