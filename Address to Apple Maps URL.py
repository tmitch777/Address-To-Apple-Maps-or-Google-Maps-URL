import urllib.parse

def convert_to_apple_maps_url(address):
    encoded_address = urllib.parse.quote(address)
    apple_maps_url = f"https://maps.apple.com/?address={encoded_address}"
    return apple_maps_url

def bulk_convert_to_apple_maps_urls(address_list):
    apple_maps_urls = [convert_to_apple_maps_url(address) for address in address_list]
    return apple_maps_urls

# Example addresses
addresses = [
"4455 Ville Pkwy, Birdland, CA 94587",
]

# Convert to Apple Maps URLs
apple_maps_urls = bulk_convert_to_apple_maps_urls(addresses)

# Print the results
for address, apple_maps_url in zip(addresses, apple_maps_urls):
    print(apple_maps_url)