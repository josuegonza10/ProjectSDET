
🛠️ Technologies Used
Language: Python 3.12.0

Testing Library: unittest (standard library)

Browser Automation: Selenium WebDriver

Browser: Chrome (via ChromeDriver)

Pattern: Page Object Model (Only Login)


Install dependencies

pip install -r requirements.txt

Download ChromeDriver
Make sure the version matches your Chrome browser and place it in the drivers/ folder.

Requirements:

pytest==8.3.5
selenium==4.31.0
webdriver-manager==4.0.2
pytest-html==4.1.1


▶️ Running the Tests
   positive: All positive Selenium test
   negative: All negative test
   addproduct: All products added test
   filter: search by filter test
   removeproduct: Removed product
