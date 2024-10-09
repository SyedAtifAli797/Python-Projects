import mysql.connector

# --> ESTABLISHING CONNECTION :-

mydb = mysql.connector.connect(
    user="root",
    database="employee",
    password='W7301@jqir#'
)

# --> CREATING A CURSOR : A cursor is an object that executes SQL statements and fetches results.:-

cur = mydb.cursor()

# --> GETTING DATA :-

def get_data():
    cur.execute("select * from record")
    x = cur.fetchall()
    for i in x:
        print(i)

# get_data()

def insert_data():
    while True:
        user_input = input("Do you want to add some data to the database? :")
        user_input = user_input.lower()
        if (user_input == 'yes'):
             record_id = int(input("Enter record_id : "))
             employee_name = input("Enter employee_name : ")
             employee_email = input("Enter employee_email : ")

             inserted_data = cur.execute("INSERT INTO record "
               "(record_id, employee_name,employee_email) "
               f"VALUES ('{record_id}','{employee_name}', '{employee_email}')" 
             )

        elif(user_input == 'no'):
            break

    mydb.commit()
    return inserted_data

# print(insert_data())

def update_data():
    while True:
        user_input = input("Do you want to update the data? : ")
        user_input = user_input.lower()
        if (user_input == 'yes'):
            record_id = int(input("Enter the employee's record id for make changes : "))
            column_name = input("Enter your columns name for which you want to make changes : ")
            new_value = input("Enter the selected columns value : ")

            updated_data = cur.execute(
            f"UPDATE record SET {column_name} = '{new_value}' WHERE record_id = '{record_id}' LIMIT 2"
            )

        else:
            break

    mydb.commit()

    return updated_data

# print(update_data())

def delete_data():
    record_id = int(input("Enter the record id of which the data you have to delete : "))
    deleted_data = cur.execute(
        f"DELETE FROM record WHERE record_id = '{record_id}' "
    )

    mydb.commit()

    return deleted_data

# print(delete_data())

def what_you_want():
    user_input = input("What task do you want to perform? If you want to get data press f. If you want to insert data enter i. If you want to update data enter u. If you want to delete data enter d!! :  ")
    user_input = user_input.lower()

    if(user_input == 'f'):
        return get_data()

    elif(user_input == 'i'):
        return insert_data()

    elif(user_input == 'u'):
        return update_data()
    
    elif(user_input == 'd'):
        return delete_data()

print(what_you_want())
