from bs4 import BeautifulSoup
import requests
import sys

def main():

    # Error Checking
    if len(sys.argv) != 1:
        sys.exit("usage: python project.py")

    menu()
    try:
        option = int(input("Enter your option: "))
    except (ValueError, TypeError):
        sys.exit("\nPlease enter a valid option!\n")


    while option != 0:

        # Basic Search
        if option == 1:

            # Asking for item
            item = input("\nWhat item are you looking for? ")

            # Item Error Checking
            if len(item)<=2:
                sys.exit("\nPlease input 3 or more charcters!\n")

            # Setting values
            ilimit = 4
            sort_order = 3
            print("\nSetting default limit to '4' and sort order to 'Best Selling'...")

            # Function calling
            retrieve_html(item, sort_order)
            data = scrape_html(ilimit, 0)
            for i in data:
                print(f"{data[i]} -- {i}")
            print("\n")


        # Advanced Search
        elif option == 2:
           # Asking for item
            item = input("\nWhat item are you looking for? ")

            # Item Error Checking
            if len(item)<=2:
                sys.exit("\nPlease input 3 or more charcters!\n")

            # Setting limit
            ilimit = input("\nLimit for results?\n(Can't exceed 25)\n(Default = 4 by pressing Enter)\n")

            # Defualt/Error checking ilimit
            ilimit = ilimitdefault(ilimit)

            # Setting sort
            sort_order = input("Sort by:\n[0] Featured Items\n[1] Lowest Price\n[2] Highest Price\n[3] Best Selling\n[4] Best Rating\n[5] Most Reviews\n(Default = 3 by pressing Enter)\n")

            # Defualt/Error checking sort_order
            sort_order = sort_orderdefault(sort_order)

            # Function calling
            retrieve_html(item, sort_order)
            data = scrape_html(ilimit, 1)


            for i in data:
                price, url = data[i].split(" --url ")
                print(f"{price} -- {i}\nURL: {url}\n")
            print()

        # Invalid Option
        else:
            print("Invalid option.")
            print()

        # Reprompt user
        menu()
        try:
            option = int(input("Enter your option: "))
        except (ValueError, TypeError):
            sys.exit("\nPlease enter a valid option!\n")

    print("\nThanks for using this program!\n")


# --------------------------- Function Declaration --------------------------- #


# Retrieve the HTML document
def retrieve_html(item, sort_order):

    # Request url
    url = f"https://www.newegg.com/p/pl?d={item}&Order={sort_order}"
    response = requests.get(url)

    # If code 200 proceed
    if response.status_code == 200:
        html = response.text
    else:
        sys.exit("Error: Could not fetch HTML")

    # Save the response to a new file
    with open("newegg.html", "w") as newf:
        newf.write(html)
        newf.close()

    # Verify that the file was created and data was saved
    with open('newegg.html', 'r') as file:
        if file:
            print("\nOutput file named 'newegg.html' created!\n\n")
            return None
        print("Output file not created!")


# Scrape the HTML document
def scrape_html(ilimit, s_type):
    with open("newegg.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")

        # Get the names
        names = doc.find_all("a", title="View Details", class_="item-title", limit=ilimit)

        # Get the prices
        raw_prices = doc.find_all(class_="item-action", limit=ilimit)
        prices = []
        for current_price in raw_prices:
            for price in current_price.find_all(class_="price-current", limit=ilimit):
                if price.strong == None:
                    prices.append(f"No Pricing")
                else:
                    prices.append(f"{price.strong.string}{price.sup.string}")

        # Make dict objects with items
        items = {}
        if s_type == 1:
            for name, price in zip(names, prices):
                items[name.text] = f"${price} --url {name['href']}"
            return items

        else:
            for name, price in zip(names, prices):
                items[name.text] = f"${price}"
            return items


def menu():
    print("===================")
    print("  NewEgg Scrapper")
    print("===================")
    print("[0] Exit the program.")
    print("[1] Basic Search")
    print("[2] Advanced Search")
    print()


def ilimitdefault(ilimit):
    if ilimit == "":
        return 4

    # Limit Error Checking
    try:
        if int(ilimit) > 25:
            sys.exit("\nExceeded result limit!\n")
        elif int(ilimit) <= 0:
            sys.exit("\nInvalid negative or zero result limit!\n")
    except (ValueError, TypeError):
        sys.exit("\nPlease enter a valid option!\n")

    else:
        print()
        return int(ilimit)


def sort_orderdefault(sort_order):
    if sort_order == "":
        return 3

    # Sort Error Checking
    try:
        if int(sort_order) > 5:
            sys.exit("\nExceeded sort options!\n")
        elif int(sort_order) < 0:
            sys.exit("\nInvalid negative sort options!\n")
    except (ValueError, TypeError):
        sys.exit("\nPlease enter a valid option!\n")

    else:
        return int(sort_order)



if __name__ == "__main__":
    main()
