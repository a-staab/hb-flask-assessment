from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def show_landing_page():
    """Return landing page with link to application form."""

    return render_template("index.html")


@app.route('/application-form')
def display_form():
    """Display job application form."""

    roles = ["Software Engineer", "QA engineer", "Product Manager"]
    return render_template("application-form.html",
                           jobs=roles)


@app.route('/application-success', methods=["POST"])
def show_confirmation():
    """Show confirmation page repeating applicant's name, the role for which
    they're applying, and the minimum salary they would accept.
    """
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    job_title = request.form.get("select")
    salary = request.form.get("salary")

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           job_title=job_title,
                           salary=salary)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
