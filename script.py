"""
Prints audience stats to CSV
"""
import requests
import json
import csv
import time


def fetch_jwt_token(client_id,
                    client_secret, account_id):
    """
    :param account_id: mParticle account ID
    :param client_secret: mParticle client secret
    :param client_id: mParticle client ID
    :return: return the JWT token
    """

    # API URL
    token_api_url = 'https://sso.auth.mparticle.com/oauth/token'

    headers = {
        'Content-Type': 'application/json',
    }

    # Fetch JWT token
    auth_payload = json.dumps({
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": "https://api.mparticle.com",
        "grant_type": "client_credentials"
    })
    try:
        response = requests.request('POST', token_api_url, headers=headers, data=auth_payload)
        if response.status_code == 200:
            jwt_token = response.json().get('access_token')
            audience_download(jwt_token=jwt_token, account_id=account_id)
        else:
            print("Error retrieving JWT token")

    except requests.exceptions.ConnectionError as e:
        print("Error retrieving JWT token")


def audience_download(jwt_token, account_id):
    """
    :param account_id: mParticle account_id
    :param jwt_token:jwt token from the auth API
    :return: return the payload from audience
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(jwt_token)
    }

    # Platform API URL
    platform_api_base_url = "https://api.mparticle.com/v1/audiences?accountId={}".format(account_id)

    try:
        response = requests.request('GET', platform_api_base_url, headers=headers)
        if response.status_code == 200:
            write_csv(response.json().get('data'))
        else:
            print("Error retrieving audience from the platform API")

    except requests.exceptions.ConnectionError as e:
        print("Error retrieving audience from the platform API")


def write_csv(payload):
    """
    :return: returns status of the file creation
    """
    export_file_name = 'audience_info_{}.csv'.format(str(int(time.time())))
    try:
        with open(export_file_name, mode='w') as export_file:
            export_writer = csv.writer(export_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Write header
            export_writer.writerow(
                ['Audience Name', 'Audience ID', 'Status', 'Size', 'Created By', 'Last Modified By', 'Last Modified On',
                 '# Added Last 24 Hrs', '# Dropped Last 24 Hrs'])
            # Loop through the payload and write to CSV
            for i in range(len(payload)):
                audience_row = [payload[i].get('name'), payload[i].get('id'), payload[i].get('status'),
                                payload[i].get('size'), payload[i].get('created_by'),
                                payload[i].get('last_modified_by'),
                                payload[i].get('last_modified_on'), payload[i].get('added_last_24_hours'),
                                payload[i].get('dropped_last_24_hours')]
                export_writer.writerow(audience_row)
        print('done!')
    except requests.exceptions.ConnectionError as e:
        print("Error Generating CSV file")


if __name__ == '__main__':
    # New credentials can be obtained from here
    # https://docs.mparticle.com/developers/credential-management#creating-new-credentials;
    # account ID is displayed on the pop-up when setting up the credentials
    fetch_jwt_token(client_id='client_id', client_secret='client_secret', account_id='test')
