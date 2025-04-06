# FormsSelenium

This project automates form filling using Selenium and webdriver_manager.

## Requirements

- Python
- Selenium
- webdriver_manager

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NurdauletSovetkhan/FormsSelenium.git
    cd FormsSelenium
    ```

2. Install the required packages:
    ```sh
    pip install selenium webdriver_manager
    ```

## Usage

1. Set the URL of the form you want to automate in the `form_url` variable inside `main.py`.

2. Run the script:
    ```sh
    python main.py
    ```

## Code Explanation

- The script imports necessary modules and sets up the Selenium WebDriver using `webdriver_manager` to automatically manage the ChromeDriver.
- It navigates to the specified `form_url`.
- The script automatically fills in checkboxes and radio buttons found on the form page.
- It attempts to navigate through the form pages by clicking "Next" or "Submit" buttons.
- If the "Submit" button is found, the form is submitted.

## License

This project is licensed under the MIT License.
