import psycopg2

class ConnectionDB():
    conn = None
    def connectDB(self):
        self.conn = psycopg2.connect(
            database="ACAM",
            user="postgres",
            password="P@ssw0rd",
            host="localhost",
            port="5432"
            )

        # print("Соединение установлено")   
        cursor = self.conn.cursor()
        return cursor


    def select_all(self):
        cursor = self.connectDB()
        cursor.execute('SELECT registration_date, request_type, "number", technical_status,' +
        'service, component, description, responsible_group, responsible_officer,' +
        ' "planned_run_time", expired_deadline, actual_execution_time, closing_code, ' +
        ' solution_description, who_decided_the_group, who_decided_the_employee, location, service_recipient, request_type_two FROM public."pupeStore";')

        # for row in cursor:
            # print(row)

        records = cursor.fetchall()
        cursor.close()
        self.conn.close()

    def select_one_number(self, number):
        cursor = self.connectDB()
        cursor.execute('SELECT "number"	FROM public."pupeStore" where "number" = %s', (number,))

        records = cursor.fetchone()
        cursor.close()
        self.conn.close()
        return records

    def insert_all(self, registration_date, request_type, number, technical_status, service,
              component, description, responsible_group, responsible_officer, planned_run_time, expired_deadline, actual_execution_time, closing_code,
              solution_description, who_decided_the_group, who_decided_the_employee, location, service_recipient, request_type_two):
        cursor = self.connectDB()
        cursor.execute('''INSERT INTO public."pupeStore"(
	registration_date, request_type, "number", technical_status, service, component, description, responsible_group,
     responsible_officer, planned_run_time, expired_deadline, actual_execution_time, closing_code, solution_description,
      who_decided_the_group, who_decided_the_employee, location, service_recipient, request_type_two)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (registration_date, request_type, number, technical_status, service,
              component, description, responsible_group, responsible_officer, planned_run_time, expired_deadline, actual_execution_time, closing_code,
              solution_description, who_decided_the_group, who_decided_the_employee, location, service_recipient, request_type_two
            ))

        self.conn.commit()
        cursor.close()
        self.conn.close()

    def update_one_number(self,  registration_date, request_type, technical_status, service,
              component, description, responsible_group, responsible_officer, planned_run_time, expired_deadline, actual_execution_time, closing_code,
              solution_description, who_decided_the_group, who_decided_the_employee, location, service_recipient, request_type_two, number):
        cursor = self.connectDB()
        cursor.execute('''UPDATE public."pupeStore"
	SET registration_date=%s, request_type=%s, technical_status=%s, service=%s, component=%s, description=%s, responsible_group=%s, responsible_officer=%s,
     planned_run_time=%s, expired_deadline=%s, actual_execution_time=%s, closing_code=%s, solution_description=%s, who_decided_the_group=%s,
      who_decided_the_employee=%s, location=%s, service_recipient=%s, request_type_two=%s
	WHERE "number"=%s;''', (registration_date, request_type, technical_status, service,
              component, description, responsible_group, responsible_officer, planned_run_time, expired_deadline, actual_execution_time, closing_code,
              solution_description, who_decided_the_group, who_decided_the_employee, location, service_recipient, request_type_two, number))

        self.conn.commit()
        cursor.close()
        self.conn.close()
        

