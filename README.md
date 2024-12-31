# dictionary-attack-demo
Dictionary Attack Demo for educational purposes.

This project demonstrates a dictionary attack on a website with a vulnerable login API. The app is implemented in Flask and includes a vulnerable login endpoint.
The repo also contain the option of running a live visual demo using a flask html template.

## Features

- A basic login page (`/`)
- A vulnerable API endpoint (`/api/login`)
- Demonstration script for dictionary attack
- A list of common passwords ('pass_strings.txt')

## How to Run

1. Clone the repository:
    ```
    git clone <repository-url>
    cd dictionary_attack_demo
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```
    python app/app.py
    ```

4. Test the attack script:
    ```
    python demo.py
    ```
5. If you wish, show a demo of the attack using your web browser - 
it will be available under localhost:{your flask port}(usually 5000)

## Important Notes

This project is for educational purposes **ONLY**. Do not use this to attack real systems.
The template login.html file was added for a more visual demo - you can just execute a "backend demo" if you wish.

## Dependencies

- Flask
- requests