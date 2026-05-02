## Why

The edu-track system needs a `subjects` table to represent academic subjects (disciplinas/materias) that students are enrolled in. Currently there is no structured way to store subject information linked to users.

## What Changes

- Create the `subjects` table schema in Xano with the defined fields
- Establish the relationship between subjects and authenticated users via `user_id`

## Capabilities

### New Capabilities

- `subjects-schema`: Database schema definition for the subjects table with fields: id, name, teacher, hours, user_id

### Modified Capabilities

<!-- No existing capabilities are being modified -->

## Impact

- Xano database: new `subjects` table
- The `user_id` field references the Xano auth `user/users` table (foreign key)
