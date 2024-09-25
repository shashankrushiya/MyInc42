from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# A decorator function to handle wait for element visibility before performing an action
def wait_helper(func):
    """
    A decorator to wait for an element to be visible before performing the desired action.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that introduces the waiting logic before calling the original function.
        """
        instance, locator = args            # Unpack the class instance and the locator from the arguments
        wait_object = WebDriverWait(instance.driver, timeout=20)
        wait_object.until(EC.visibility_of_element_located(locator))
        return func(*args, **kwargs)        # Call the original function after the wait condition is satisfied
    return wrapper
