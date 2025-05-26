prompt_for_web_testing = """
Common Attention:
Attention 1: You can only write code in Python.
Attention 2: The third-party libraries you are allowed to use include psutil, shutil, unittest and selenium.
Attention 3: Please adhere strictly to the Testing Task description to develop unit test code for the web application using Python, Selenium, and unittest framework.
Attention 4: The test code needs to be directly executable and only need to cover the tests required by the Testing Task description.
Attention 5: You will implement the test.py and finish it follows in the strictly defined format.
Attention 6: You should run codebase code yourself, testing one feature per run. so you need to run the command "python main.py"
Attention 6: Chrome WebDriver is already installed and the path is in the environment variable, so there is no need to specify its path in the test code. And 'WebDriver' object has no attribute 'find_element_by_id'
Attention 7: Access to the login page is available at http://localhost:xxxx.
Attention 8: You must utilize the username and password from Data Storage to construct a login method within the test class. 
Attention 9: Access to All pages, except for the login and registration pages, requires logging in from the login page and then proceeding by clicking the corresponding buttons on the page to navigate to the desired page.
Attention 10: After logging in, you will be redirected to other pages and will not stay on the login page.
Attention 11: For each Functionalities in Black Box Unit Test Cases, please generate a unit test function. If the functionality is not implemented in the codebase, generate a corresponding test point that returns a failure.Each unit test function corresponds to a Functionalities in Black Box Unit Test Cases.
Attention 12: If a Functionalities has multiple test cases, you should write all of them inside one unit test function.
### codebase
{codebase}
### testcase
{testcase}
### instruction: Write test code for the software in the codebase based on the test cases.

### Example Code
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import subprocess

class TestDailyJournalApp(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver and open the login page
        self.process = subprocess.Popen(['python', 'main.py'])  # 修改为实际路径
        time.sleep(5)  # 等待 Web 应用完全启动
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000/')

    def tearDown(self):
        # Close the web driver session
        self.driver.quit()

    def login(self, username, password):
        # Helper method to perform login
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[text()="Login"]').click()
        time.sleep(1)  # Wait for the next page to load

    def test_login(self):
        # Functionalities 1  Test user login functionality
        self.login("admin", "admin123")

        # Verify that the Dashboard Page has loaded
        self.assertIn("Dashboard", self.driver.title)

    def test_navigate_to_registration(self):
        # Functionalities 2 Test navigation to the Registration Page
        self.driver.find_element(By.LINK_TEXT, 'Register here').click()
        time.sleep(1)  # Wait for the next page to load

        # Verify that the Registration Page has loaded
        self.assertIn("Register", self.driver.title)

    def test_registration(self):
        # Functionalities 3 Test user registration functionality
        self.driver.find_element(By.LINK_TEXT, 'Register here').click()
        time.sleep(1)  # Wait for the next page to load

        new_username = "new_user"
        new_password = "new_password"

        # Input username and password for registration
        self.driver.find_element(By.NAME, 'username').send_keys(new_username)
        self.driver.find_element(By.NAME, 'password').send_keys(new_password)
        self.driver.find_element(By.XPATH, '//button[text()="Register"]').click()
        time.sleep(1)  # Wait for the next page to load

        # Verify the user is redirected to the login page
        self.assertIn("Login", self.driver.title)

    def test_view_journal_entries(self):
        # Functionalities 4 Test viewing journal entries after logging in
        self.login("admin", "admin123")

        # Verify that the Dashboard Page shows entries
        entries = self.driver.find_elements(By.CLASS_NAME, 'list-group-item')
        self.assertGreater(len(entries), 0, "No journal entries found.")

    def test_create_new_entry(self):
        # Functionalities 5 Test creating a new journal entry
        self.login("admin", "admin123")

        # Navigate to New Entry Page
        self.driver.find_element(By.LINK_TEXT, 'Create New Entry').click()
        time.sleep(1)  # Wait for the next page to load

        entry_title = "My New Journal Entry"
        entry_content = "This is the content of my new journal entry."

        # Fill out the new entry form
        self.driver.find_element(By.NAME, 'title').send_keys(entry_title)
        self.driver.find_element(By.NAME, 'content').send_keys(entry_content)
        self.driver.find_element(By.XPATH, '//button[text()="Save Entry"]').click()
        time.sleep(1)  # Wait for saving the entry

        # Verify that the new entry is displayed on the Dashboard
        self.assertIn(entry_title, self.driver.page_source)

    def test_save_journal_entry(self):
        # Functionalities 6
        self.fail(not implemented")

    def test_logout(self):
        # Functionalities 7 Test logging out
        self.login("admin", "admin123")

        # Click the Logout button
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        time.sleep(1)  # Wait for the next page to load

        # Verify that the user is redirected to the Login Page
        self.assertIn("Login", self.driver.title)

    def test_data_storage(self):
        # Functionalities 8
        self.fail(not implemented")

if __name__ == '__main__':
    unittest.main()


```
"""

prompt_for_game_testing = """
Common Attention:
Attention 1: You can only write code in Python.
Attention 2: The third-party libraries you are allowed to use include psutil, shutil, unittest, and selenium.
Attention 3: Please adhere strictly to the Testing Task description to develop unit test code for the pygame using Python and unittest framework.
Attention 4: The test code needs to be directly executable and only need to cover the tests required by the Testing Task description.
Attention 5: You will implement the test.py and finish it follows in the strictly defined format.
Attention 6: You should run codebase code yourself, testing one feature per run.
Attention 7: For each Functionalities in Black Box Unit Test Cases, please generate a unit test function. If the functionality is not implemented in the codebase, generate a corresponding test point that returns a failure.Each unit test function corresponds to a Functionalities in Black Box Unit Test Cases.
Attention 8: If a Functionalities has multiple test cases, you should write all of them inside one unit test function.
### codebase
{codebase}
### testcase
{testcase}
### instruction: Write test code for the software in the codebase based on the test cases.
-------
### Example Code
```python
import unittest
import pygame
from game import Game
from paddle import Paddle
from ball import Ball
from brick import Brick

class TestBrickBreakerGame(unittest.TestCase):

    def setUp(self):
        # Initialize the game and its components
        self.game = Game()
        self.paddle = self.game.paddle
        self.ball = self.game.ball
        self.bricks = self.game.bricks

    def test_control_paddle_movement(self):
        # Functionalities 1 Test paddle movement to the left
        initial_x = self.paddle.x
        self.paddle.move('left')
        self.assertLess(self.paddle.x, initial_x, "Paddle should move left")

        # Test paddle movement to the right
        initial_x = self.paddle.x
        self.paddle.move('right')
        self.assertGreater(self.paddle.x, initial_x, "Paddle should move right")

    def test_ball_bounce_mechanics(self):
        # Functionalities 2 Set the ball position to simulate hitting the paddle
        self.ball.x = self.paddle.x + self.paddle.width // 2
        self.ball.y = 580 - self.ball.radius
        initial_dy = self.ball.dy
        self.game.check_collisions()
        self.assertEqual(self.ball.dy, -initial_dy, "Ball should bounce off the paddle")

    def test_brick_disappearance(self):
        # Functionalities 3 Hit a brick until it disappears
        brick = self.bricks[0]
        initial_life = brick.life
        for _ in range(initial_life):
            brick.hit()
        self.assertEqual(brick.life, 0, "Brick should disappear when life reaches 0")

    def test_game_start_mechanism(self):
        # Functionalities 4 Simulate starting the game by moving the paddle
        self.game.handle_input()
        self.assertTrue(self.game.running, "Game should be running after starting")

    def test_ball_movement(self):
        # Functionalities 5 Test ball movement upwards
        initial_y = self.ball.y
        self.ball.move()
        self.assertNotEqual(self.ball.y, initial_y, "Ball should move upwards")

    def test_end_game_condition(self):
        # Functionalities 6 Simulate the ball falling below the paddle
        self.ball.y = self.game.screen_height + 1
        self.game.update()
        self.assertFalse(self.game.running, "Game should end when the ball falls below the paddle")

    def test_brick_splitting_logic(self):
        # Functionalities 7 Test brick splitting logic (not implemented in codebase)
        self.fail("Brick splitting logic is not implemented in the codebase")

    def test_save_game_state(self):
        # Functionalities 8 Test saving game state (not implemented in codebase)
        self.fail("Save game state functionality is not implemented in the codebase")

    def test_load_game_state(self):
        # Functionalities 9 Test loading game state (not implemented in codebase)
        self.fail("Load game state functionality is not implemented in the codebase")

if __name__ == '__main__':
    unittest.main()
```
"""

prompt_for_gui_testing = """
Common Attention:
Attention 1: You can only write code in Python.
Attention 2: The third-party libraries you are allowed to use include psutil, shutil, unittest.
Attention 3: Please adhere strictly to the Testing Task description to develop unit test code for the gui application using Python and unittest framework.
Attention 4: The test code needs to be directly executable and only need to cover the tests required by the Testing Task description.
Attention 5: You will implement the test.py and finish it follows in the strictly defined format.
Attention 6: You should run codebase code yourself, testing one feature per run.
Attention 7: For each Functionalities in Black Box Unit Test Cases, please generate a unit test function. If the functionality is not implemented in the codebase, generate a corresponding test point that returns a failure.Each unit test function corresponds to a Functionalities in Black Box Unit Test Cases.
Attention 9: If a Functionalities has multiple test cases, you should write all of them inside one unit test function.
### codebase
{codebase}
### testcase
{testcase}
### instruction: Write test code for the software in the codebase based on the test cases.

----------
### Example Codes
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()


    def test_addition(self):
        # Functionalities 1: Perform Basic Arithmetic Operations
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.subtract(7, -2), 9)
        self.assertEqual(self.calculator.multiply(4, 6), 24)
        self.assertEqual(self.calculator.divide(8, 2), 4)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)


    def test_square_root_positive(self):
        # Functionalities 2: Calculate Square Roots
        self.assertEqual(self.calculator.square_root(16), 4)
        self.assertEqual(self.calculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            self.calculator.square_root(-9)

    def test_exponentiation_positive(self):
        # Functionalities 3: Perform Exponentiation Calculations
        self.assertEqual(self.calculator.exponentiate(2, 3), 8)
        self.assertEqual(self.calculator.exponentiate(0, 5), 0)
        self.assertEqual(self.calculator.exponentiate(7, 0), 1)
        self.assertEqual(self.calculator.exponentiate(-3, 2), 9)


    def test_percentage_positive(self):
        # Functionalities 4: Calculate Percentages
        self.fail("not implemented")

if __name__ == '__main__':
    unittest.main()

"""

