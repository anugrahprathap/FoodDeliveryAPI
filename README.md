


# API Usage Instructions

This README provides instructions on how to call the API with the given parameters.

## API Endpoint

The API endpoint for accessing the delivery cost calculation is:

```
https://fooddeliveryapi-ocw8.onrender.com/api/delivery-cost/
```

## Setup Guide

To use the API, follow these setup steps:

1. **Ensure Python and Django are Installed**:
   Make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/). Additionally, install Django by running:
   ```
   pip install django
   ```

2. **Install Required Packages**:
   Install the required packages for the project by running:
   ```
   pip install djangorestframework
   ```

3. **Make Migrations**:
   Apply database migrations to set up the database schema by running:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Django Development Server**:
   Start the Django development server by running:
   ```
   python manage.py runserver
   ```

5. **Access the API Endpoint**:
   Once the server is running, you can access the API endpoint at the following URL:
   ```
   http://localhost:8000/api/delivery-cost/
   ```

## Request Parameters

The API requires the following parameters to calculate the delivery cost:

- `organization_id`: The ID of the organization.
- `zone`: The delivery zone.
- `total_distance`: The total distance in kilometers.
- `item_id`: The ID of the item.

Here are the parameters for the request:

```json
{
    "organization_id": "005",
    "zone": "central",
    "total_distance": 12,
    "item_id": 3
}
```

## Item IDs
- Items 1 and 2 are for perishable items.
- Items 3 and 4 are for non-perishable items.

## Response

Upon making the API call, you will receive a response containing the total delivery cost calculated based on the provided parameters.

Example response:

```json
{
    "total_price": 30.0
}
```

The `total_price` field in the response represents the total delivery cost.

---

