# Django Blog API

## Base Path
- **/api**

## Authentication
This API uses Basic Authentication.

## Endpoints

### Create an Article

- **URL:** `/article/create/`
- **Method:** `POST`
- **Authentication:** Required
- **Request Body:**
  ```json
  {
    "title": "string",
    "content": "string",
    "author": 1
  }
  ```
- **Response:**
  - **201 Created**
  ```json
  {
    "id": 1,
    "title": "string",
    "content": "string",
    "date_posted": "2024-02-20T12:34:56Z",
    "author": 1
  }
  ```

### Retrieve an Article

- **URL:** `/article/{id}/`
- **Method:** `GET`
- **Authentication:** Required
- **Path Parameters:**
  - `id` (string) **Required** – Article ID
- **Response:**
  - **200 OK**
  ```json
  {
    "id": 1,
    "title": "string",
    "content": "string",
    "date_posted": "2024-02-20T12:34:56Z",
    "author": 1
  }
  ```

### List All Articles

- **URL:** `/articles/`
- **Method:** `GET`
- **Authentication:** Required
- **Response:**
  - **200 OK**
  ```json
  [
    {
      "id": 1,
      "title": "string",
      "content": "string",
      "date_posted": "2024-02-20T12:34:56Z",
      "author": 1
    }
  ]
  ```

## Models

### Article
| Field        | Type    | Required | ReadOnly |
|-------------|--------|----------|----------|
| id          | integer | No       | Yes      |
| title       | string  | Yes      | No       |
| content     | string  | Yes      | No       |
| date_posted | string (date-time) | No | Yes |
| author      | integer | Yes      | No       |

## Security Definitions
- **Basic Authentication**
