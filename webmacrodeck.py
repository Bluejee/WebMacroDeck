from flask import Flask, render_template, request, jsonify, abort
import actions

app = Flask(__name__)

# Define a mapping of action names to functions
action_map = {
    'type_text': actions.type_text,
    'open_app': actions.open_app,
    'open_website': actions.open_website,
    'open_workspace': actions.open_workspace,
    'volume_up': actions.volume_up,
    'volume_down': actions.volume_down,
    'mute_unmute': actions.mute_unmute,
    'copy': actions.copy,
    'cut': actions.cut,
    'paste': actions.paste,
    # Add other functions from the actions file as needed
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