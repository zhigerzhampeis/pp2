import psycopg2
def main():
    connection = psycopg2.connect(
        host="localhost",
        database="one",
        user="postgres",
        password= "postgresql"
    )
    connection.autocommit = True
    cursor = connection.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook(
    Id BIGSERIAL PRIMARY KEY,
    Name VARCHAR(20) NOT NULL,
    Phone_number VARCHAR(20) NOT NULL
    ) """)
    while True:
        inp=int(input("""Enter relevant number of service:
Add--1
Delete--2
Query--3
Update--4
Show--5
Upload(csv)--6
Exit--7
"""))
        match inp:
            case 1: #adds user
                name=input("Name: ")
                phone=input("Phone number: ")
                cursor.execute("""INSERT INTO phonebook(Name,Phone_number)
                VALUES (%s,%s)""",(name,phone))
                connection.commit()

            case 2: #deletes from table
                name=input("Name: ")
                cursor.execute("DELETE FROM phonebook WHERE name = %s",(name,))
                connection.commit()

            case 3: #querying data
                name = input("Name: ")
                phone = input("Phone number: ")
                cursor.execute(f"""SELECT * FROM phonebook WHERE Name LIKE '%{name}%' AND Phone_number LIKE '%{phone}%'""")
                res = cursor.fetchall()
                print("Found: ",cursor.rowcount)
                for r in res:
                    print(r[0],'--',r[1],'--',r[2])

            case 4:
                name=input("Name: ")
                name2=input("New name: ")
                phone2=input("New phone number: ")
                cursor.execute("UPDATE phonebook SET name = %s, Phone_number = %s WHERE name = %s", (name2, phone2, name))
                connection.commit()
            
            case 5: #shows the table
                cursor.execute("SELECT * FROM phonebook")
                res = cursor.fetchall()
                for r in res:
                    print(r[0],'--',r[1],'--',r[2])
            case 6:
                path = input("Enter file path: ")
                cursor.execute("COPY phonebook FROM %s WITH (FORMAT csv)",(path,))
            case 7:
                break
            case _:
                print("Invalid input")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()