from flask import Flask, render_template, request, jsonify, abort
import actions

app = Flask(__name__)

# Define a mapping of action names to functions, colors and respective positions
action_map = {
    'type_text': [actions.type_text, 'green', 1],
    'open_app': [actions.open_app, 'blue', 5],
    'open_website': [actions.open_website, 'orange', 6],
    'open_workspace': [actions.open_workspace, 'light_blue', 7],
    'volume_up': [actions.volume_up, 'red', 16],
    'volume_down': [actions.volume_down, 'purple', 20],
    'mute_unmute': [actions.mute_unmute, 'pink', 24],
    'copy': [actions.copy, 'brown', 17],
    'cut': [actions.cut, 'gray', 13],
    'paste': [actions.paste, 'cyan', 21],
    # Add other functions from the actions file with colors and positions as needed
}

# Creating a list for holding the positions of dummy icons. This is passed to the template to index the dummy icons.
dummy_list = [i for i in range (1,33)]
for key,value in action_map.items():
    if value[2] in dummy_list:
        dummy_list.remove(value[2])
        

@app.route('/')
def index():
    # Pass the keys of action_map along with their color and position to the template for GET requests
    action_tp = [{'name': action_key, 'color': action_data[1], 'position': action_data[2]} for action_key, action_data in action_map.items()]
    return render_template('index.html', actions=action_tp, ilist = dummy_list)


@app.route('/trigger')
def trigger_action():
    action_key = request.args.get('action')
    if action_key not in action_map:
        # If the action is not found in the map, return an error
        abort(404, description="Action not found")

    action_func = action_map[action_key][0]
    try:
        action_func()  # Execute the corresponding action function
        # You might want to log the action or handle errors as needed
        return '', 204  # Return an empty response (no content) to indicate success
    except Exception as e:
        # Handle any exceptions raised by the action function
        abort(500, description=str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)