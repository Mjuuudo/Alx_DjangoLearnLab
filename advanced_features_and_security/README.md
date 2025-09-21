# Managing Permissions and Groups in Django

## Overview

This implementation demonstrates how to set up and manage permissions and groups in a Django application.

## Custom Permissions

The following custom permissions have been added to the `Book` model:

- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing books.
- `can_delete`: Allows deleting books.

## Groups

### Groups and Permissions:

1. **Viewers**:
   - Permissions: `can_view`
2. **Editors**:
   - Permissions: `can_edit`, `can_create`
3. **Admins**:
   - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

## Views

The views enforce permissions using the `@permission_required` decorator. Example views include:

- `view_books`: Requires `can_view` permission.
- `create_book`: Requires `can_create` permission.
- `edit_book`: Requires `can_edit` permission.
- `delete_book`: Requires `can_delete` permission.

## Testing

1. Create test users in the Django admin.
2. Assign users to groups.
3. Verify that permissions are enforced by attempting to access views with different users.

## Notes

- Ensure that users are assigned to appropriate groups for their roles.
- Admin users have full access to all actions.
