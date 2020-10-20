# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Website's
maximumWebs = 5

while maximumWebs > 0:
    # Input The New Website
    webSite = input("\nWebsite Name Without https://")

    # Add The New Website To The List
    myFavouriteWebs.append(f"https://{webSite.strip().lower()}")

    # Decrease One Number From Allowed Website's
    maximumWebs -= 1 # maximumWebs = maximumWebs - 1

    # Print The Add Message
    print(f"\nWebSite Added, {maximumWebs} Places Left")

    # Print The List
    print(f"\n{myFavouriteWebs}")

else:
    print("\nBookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:
    # Sort The List
    myFavouriteWebs.sort()

    # The Loop Counter
    index = 0

    print("\nPrinting The List Of WebSite's In Your BookMark")

    while index < len(myFavouriteWebs):
        print(f"\n{myFavouriteWebs[index]}")

        # Increase The Loop Counter By One
        index += 1 # index = index + 1
