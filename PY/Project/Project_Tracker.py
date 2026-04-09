#Project Tracker

#Crete a database folder
import sqlite3
from datetime import date, datetime

class DatabaseManager:
    def __init__(self, db_name="project_tracker.db"):
        self.db_name = db_name
        self.init_database()

#Initialise database 
    def init_database(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    db_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    p_name TEXT NOT NULL,
                    p_manager TEXT NOT NULL,
                    p_team TEXT,
                    p_segment TEXT NOT NULL,
                    p_type TEXT NOT NULL,
                    p_status TEXT NOT NULL,
                    p_s_date TEXT NOT NULL,
                    p_e_date TEXT,
                    job_id INTEGER NOT NULL,
                    job_ol_id INTEGER NOT NULL,
                    job_ra_id INTEGER NOT NULL,
                    s_id INTEGER NOT NULL,
                    ta_id INTEGER NOT NULL,
                    pf_link TEXT NOT NULL,
                    b_unit TEXT NOT NULL,
                    b_country TEXT NOT NULL,
                    b_name TEXT NOT NULL,
                    b_name_id INTEGER NOT NULL,
                    market TEXT NOT NULL,
                    ir FLOAT NOT NULL,
                    loi FLOAT NOT NULL,
                    f_deliverables INTEGER NOT NULL,
                    f_revenue FLOAT NOT NULL,
                    f_cost FLOAT NOT NULL,
                    f_nprofit FLOAT NOT NULL,
                    f_margin FLOAT NOT NULL,
                    f_remarks TEXT,
                    created_at DATETIME DEFAULT (datetime('now', '+8 hours'))
                )           
            ''')
            conn.commit()

    def to_sql_date(self, date_str):
        """Convert date from DD-MM-YYYY to YYYY-MM-DD format."""
        try:
            return datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

#Project creation
    def create_project(self, p_name, p_manager, p_team, p_segment, p_type, p_s_date, p_e_date, job_id, job_ol_id, job_ra_id,
                       s_id, ta_id, pf_link, p_status, b_unit, b_country, b_name, b_name_id,
                       market, ir, loi, f_deliverables, f_revenue, f_cost,
                       f_nprofit, f_margin, f_remarks):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO projects (
                    p_name, p_manager, p_team, p_segment, p_type, p_s_date, p_e_date, job_id, job_ol_id, job_ra_id,
                    s_id, ta_id, pf_link, p_status, b_unit, b_country, b_name, b_name_id,
                    market, ir, loi, f_deliverables, f_revenue, f_cost,
                    f_nprofit, f_margin, f_remarks
                    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''', (p_name, p_manager, p_team, p_segment, p_type, p_s_date, p_e_date, job_id, job_ol_id, job_ra_id,
                    s_id, ta_id, pf_link, p_status, b_unit, b_country, b_name, b_name_id,
                    market, ir, loi, f_deliverables, f_revenue, f_cost,
                    f_nprofit, f_margin, f_remarks))
                return cursor.lastrowid
            
        except sqlite3.IntegrityError as e:
            print(f"An error occurred: {e}")
            return None

#Project count
    def fetch_all_projects_count(self, query, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            print(f"Total projects count: {len(results)}")  
            return results

    def fetch_one_with_count(self, query, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            count = self.fetch_all_projects_count(query, params)
            print(f"Project count: {len(count)}")
            return result

#Project retrieval
    def get_all_projects(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects')
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects')  
        
    def get_project_by_db_id(self, db_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE db_id = ?', (db_id,))
            return cursor.fetchone()
            return self.fetch_one_with_count('SELECT * FROM projects WHERE db_id = ?', (db_id,))  
    
    def get_projects_by_name(self, keyword):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE p_name LIKE ? COLLATE NOCASE ORDER BY p_name', (f'%{keyword}%',))
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE p_name LIKE ? COLLATE NOCASE ORDER BY p_name', (f'%{keyword}%',))
    
    def get_projects_by_s_id(self, s_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE s_id = ?', (s_id,))
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE s_id = ?', (s_id,))
    
    def get_projects_by_p_segment(self, p_segment):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE p_segment = ?', (p_segment,))
            return cursor.fetchall()  
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE p_segment = ?', (p_segment,))
    
    def get_projects_by_p_type(self, p_type):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE p_type = ?', (p_type,))
            return cursor.fetchall()  
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE p_type = ?', (p_type,))  

    def get_projects_by_ta_id(self, ta_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE ta_id = ?', (ta_id,))
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE ta_id = ?', (ta_id,))    
    
    def get_projects_by_job_id(self, job_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE job_id = ?', (job_id,))
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE job_id = ?', (job_id,))  
        
    def get_projects_by_job_ol_id(self, job_ol_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE job_ol_id = ?', (job_ol_id,))
            return cursor.fetchall()     
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE job_ol_id = ?', (job_ol_id,))      
    
    def get_projects_by_job_ra_id(self, job_ra_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE job_ra_id = ?', (job_ra_id,))
            return cursor.fetchall()    
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE job_ra_id = ?', (job_ra_id,))  
    
    def get_projects_by_p_status(self, p_status):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE p_status = ?', (p_status,))
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE p_status = ?', (p_status,))
        
    def get_projects_by_p_manager(self, p_manager):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE p_manager = ?', (p_manager,))
            return cursor.fetchall()  
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE p_manager = ?', (p_manager,))
        
    def get_projects_by_b_unit(self, b_unit):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE b_unit = ?', (b_unit,))
            return cursor.fetchall()
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE b_unit = ?', (b_unit,))
    
    def get_projects_by_b_country(self, b_country):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE b_country = ?', (b_country,))
            return cursor.fetchall()  
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE b_country = ?', (b_country,))
    
    def get_projects_by_b_name(self, b_name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM projects WHERE b_name = ?', (b_name,))
            return cursor.fetchall()   
            return self.fetch_all_projects_count('SELECT * FROM projects WHERE b_name = ?', (b_name,))
        
    def get_projects_by_f_margin_band(self, f_margin_band):
        """Filter projects by margin range."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            if f_margin_band == "19%_and_below":
                cursor.execute('SELECT * FROM projects WHERE f_margin <= 19')
                return self.fetch_all_projects_count('SELECT * FROM projects WHERE f_margin <= 19')
            elif f_margin_band == "20%_to_49%":
                cursor.execute('SELECT * FROM projects WHERE f_margin BETWEEN 20 AND 49')
                return self.fetch_all_projects_count('SELECT * FROM projects WHERE f_margin BETWEEN 20 AND 49')
            elif f_margin_band == "50%_to_79%":
                cursor.execute('SELECT * FROM projects WHERE f_margin BETWEEN 50 AND 79')
                return self.fetch_all_projects_count('SELECT * FROM projects WHERE f_margin BETWEEN 50 AND 79')
            elif f_margin_band == "80%_and_above":
                cursor.execute('SELECT * FROM projects WHERE f_margin >= 80')
                return self.fetch_all_projects_count('SELECT * FROM projects WHERE f_margin >= 80')
            else: 
                return []
            
            return cursor.fetchall()

    def get_projects_by_date_filter(self, month=None, year=None, since=False):
        """Filter by month/year or since month/year."""
        current_year = datetime.now().year

        if month is not None:
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError("month must be between 1 and 12")

        if year is not None:
            year = int(year)

        if since:
            if month is not None and year is None:
                start_date = f"{current_year}-{month:02d}-01"
            elif month is not None and year is not None:
                start_date = f"{year}-{month:02d}-01"
            elif month is None and year is not None:
                start_date = f"{year}-01-01"
            else:
                return []

            return self.fetch_all_projects_count(
                'SELECT * FROM projects WHERE "date" >= ? ORDER BY "date"',
                (start_date,)
            )

        if month is not None and year is None:
            return self.fetch_all_projects_count(
                '''
                SELECT * FROM projects
                WHERE CAST(strftime('%m', "date") AS INTEGER) = ?
                  AND CAST(strftime('%Y', "date") AS INTEGER) = ?
                ORDER BY "date"
                ''',
                (month, current_year)
            )

        if month is not None and year is not None:
            return self.fetch_all_projects_count(
                '''
                SELECT * FROM projects
                WHERE CAST(strftime('%m', "date") AS INTEGER) = ?
                  AND CAST(strftime('%Y', "date") AS INTEGER) = ?
                ORDER BY "date"
                ''',
                (month, year)
            )

        if year is not None:
            return self.fetch_all_projects_count(
                '''
                SELECT * FROM projects
                WHERE CAST(strftime('%Y', "date") AS INTEGER) = ?
                ORDER BY "date"
                ''',
                (year,)
            )

        return self.fetch_all_projects_count('SELECT * FROM projects ORDER BY "date"')
    
#Project update
    def update_project(self, db_id, **kwargs):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            fields = []
            values = []
            for key, value in kwargs.items():
                fields.append(f"{key} = ?")
                values.append(value)
            values.append(db_id)
            sql = f"UPDATE projects SET {', '.join(fields)} WHERE db_id = ?"
            cursor.execute(sql, values)
            conn.commit()
            
            if cursor.rowcount > 0:
                    print(f"Project {db_id} updated successfully.")
                    return True
            else:
                    print(f"No project found with db_id {db_id}.")
                    return False    
            
    def update_project(self, db_id, **kwargs):
        if not kwargs:
            print("No fields provided for update.")
            return False

        fields = ", ".join([f"{key} = ?" for key in kwargs])
        values = list(kwargs.values())
        values.append(db_id)

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE projects SET {fields} WHERE db_id = ?", values)
            conn.commit()

            if cursor.rowcount > 0:
                print(f"Project {db_id} updated successfully.")
                return True
            else:
                print(f"No project found with db_id {db_id}.")
                return False    

#Project deletion
    def delete_project(self, db_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM projects WHERE db_id = ?', (db_id,))
            conn.commit()
            
            if cursor.rowcount > 0:
                    print(f"Project {db_id} deleted successfully.")
                    return True
            else:
                    print(f"No project found with db_id {db_id}.")
                    return False
            
#Project display menu
    def display_menu(self):
        print("\n" + "="*30)
        print("Project Tracker Menu:")
        print("="*30)
        print("1. Project Creation")
        print("2. Project Retrieval")
        print("3. Project Update")
        print("4. Project Deletion")
        print("5. Exit")
        print("="*30)

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                print("\nProject Creation:")
                p_name = input("Project Name: ")
                p_manager = input("Project Manager: ")
                p_team = input("Project Team: ")
                p_segment = input("Project Segment: ")
                p_type = input("Project Type: ")
                p_s_date = self.to_sql_date(input("Start Date (DD-MM-YYYY): "))
                p_e_date_input = input("End Date (DD-MM-YYYY, optional): ")
                p_e_date = self.to_sql_date(p_e_date_input) if p_e_date_input else None
                job_id = int(input("Job ID: "))
                job_ol_id = int(input("Job OL ID: "))
                job_ra_id = int(input("Job RAES ID: "))
                s_id = int(input("SID: "))
                ta_id = int(input("TA ID: "))
                pf_link = input("Path Folder Link: ")
                p_status = input("Project Status: ")
                b_unit = input("Business Unit: ")
                b_country = input("Business Country: ")
                b_name = input("Business Name: ")
                b_name_id = int(input("Business Name ID: "))
                market = input("Market: ")
                ir = float(input("IR (%): "))
                loi = int(input("LOI (minutes): "))
                f_deliverables = int(input("Final Deliverables: "))
                f_revenue = float(input("Final Revenue ($): "))
                f_cost = float(input("Final Cost ($): "))
                f_nprofit = float(input("Final Net Profit ($): "))
                f_margin = float(input("Final Margin (%): "))
                f_remarks = input("Final Remarks: ")
                try:
                    db_id = self.create_project(p_name, p_manager, p_team, p_segment, p_type, p_s_date, p_e_date, job_id, job_ol_id, job_ra_id,
                                               s_id, ta_id, pf_link, p_status, b_unit, b_country, b_name, b_name_id,
                                               market, ir, loi, f_deliverables, f_revenue, f_cost,
                                               f_nprofit, f_margin, f_remarks)
                    if db_id:
                        print(f"Project created successfully with ID: {db_id}")
                    else:
                        print("Failed to create project.")
                except ValueError as e:
                    print(f"Invalid input: {e}")
                
            elif choice == '2':
                print("\n" + "="*30)
                print("\nProject Retrieval:")
                print("="*30)
                print("1. Retrieve total project count")
                print("2. Retrieve all projects")
                print("3. Retrieve project by Database ID")
                print("4. Retrieve projects by Project Name")
                print("5. Retrieve projects by SID")
                print("6. Retrieve projects by Project Segment")
                print("7. Retrieve projects by Project Type")
                print("8. Retrieve projects by TA ID")
                print("9. Retrieve projects by Job ID")
                print("10. Retrieve projects by Job OL ID")
                print("11. Retrieve projects by Job RAES ID")
                print("12. Retrieve projects by Project Status")
                print("13. Retrieve projects by Project Manager")
                print("14. Retrieve projects by Business Unit")
                print("15. Retrieve projects by Business Country")
                print("16. Retrieve projects by Business Name")
                print("17. Retrieve projects by Final Margin Band")
                print("18. Retrieve projects by Date Filter")
                print("19. Back to Main Menu")
                sub_choice = input("Enter your choice (1-19): ")

                if sub_choice == '4':
                    keyword = input("Enter project name keyword: ")
                    projects = self.get_projects_by_name(keyword)
                    if projects:
                        print(f"Projects matching '{keyword}':")
                        for i, project in enumerate(projects, start=1):
                            print(f"{i}. DB ID: {project[0]}, SID: {project[11]}, Project Name: {project[1]}, Project Manager: {project[2]}")
                        
                        selected_db_id = int(input("Enter the DB ID to view full project details: "))
                        project = self.get_project_by_db_id(selected_db_id)
                        print(project)
                    else:
                        print(f"No projects found matching '{keyword}'.")

            elif choice == '3':
                print("\nProject Update:")
                db_id = int(input("Enter the Database ID of the project to update: "))
                print("\n" + "="*30)
                print("\nProject update:")
                print("="*30)
                print("1. Update Project Name")
                print("2. Update Project Manager")
                print("3. Update Project Team")
                print("4. Update Project Segment")
                print("5. Update Project Type")
                print("6. Update Start Date")
                print("7. Update End Date")
                print("8. Update Job ID")
                print("9. Update Job OL ID")
                print("10. Update Job RAES ID")
                print("11. Update SID")
                print("12. Update TAID")
                print("13. Update Path Folder Link")
                print("14. Update Project Status")
                print("15. Update Business Unit")
                print("16. Update Business Country")
                print("17. Update Business Name")
                print("18. Update Business Name ID")
                print("19. Update Market")
                print("20. Update IR")
                print("21. Update LOI")
                print("22. Update Final Deliverables")
                print("23. Update Final Revenue")
                print("24. Update Final Cost")
                print("25. Update Final Net Profit")
                print("26. Update Final Margin")
                print("27. Update Final Remarks")
                print("28. Back to Main Menu")
                update_choice = input("Enter your choice (1-28): ")

                field_mapping = {
                    '1': 'p_name',
                    '2': 'p_manager',
                    '3': 'p_team',
                    '4': 'p_segment',
                    '5': 'p_type',
                    '6': 'p_s_date',
                    '7': 'p_e_date',
                    '8': 'job_id',
                    '9': 'job_ol_id',
                    '10': 'job_ra_id',
                    '11': 's_id',
                    '12': 'ta_id',
                    '13': 'pf_link',
                    '14': 'p_status',
                    '15': 'b_unit',
                    '16': 'b_country',
                    '17': 'b_name',
                    '18': 'b_name_id',
                    '19': 'market',
                    '20': 'ir',
                    '21': 'loi',
                    '22': 'f_deliverables',
                    '23': 'f_revenue',
                    '24': 'f_cost',
                    '25': 'f_nprofit',
                    '26': 'f_margin',
                    '27': 'f_remarks',
                }
                field_name = field_mapping.get(update_choice)
                if field_name:
                    new_value = input(f"Enter new value for {field_name}: ")
                    try:
                        if field_name in ['job_id', 'job_ol_id', 'job_ra_id', 's_id', 'ta_id', 'b_name_id']:
                            new_value = int(new_value)
                        elif field_name in ['ir', 'f_revenue', 'f_cost', 'f_nprofit', 'f_margin']:
                            new_value = float(new_value)
                        elif field_name in ['p_s_date', 'p_e_date']:
                            new_value = self.to_sql_date(new_value)
                        
                        self.update_project(db_id, **{field_name: new_value})
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                else:
                    print("Invalid choice for update field.")
                
            elif choice == '4':
                print("\nProject Deletion:")
                try:
                    db_id = int(input("Enter the Database ID of the project to delete: "))
                    confirm = input(f"Please confirm to delete project (yes/no): \n"
                                    f"Database ID: {db_id} \n"
                                    f"Project Name: {p_name} \n")
                    if confirm.lower() == 'yes':
                        self.delete_project(db_id)
                        print(f"Project {db_id} {p_name} deleted successfully.")
                    else:
                        print("Project deletion canceled.")
                except ValueError as e:
                    print(f"Invalid input: {e}")

            elif choice == '5':
                print("Exiting Project Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
            
        input("\n Press Enter to continue...")

if __name__ == "__main__":
    db = DatabaseManager()
    db.main()
