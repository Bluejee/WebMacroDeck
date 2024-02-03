from flask import Flask, render_template, request, jsonify, abort
import actions

app = Flask(__name__)

# Define a mapping of action names to functions
action_map = {
    'login_163': actions.login_163,
    'login_197': actions.login_197,
    # Add other actions here as needed
}


@app.route('/')
def index():
    # Pass the keys of action_map to the template for GET requests
    return render_template('index.html', actions=list(action_map.keys()))


@app.route('/trigger')
def trigger_action():
    action_key = request.args.get('action')
    if action_key not in action_map:
        # If the action is not found in the map, return an error
        abort(404, description="Action not found")

    action_func = action_map[action_key]
    try:
        action_func()  # Execute the corresponding action function
        # You might want to log the action or handle errors as needed
        return '', 204  # Return an empty response (no content) to indicate success
    except Exception as e:
        # Handle any exceptions raised by the action function
        abort(500, description=str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)