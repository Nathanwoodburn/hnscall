# This script is used to redirect subdomains to the HNSCALL server

from flask import Flask, redirect, request
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def redirector():
    # If the host is just hcall, redirect to the join page
    if len(request.host.split('.')) < 2:
        return redirect('https://hnscall/join/'+request.path[1:])
    
    # Else get all subdomain parts
    subdomain = ""
    for part in request.host.split('.')[:-1]:
        subdomain += part + '.'
    
    try:
        # Run dig to get the IP address of the subdomain
        dig = subprocess.run(['dig', '@152.69.186.119', '-p', '5350', subdomain, 'TXT'], capture_output=True, text=True)
        # Get the value of the TXT with HNSCALL=<data>
        hns_call = re.search(r'HNSCALL=(.*)', dig.stdout)
        #If the TXT record exists, redirect to the path
        if hns_call:
            return redirect('https://hnscall/join/'+hns_call.group(1).split('"')[0])
        # If the TXT record doesn't exist, redirect to the home page
        else:
            return redirect('https://hnscall')
    
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the subprocess execution
        error_message = f"Error executing dig command: {e}"
        return error_message, 500

if __name__ == '__main__':
    app.run()