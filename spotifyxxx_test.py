import json
import os
import pdb

from spotifyxxx.py import parse_response_devices,parse_response_artist

# Device raw data for testing
dump_json_device=[{
            "id": "dd8d61e3ebe68159a079e94832a93a62df866c81",
            "is_active": True,
            "is_private_session": False,
            "is_restricted": False,
            "name": "YINI\u2019s MacBook Air",
            "type": "Computer",
            "volume_percent": 100
}]

# Artist raw data for testing
dump_json_artists=[{
             "genres": "pop",
             "id": "2wY79sveU1sp5g7SokKOiI",
             "name": "Sam Smith",
             "type": "artist",
             "uri": "spotify:artist:2wY79sveU1sp5g7SokKOiI"
             }]


parse_response_devices = parse_response_devices(devices)
assert parse_response_devices == dump_json_device

parse_response_artist = parse_response_artist(searchResults)
assert parse_response_artist == dump_json_artists
