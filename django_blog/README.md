
# 📝 Blog Post Management – Feature Documentation

## 📌 Overview

The **Blog Post Management System** extends the `django_blog` project with full CRUD functionality for blog posts. It enables authenticated users to create, update, and delete posts while allowing all visitors to view published posts.

---

## 🚀 Features

### 🔹 List All Posts

* **URL**: `/posts/`
* **View**: `PostListView`
* **Template**: `post_list.html`
* **Description**: Displays all blog posts ordered by newest first.
* **Permissions**: Public (accessible to all users).

---

### 🔹 View Single Post

* **URL**: `/posts/<id>/`
* **View**: `PostDetailView`
* **Template**: `post_detail.html`
* **Description**: Shows details of a single post (title, content, author, date).
* **Permissions**: Public.

---

### 🔹 Create Post

* **URL**: `/posts/new/`
* **View**: `PostCreateView`
* **Template**: `post_form.html`
* **Description**: Authenticated users can create new posts.
* **Notes**:

  * The **author** is automatically set to the logged-in user.
  * `published_date` is automatically set when the post is created.
* **Permissions**: Login required.

---

### 🔹 Update Post

* **URL**: `/posts/<id>/edit/`
* **View**: `PostUpdateView`
* **Template**: `post_form.html`
* **Description**: Allows authors to edit their own posts.
* **Permissions**:

  * Login required.
  * Only the **author of the post** can edit.

---

### 🔹 Delete Post

* **URL**: `/posts/<id>/delete/`
* **View**: `PostDeleteView`
* **Template**: `post_confirm_delete.html`
* **Description**: Authors can delete their own posts.
* **Permissions**:

  * Login required.
  * Only the **author of the post** can delete.
* **Redirects to**: `/posts/` (Post list) after deletion.

---

## 🔑 Permissions & Data Handling

* Anonymous users → **can only view** posts.
* Authenticated users → **can create** posts.
* Authors → **can edit and delete** their own posts only.
* **Data integrity**:

  * When a user is deleted, all their posts are also deleted (`on_delete=models.CASCADE`).
  * Each post is tied to exactly one author via `ForeignKey`.

---

## 🛠 Quick Usage

1. Register and log in.
2. Go to `/posts/new/` to create a post.
3. Browse `/posts/` to see all posts.
4. Click a post to view details.
5. If you’re the author, you’ll see **Edit** and **Delete** buttons.

---

## 📊 Quick Reference Table

| Feature     | URL                   | View             | Permissions        |
| ----------- | --------------------- | ---------------- | ------------------ |
| List Posts  | `/posts/`             | `PostListView`   | Public             |
| View Post   | `/posts/<id>/`        | `PostDetailView` | Public             |
| Create Post | `/posts/new/`         | `PostCreateView` | Authenticated only |
| Update Post | `/posts/<id>/edit/`   | `PostUpdateView` | Author only        |
| Delete Post | `/posts/<id>/delete/` | `PostDeleteView` | Author only        |

