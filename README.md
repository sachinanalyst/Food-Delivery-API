# Food Delivery Backend API

This repository contains a robust Food Delivery Backend API built using **Django** and integrated with **Firebase** for authentication and database management. The API supports features like user authentication, restaurant management, menu handling, order placement, and real-time order tracking.

## Features
- **Authentication & Authorization**
  - Email/password login and Google login using Firebase Authentication.
  - Role-based access control (Admin and User).
- **Restaurant Management**
  - Admins can add, update, and delete restaurants and menu items.
- **Order Handling**
  - Users can place orders, view order history, and track order status in real time.
- **Real-Time Updates**
  - Real-time order tracking using Firebase Realtime Database or Firestore.
- **API Documentation**
  - Swagger UI for API exploration.

---

## Prerequisites

1. **Python**: Version 3.8+
2. **Django**: Installed via `pip install django`
3. **Firebase Account**: To configure Firebase Authentication and database.
4. **Virtual Environment** (Optional but recommended): To isolate dependencies.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sachinanalyst/Food-Delivery-API.git
cd food_delivery_backend
```

### 2. Set Up Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Firebase
1. Go to [Firebase Console](https://console.firebase.google.com/).
2. Create a Firebase project.
3. Download the **Service Account Key JSON** (Firebase Admin SDK).
4. Place the downloaded JSON file in the project root as `serviceAccountKey.json`.
5. Update `settings.py`:
   ```python
   FIREBASE_CREDENTIALS = 'path/to/serviceAccountKey.json'
   ```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 7. Run the Server
```bash
python manage.py runserver
```
By default, the server will be available at `http://127.0.0.1:8000/`.

---

## Testing the API

### Using Postman or CURL
1. **Authentication**
   - Obtain a Firebase JWT token via Firebase Authentication.
   - Use the token in the `Authorization` header:
     ```
     Authorization: Bearer <firebase_token>
     ```

2. **Endpoints**
   - **List Restaurants**: `GET /api/restaurants/`
   - **Add Restaurant**: `POST /api/restaurants/` (Admin only)
   - **Place Order**: `POST /api/orders/`
   - **Order History**: `GET /api/orders/history/`

### Running Unit Tests

1. Run all tests:
   ```bash
   python manage.py test
   ```

2. Example unit test for authentication:
   ```python
   from rest_framework.test import APIClient

   class FirebaseAuthTests(TestCase):
       def setUp(self):
           self.client = APIClient()

       def test_authentication(self):
           response = self.client.get('/api/restaurants/')
           self.assertEqual(response.status_code, 200)
   ```

---

## API Documentation

### Swagger UI
1. Install Swagger with `drf-yasg`:
   ```bash
   pip install drf-yasg
   ```

2. Access Swagger UI:
   - Navigate to `http://127.0.0.1:8000/swagger/` for interactive API documentation.

---

## Deployment

1. Deploy the project on any platform like **Heroku**, **AWS**, or **Render**.
2. Make sure to:
   - Configure Firebase credentials on the platform.
   - Use environment variables for sensitive data (e.g., Firebase credentials).


