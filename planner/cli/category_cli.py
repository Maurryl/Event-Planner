

from models.category import Category
from planner.cli.database_setup import Session

def category_menu():
    session = Session()
    while True:
        print("\nCategory Management")
        print("1. Create Category")
        print("2. Delete Category")
        print("3. Display All Categories")
        print("4. Find Category by ID")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_category(session)
        elif choice == '2':
            delete_category(session)
        elif choice == '3':
            display_all_categories(session)
        elif choice == '4':
            find_category_by_id(session)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def create_category(session):
    try:
        name = input("Enter category name: ")
        description = input("Enter category description: ")

        category = Category(category_name=name, category_description=description)
        session.add(category)
        session.commit()
        print(f"Category '{name}' created successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error creating category: {e}")

def delete_category(session):
    try:
        category_id = int(input("Enter category ID to delete: "))
        category = session.query(Category).get(category_id)

        if category:
            session.delete(category)
            session.commit()
            print(f"Category '{category.category_name}' deleted successfully.")
        else:
            print(f"Category with ID '{category_id}' not found.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting category: {e}")

def display_all_categories(session):
    try:
        categories = session.query(Category).all()

        if categories:
            for category in categories:
                print(f"ID: {category.category_id}, Name: {category.category_name}, Description: {category.category_description}")
        else:
            print("No categories found.")
    except Exception as e:
        print(f"Error displaying categories: {e}")

def find_category_by_id(session):
    try:
        category_id = int(input("Enter category ID to find: "))
        category = session.query(Category).get(category_id)

        if category:
            print(f"ID: {category.category_id}, Name: {category.category_name}, Description: {category.category_description}")
        else:
            print(f"Category with ID '{category_id}' not found.")
    except Exception as e:
        print(f"Error finding category: {e}")
