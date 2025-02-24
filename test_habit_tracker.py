import habit
import db
import analytics
from datetime import datetime




#Initializing functions
h = habit.Habit("0","0",1,"2000-01-01") #Class initialization
db.connection("test.db")
analytics.connection("test.db")
db.create_habits_table()





"""When testing, strings must use underscores instead of spaces and cannot contain special characters. Frequency must be an integer without spaces or extra characters. The creation_date must strictly follow the (YYYY-MM-DD) format. Despite these limitations, main.py and analytics.py handle input transformations and print statements to return values formatted as originally input."""


"""Testing of habit class"""


def test_create():
    #Confirm the existence of the habit in the habits table
    h.create(habit_name="Test_name", description="Test_description", frequency=1,creation_date="2025-01-01" )
    assert db.search_habit(habit_name="Test_name") == (1, True)
    #confirms the creation of it's own check off table
    assert db.search_checkoff_table(habit_name="Test_name") == (True)

def test_create_not_valid_input():
    #Confirm the existence of the habit in the habits table
    h.create(habit_name="Test_name", description="Test_description", frequency=1,creation_date="2025-01-01" )
    

def test_modify():
    h.modify(habit_name="Test_name", new_habit_name="Modified_test_name", new_description="Modified test description")
    assert db.search_habit(habit_name="Test_name") == (0, False)
    assert db.search_habit(habit_name="Modified_test_name") == (1, True)
    #There is no need to search the description because always come along with the name, and name is more relevant because also affects the check_off_table
    assert db.search_checkoff_table(habit_name="Test_name") == (False)
    assert db.search_checkoff_table(habit_name="Modified_test_name") == (True)


def test_delete():
    h.delete(habit_name="Modified_test_name")
    assert db.search_habit(habit_name="Modified_test_name") == (0, False)
    assert db.search_checkoff_table(habit_name="Modified_test_name") == (False)


def test_check_off_today():
    today = datetime.today().strftime("%Y-%m-%d")
    h.create(habit_name="Test_name", description="Test_description", frequency=1,creation_date="2025-01-01" )
    h.check_off_today(habit_name="Test_name", frequency=1)
    assert db.search_check_off(habit_name="Test_name",check_off_date=today) == [(today)]
    #I have to delete the habit and create again because check off today creates unnecesary difficulties to test when trying to verify the struggle functions.
    h.delete(habit_name="Test_name")
    h.create(habit_name="Test_name", description="Test_description", frequency=1,creation_date="2025-01-01" )

def test_check_off_date():
    h.check_off_date(habit_name="Test_name",check_off_date="2025-01-30", frequency=1)
    assert db.search_check_off(habit_name="Test_name",check_off_date="2025-01-30") == ["2025-01-30"]
    assert db.search_check_off(habit_name="Test_name",check_off_date="2025-01-29") == [] #Ensure that previous days are not being checked off, only the selected one




"""Testing of analytics module"""


def test_list():
    assert analytics.list_habits() == ['habit name, description, frequency, creation date', ('Test_name', 'Test_description', 1, '2025-01-01')]

def test_same_frequency():
    assert analytics.same_frequency_list(1) == [('Test_name',)]

def test_longest_streak():
    #To ensure a proper comparison between multiple habits, let’s create two additional habits (with different frequencies) and check them off today.
    h.create(habit_name="Test_name2", description="Test_description2", frequency=2,creation_date="2025-01-01" )
    h.check_off_date(habit_name="Test_name2",check_off_date="2025-01-30", frequency=2)
    h.create(habit_name="Test_name3", description="Test_description3", frequency=3,creation_date="2025-01-01" )
    h.check_off_date(habit_name="Test_name3",check_off_date="2025-01-30", frequency=3)
    assert analytics.overall_streak() == 3

def test_streak():
    assert analytics.streak(habit_name="Test_name") == 1
    assert analytics.streak(habit_name="Test_name2") == 2
    assert analytics.streak(habit_name="Test_name3") == 3

def test_longest_struggle():
    assert analytics.overall_struggle() == 29

def test_struggle():
    assert analytics.struggle(habit_name="Test_name") == 29
    assert analytics.struggle(habit_name="Test_name2") == 28
    assert analytics.struggle(habit_name="Test_name3") == 27
    db.erase("test.db")#Finally, the database is deleted to prevent incompatibilities if the test is run multiple times or the functions are modified.
