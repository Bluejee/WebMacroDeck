# WebMacroDeck 🚀

WebMacroDeck is a local server-based tool designed to emulate a macro keyboard with fully customizable buttons. This
innovative server enables users to execute a wide range of predefined Python functions—ranging from text manipulation to
application and web navigation, system control, and clipboard functions—through an intuitive web interface. Built on
Flask for server-side operations and leveraging PyAutoGUI for seamless keyboard and mouse control, WebMacroDeck offers a
highly flexible solution for automating routine tasks and boosting productivity.

## Key Features 🌟

- **Text Manipulation:** Effortlessly simulate typing, including support for newline characters and intentional delays,
  to mimic natural typing behavior. This functionality proves to be exceptionally useful in scenarios such as logging
  into multiple servers using ssh with different IP addresses, memorizing frequently typed phrases, or managing
  addresses. Whether you're navigating through routine login sequences or inputting repetitive data across various
  platforms, WebMacroDeck's text manipulation capabilities streamline your workflows, making them more efficient and
  less prone to error.
- **Application & Web Navigation:** Launch applications and navigate to websites directly from your MacroDeck with a
  single click.
- **Workspace Setup:** Instantly prepare your development environment by opening specified folders in Windows Explorer,
  PyCharm, and Visual Studio Code or any combination of workspace organisations.
- **System Control:** Have control over your system's volume and toggle mute with ease.
- **Clipboard Management:** Simplify copying, cutting, and pasting operations.
- **Limitless Automation:** Virtually anything you can script can be turned into a button click action, opening endless
  possibilities for automation, So Go Crazy

## Security Advisory ⚠️

- **VERY IMPORTANT:** WebMacroDeck is designed to enhance productivity through automation on your private network. It is
  crucial to be aware of the security implications of using this tool, especially since it lacks advanced security
  features at this stage. This means anyone with access to your network could potentially control your machine or
  execute the predefined actions. **Use WebMacroDeck within a trusted environment and be mindful of the network security
  settings.** If you have any concerns or need clarification on the potential risks, please do not hesitate
  to [open an issue](https://github.com/Bluejee/WebMacroDeck/issues). We're here to help and discuss any security
  concerns you might have, ensuring you can use WebMacroDeck safely and effectively.

## Getting Started 🛠

### Prerequisites

Before diving into WebMacroDeck, make sure you have Python 3.x installed on your system. Additionally, you'll need Flask
and PyAutoGUI, which can be installed via pip:

```sh
pip install flask pyautogui
```

### Installation and Setup

1. **Clone the repository** to your local machine using the command below:

```sh
git clone https://github.com/Bluejee/WebMacroDeck.git
```

(Or just download the folder, although that would make you look weaker in front of your tech pals)

2. **Launch the Server** by going into the WebMacroDeck directory and running the following command in the project's
   root directory:

```sh
python webmacrodeck.py
```

This fires up the Flask server, making WebMacroDeck accessible at `http://localhost:5000` and across your local
network (e.g., `http://192.168.1.5:5000`).

## How to Use 📚

Once the server is up, simply open the provided URL(The Local IP one, not the local host as it won't be accessible from
other devices.) in your web browser to interact with the WebMacroDeck interface.

(I think it is clear that I mean the web browser of another device like a smartphone or a tablet. Using a spare device
is the best case scenario as using it like a Stream Deck or a Macro Keyboard is the Main Idea)

- **Interface Overview:** The web page showcases a grid of buttons, each linked to a specific action. This setup is
  ideal for using a smartphone, tablet, or any touch device as a macro keyboard.

- **Executing Actions:** Click any button on the web interface to trigger the corresponding action. From opening
  websites to managing your clipboard, each action is just a tap away.

- **Modifying Actions:** To adjust or add new actions, tweak the `actions.py` file and update the `action_map`
  in `webmacrodeck.py`. Restart the server to apply changes and refresh the action buttons displayed on the web
  interface.

## Customization 🎨

- **Function Adjustments:** To tailor WebMacroDeck to your specific needs, you can modify `actions.py` to tweak existing
  functions or to introduce entirely new functionalities. It's important to note that these functions should be designed
  for direct execution via the web interface, thus should not require any parameters. Additionally, it's crucial to
  understand that simply defining a new function doesn't automatically make it available in the UI. For a function to be
  accessible through the WebMacroDeck interface, you must manually add it to the `action_map` within
  the `webmacrodeck.py` file. This extra step ensures that only intended actions are exposed to users.

- **UI Tweaks:** The appearance and layout of the action buttons are fully customizable to better suit your personal or
  organizational branding. To achieve this, dive into the `templates/index.html` and `static/css/style.css` files. These
  files control the structure and style of the WebMacroDeck interface, allowing for adjustments ranging from button
  colors and sizes to the overall layout. Experimenting with these files can lead to a more aesthetically pleasing and
  functional macro deck that aligns with your preferences or workspace requirements.

## Help with WebMacroDeck

If you need help regarding WebMacroDeck, then please open an issue or reach out to me through any of the contacts you
can find in my [GitHub Profile](https://github.com/Bluejee)

If you would like to submit a bug report or feature request,
please [open an issue](https://github.com/Bluejee/WebMacroDeck/issues).

## Contributing

Contributions to this project are always welcome. Please see
the [Contribution Guidelines](https://github.com/Bluejee/WebMacroDeck/blob/main/CONTRIBUTING.md) to see how to help.

## Code of Conduct

I value a positive and respectful community, and I kindly ask that you follow our code of conduct in all interactions
with other members. Please take a moment to review
the [Code of Conduct](https://github.com/Bluejee/WebMacroDeck/blob/main/CODE_OF_CONDUCT.md).

## License

Please refer the [License](https://github.com/Bluejee/WebMacroDeck/blob/main/LICENSE.txt) of this project to understand
about your rights.
