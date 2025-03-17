import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Updated fake_users with structured transactions
fake_users = {
    "MichealRoss999@gmail.com": {
        "password": "AceOSpades05",
        "network_info": [
            "Network Range: 12.12.2.0",
            "ISP: Zagreus Telecom",
            "VPN: NordVPN v.6.39",
            "Firewall IP: 12.12.2.1",
            "Mail Server IP: 12.12.2.56",
            "Primary Data Center: London, Carnaby Street",
            "Backup Data Center: Birmingham, Newhall Street / Liverpool, Church Street"
        ],
        "teaminformation": [
            {"Name": "Walter White", "Position": "Manager", "Email": "WHW02@gmail.com"},
            {"Name": "Harvey Specter", "Position": "System Administrator", "Email": "Specter_H@hotmail.co.uk"},
            {"Name": "Saul Goodman", "Position": "Finance Officer", "Email": "GoodmanS@gmail.com"}
        ],
        "customers": [
            {"Name": "Alice Johnson", "Email": "alicej@hotmail.co.uk", "Phone": "+44 7700 900123", "Data Plan": "10GB Monthly", "Billing": "Paid (£49.00)", "IMEI Device ID": "358765432198765", "SIM ICCID": "89441100006547890123"},
            {"Name": "Emily Davis", "Email": "Dav1sE@gmail.com", "Phone": "+44 7700 900345", "Data Plan": "Unlimited 5G", "Billing": "Overdue (£30.50)", "IMEI Device ID": "357654123987654", "SIM ICCID": "89441100001239876540"},
            {"Name": "Mark Grayson", "Email": "GrayMark@gmail.com", "Phone": "+44 7700 900567", "Data Plan": "Business Plan", "Billing": "Pending (£15.00)", "IMEI Device ID": "351234567890987", "SIM ICCID": "89441100006543876590"},
            {"Name": "James Miller", "Email": "JM01@gmail.com", "Phone": "+44 7700 900789", "Data Plan": "Pay-As-You-Go", "Billing": "Paid (£5.00)", "IMEI Device ID": "359876543212345", "SIM ICCID": "89441100002134567899"}
        ]
    }
}

# ________________ Login Route ________________
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["psw"]

        if email in fake_users and fake_users[email]["password"] == password:
            session["email"] = email  
            return redirect(url_for("dashboard"))  
        else:
            return "Invalid credentials, please try again.", 401  

    return render_template("Login.html")  

# ________________ Dashboard Route ________________
@app.route("/dashboard")
def dashboard():
    if "email" not in session:
        return redirect(url_for("login"))  

    user_data = fake_users.get(session["email"])
    if user_data:
        return render_template("Dashboard.html", user=user_data)  
    else:
        return redirect(url_for("login"))  

# ________________ Logout Route ________________
@app.route("/logout", methods=["POST"])
def logout():
    session.pop("email", None)  
    return redirect(url_for("login"))  

if __name__ == "__main__":
    app.run(debug=True)
