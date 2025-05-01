import os
from flask import Flask, render_template, request, redirect, url_for, session
#   1) Flask - The micro web development framework for building webpages
#   2) render_template - uses the render HTML templates using Jinja2 to generate dynamic HTML templates which allow for Python variables to be integrated into HTML webpages
#   3) request - used to handle incoming data/user requests to applications (like a form submission or URL query). This is stored in request object.
#   4) redirect - used to redirect the user to a different URL when necessary.
#   5) url_for - used to dynamically generate the correct URL for any route in the Flask app.
#   6) session - used to maintain webpage persistence, storing data between requests.

app = Flask(__name__)
app.secret_key = os.urandom(24) # Key for session handling.

# Data Dictionary for all information displayed to dashboard.
zagreus_user_info = { # Database Information
    "MichealRoss999@gmail.com": {
        "password": "AceOSpades05",
        "network_info": [ # Information for Bulleted list
            "Network Range: 12.12.2.0",
            "ISP: Zagreus Telecom",
            "VPN: NordVPN v.6.39",
            "Firewall IP: 12.12.2.1",
            "Mail Server IP: 12.12.2.56",
            "Primary Data Center: London, Carnaby Street",
            "Backup Data Center: Birmingham, Newhall Street / Liverpool, Church Street"
        ],
        "teaminformation": [ # Information for team information table
            {"Name": "Walter White", "Position": "Manager", "Email": "WHW02@gmail.com"},
            {"Name": "Harvey Specter", "Position": "System Administrator", "Email": "Specter_H@hotmail.co.uk"},
            {"Name": "Saul Goodman", "Position": "Finance Officer", "Email": "GoodmanS@gmail.com"}
        ],
        "customers": [ # Information for customers table
            {"Name": "Alice Johnson", "Email": "alicej@hotmail.co.uk", "Phone": "+44 7700 900123", "Data Plan": "10GB Monthly", "Billing": "Paid (£49.00)", "IMEI Device ID": "358765432198765", "SIM ICCID": "89441100006547890123"},
            {"Name": "Emily Davis", "Email": "Dav1sE@gmail.com", "Phone": "+44 7700 900345", "Data Plan": "Unlimited 5G", "Billing": "Overdue (£30.50)", "IMEI Device ID": "357654123987654", "SIM ICCID": "89441100001239876540"},
            {"Name": "Mark Grayson", "Email": "GrayMark@gmail.com", "Phone": "+44 7700 900567", "Data Plan": "Business Plan", "Billing": "Pending (£15.00)", "IMEI Device ID": "351234567890987", "SIM ICCID": "89441100006543876590"},
            {"Name": "James Miller", "Email": "JM01@gmail.com", "Phone": "+44 7700 900789", "Data Plan": "Pay-As-You-Go", "Billing": "Paid (£5.00)", "IMEI Device ID": "359876543212345", "SIM ICCID": "89441100002134567899"}
        ]
    }
}

# ________________ Login Route ________________

@app.route("/", methods=["GET", "POST"]) # Defines the route for the Login page. Allows for HTTP GET and POST methods

def login(): # Define Login Function.
    if request.method == "POST": # If the request method is a HTTP POST request, it means that the user submitted a form.
        email = request.form["email"] # Verifies email input
        password = request.form["psword"] # Verifies password input

        if email in zagreus_user_info and zagreus_user_info[email]["password"] == password: # if input matches dictionary.
            session["email"] = email # The email is stored within the session
            return redirect(url_for("dashboard")) # User is redirected to dashboard
        else:
            return "Invalid credentials, please try again.", 401 # Present error 401 (Unauthorised client error response)

    return render_template("Zagreus_Login.html") # Displays login form using GET request.

# ________________ Dashboard Route ________________

@app.route("/dashboard") # Defines the route for the Dashboard page.

def dashboard(): # Define Dashboard Function
    if "email" not in session: # If email is not logged in the session
        return redirect(url_for("login")) # Redirects back to login page 

    user_data = zagreus_user_info.get(session["email"]) # Retrieves user data from Dictionary
    if user_data: # If Data exists
        return render_template("Zagreus_Dashboard.html", user=user_data) # Pass user data to Dashboard
    else:
        return redirect(url_for("login"))  # Redirects back to login if user not found

# ________________ Logout Route ________________

@app.route("/logout", methods=["POST"]) # Defined for when a user logs out. Allows for HTTP POST (used for resource creation) method.

def logout(): # Defines Logout Function
    session.pop("email", None) # Remove user from session
    return redirect(url_for("login")) # Redirects users back to login screen

if __name__ == "__main__": # ensures script runs only when executed directly
    app.run(debug=True) # enables auto-reload on code changes
