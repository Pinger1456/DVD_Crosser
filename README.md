
# DVD Logo Animation Project
![DVD Animation](https://imgur.com/a/fEBUHaP)

This project simulates the bouncing DVD logo animation, a nostalgic representation for many who remember the idle screen on DVD players. The logo changes direction when it hits the screen edges and also changes color when it bounces off the screen's corners.

## Project Structure

The project is divided into the following components:

- `main.py`: The main entry point for running the DVD animation.
- `dvd_logo.py`: Contains the `Logo` class, which manages the position, direction, and movement of the DVD logo.
- `dvd_animation.py`: Contains the `DVDAnimation` class, which manages the overall animation, including multiple logos.
- `.env`: Configuration file for managing environment variables like the number of logos, pause duration, and more.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
   
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Install additional development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```

## Environment Variables

To customize the animation, you can use the `.env` file to specify parameters like the number of logos, their colors, and the speed of animation. Here's an example `.env` configuration:

```
NUM_DIGITS=4
MAX_GUESSES=10
NUMBER_OF_LOGOS=5
PAUSE_AMOUNT=0.5
COLORS=red,green,yellow,blue,magenta,cyan,white
UP_RIGHT=ur
UP_LEFT=ul
DOWN_RIGHT=dr
DOWN_LEFT=dl
```

## Running the Project

To start the DVD animation, run the following command:

```bash
python main.py
```

## Customization

You can customize the animation by modifying the `.env` file to change:
- **NUMBER_OF_LOGOS**: Adjust the number of bouncing logos.
- **PAUSE_AMOUNT**: Adjust the speed of the animation.
- **COLORS**: Change the available colors for the logos.

## Development

If you wish to modify or extend the project, you can use the following tools (assuming you have installed `requirements-dev.txt`):
- `pylint`: For static code analysis and linting.
- `pytest`: For running unit tests.
- `black`: For automatic code formatting.

## License

This project is licensed under the MIT License.
