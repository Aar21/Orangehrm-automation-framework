from selenium import webdriver


def get_driver(browser_name="chrome"):
  browser_name = browser_name.lower()

  if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    # Headless mode is required for CI/CD pipelines (like GitHub Actions)
    # where there is no physical monitor/display screen.
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
  elif browser_name == "firefox":
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
  else:
    raise ValueError(f"Unsupported browser: {browser_name}")

  return driver