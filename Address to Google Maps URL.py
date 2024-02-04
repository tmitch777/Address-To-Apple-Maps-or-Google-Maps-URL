def convert_to_google_maps_url(address):
    # Replace spaces with plus signs for the query
    query = address.replace(' ', '+')
    
    # Construct the Google Maps URL
    map_url = f'https://www.google.com/maps/place/{query}'
    return map_url

def bulk_convert_to_google_maps(addresses):
    google_map_urls = []
    for address in addresses:
        map_url = convert_to_google_maps_url(address)
        google_map_urls.append(map_url)
    return google_map_urls

if __name__ == "__main__":
    # Example addresses, replace with your own list of addresses
    addresses = [
    "4455 Ville Pkwy, Birdland, CA 94587",
    ]

    google_map_urls = bulk_convert_to_google_maps(addresses)

    # Display the generated Google Map URLs
    for i, url in enumerate(google_map_urls, start=1):
        print(f'{url}')

        
