import psycopg2,re

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
    Id BIGSERIAL,
    First_name VARCHAR(20) NOT NULL,
    Last_name VARCHAR(20) NOT NULL,
    Phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (First_name,Last_name)
    ) """)
    while True:
        inp=int(input("""Enter relevant number of service:
Add/Update--1
Delete--2
Query--3
Pagination--4
Show--5
Insert_list--6
Exit--7
"""))
        match inp:
            case 1: #adds user
                fname=input("First name: ")
                lname=input("Last name: ")
                phone=input("Phone number: ")
                cursor.execute("""INSERT INTO phonebook(First_name, Last_name,Phone_number) VALUES(%s, %s,%s)
                ON CONFLICT (First_name,Last_name) DO UPDATE SET Phone_number = EXCLUDED.Phone_number
                """,(fname,lname,phone))
                connection.commit()

            case 2: #deletes from table
                fname=input("First name: ")
                lname=input("Last name: ")
                phone=input("Phone number: ")
                cursor.execute("""DELETE FROM phonebook WHERE First_name = %s 
                               OR Last_name = %s OR Phone_number = %s""",(fname,lname,phone))
                connection.commit()

            case 3: #querying data
                fname=input("First name: ")
                lname=input("Last name: ")
                phone = input("Phone number: ")
                cursor.execute(f"""SELECT * FROM phonebook WHERE First_name LIKE '%{fname}%' 
                AND Last_name LIKE '%{lname}%'
                AND Phone_number LIKE '%{phone}%'""")
                res = cursor.fetchall()
                print("Found: ",cursor.rowcount)
                for r in res:
                    print(r[0],'--',r[1],'--',r[2],'--',r[3])

            case 4:#pagination
                size=int(input("Size of page: "))
                page=int(input("Page number: "))
                order = input("Ordered by(First_name|Last_name|Phone_number|Id): ")
                cursor.execute("""SELECT Id, First_name, Last_name,Phone_number 
                            FROM phonebook ORDER BY """+order+""" OFFSET %s LIMIT %s""", (page, size))
                res = cursor.fetchall()
                for r in res:
                    print(r[0],'--',r[1],'--',r[2],'--',r[3])
            
            case 5: #shows the table
                cursor.execute("SELECT * FROM phonebook")
                res = cursor.fetchall()
                for r in res:
                    print(r[0],'--',r[1],'--',r[2],'--',r[3])
            case 6:#Inserting thourgh the list
                li = list(eval(input(" Enter 2D list = ")))
                invalid = []
                def Validnumber(number):
                    pattern = re.compile("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", re.IGNORECASE)
                    return pattern.match(number) is not None
                for person in li:
                    if Validnumber(person[2]):
                        cursor.execute("""INSERT INTO phonebook (First_name,Last_name,Phone_number) 
                                       VALUES (%s,%s, %s)""", (person[0],person[1],person[2]))
                        connection.commit()
                    else:
                        invalid.append(person)
                print("Invalid phone numbers:")
                for row in invalid:
                    print(row[0],'--',row[1],'--',row[2])

            case 7:
                break
            case _:
                print("Invalid input")

    cursor.close()
    connection.close()

#list = [("Levon","Aronian","+1 309-299-3529"),("Gukesh","Dommarju","+1 205-791-0279"),("Maxime", "Vachier-Lagrave","+1 505-644-9536"),("Viswanathan", "Anand","+1 505-548-0918"),("Richard", "Rapport","+1 505-861-5466")]
if __name__ == "__main__":
    main()