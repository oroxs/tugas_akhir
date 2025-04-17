class DataUser:
    users = [
        ('Jhon','Doe','27442')
        ]
    negative_users = [
        ("", "Doe", "321222", "Error: First Name is required"),
        ("Jone", "", "321222", "Error: Last Name is required"),
        ("Jone", "Doe", "", "Error: Postal Code is required"),
        ]