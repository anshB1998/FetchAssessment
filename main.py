from driver_utils import initialize_driver, click_weigh, click_reset, fill_bowls
from game_utils import get_measurement, check_fake_bar

# Main function to run the test
def run_test():
    driver = initialize_driver()
    """ 
    Algorithm to find the fake gold bar:

    1. Take first 6 gold bars, distributing them evenly on the left anf right bowls.
    2. Weigh them out.
    3. If weights are equal, we know that the fake bar is one of the last 3 gold bars
       Else we know which set of gold bars (left/right bowl) contains the fake bar.
    4. Take 2 gold bars (one in each bowl) from the decided set and weigh them.
    5. If both gold bars are equal, we know the final left gold bar is the fake one
       Else we know which gold bar weighed less is the fake one.

    In this fashion, we can find the fake gold bar in just 2 weighings everytime. 
    """

    # Take the first 6 gold bars and distribute them across the left and right bowls
    left_bowl = [0, 1, 2]
    right_bowl = [3, 4, 5]

    fill_bowls(driver, left_bowl, right_bowl)
    click_weigh(driver)
    weighing_result, operator = get_measurement(driver)

    reduced_set = []
    if operator == '<':
        reduced_set = [0, 1, 2]
    elif operator == '>':
        reduced_set = [3, 4, 5]
    elif operator == '=':
        reduced_set = [6, 7, 8]

    click_reset(driver)
    fill_bowls(driver, [reduced_set[0]], [reduced_set[1]])
    click_weigh(driver)
    weighing_result, operator = get_measurement(driver)

    if operator == '<':
        fake_bar_number = reduced_set[0]
    elif operator == '>':
        fake_bar_number = reduced_set[1]
    elif operator == '=':
        fake_bar_number = reduced_set[2]

    alert_message = check_fake_bar(driver, fake_bar_number)
    print("\n######################  FAKE GOLD BAR FINDER RESULT ######################")
    print(f"\nClicked on bar number {fake_bar_number} to get the alert: '{alert_message}'")

    if alert_message == "Yay! You find it!": # Alert message contains the word 'find' instead of 'found' on actual website
        print(f"Algorithm complete. Found Fake Gold Bar at number: {fake_bar_number}")
        print("\nNumber of weighings: 2")
        print("\nWeighing list:")
        for i, result in enumerate(weighing_result):
            print(f"Weighing {i + 1}: {result}")

    driver.quit()

if __name__ == "__main__":
    run_test()
