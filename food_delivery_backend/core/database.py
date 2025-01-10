import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase app
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com'
})

# Example function to update order status
def update_order_status(order_id, status):
    ref = db.reference(f"orders/{order_id}")
    ref.update({"status": status})
