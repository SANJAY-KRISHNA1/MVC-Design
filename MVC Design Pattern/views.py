from flask import render_template  # type: ignore
 
def render_data(data): 
    # Render the data using an HTML template 
    return render_template('index.html', users=data)