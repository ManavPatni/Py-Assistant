## Py Assistant - Ruby: A Voice-Controlled Python Assistant 

This Python script creates a voice-controlled assistant named Ruby using various libraries for speech recognition, text-to-speech, and web interactions. Ruby can perform a variety of tasks based on user commands, including:

**Basic Information and Actions:**

*   Tell you the current time and date
*   Open applications like YouTube, Facebook, Instagram, Chrome, Notepad, Calculator, Word, Excel
*   Search for information on Google, YouTube, and Wikipedia
*   Provide summaries of Wikipedia articles
*   Check train and flight status
*   Search for flights based on departure and arrival locations
*   Display weather information for a specified city
*   Get details about a phone number, including location and service provider
*   Toss a coin and tell you the result
*   Create notes and open them in Notepad
*   Search for locations on Google Maps

**Additional Features:**

*   The assistant responds to natural language commands. 
*   It uses text-to-speech to communicate with the user.
*   A graphical user interface (GUI) displays the conversation and allows users to activate the listening function.
*   The script utilizes threading for efficient task management.

**Technical Details:**

*   **Libraries:** 
    *   `webbrowser`: Opens web pages in the user's default browser.
    *   `pyttsx3`: Enables text-to-speech functionality.
    *   `speech_recognition`: Recognizes speech input from the user.
    *   `datetime`: Provides functions for working with dates and times.
    *   `wikipedia`: Allows access to Wikipedia information.
    *   `os`: Interacts with the operating system.
    *   `requests`: Makes HTTP requests for fetching data.
    *   `phonenumbers`: Extracts information from phone numbers.
    *   `random`: Generates random numbers for functionalities like coin toss.
    *   `subprocess`: Executes system commands.
    *   `time`: Provides time-related functions.
    *   `tkinter`: Creates the graphical user interface.
    *   `PIL`: Handles image processing for the GUI.
    *   `threading`: Enables multithreading for concurrent tasks.
*   **Threading:** The script uses threading to run the main functionality in a separate thread, allowing the GUI to remain responsive while the assistant processes commands.

**How to Use:**

1.  **Install Required Libraries:** Ensure you have all the necessary libraries installed using pip:

    ```bash
    pip install webbrowser pyttsx3 speech_recognition datetime wikipedia os requests phonenumbers random subprocess time tkinter pillow
    ```
2.  **Run the Script:** Execute the Python script. 
3.  **Interact with Ruby:** Speak your commands clearly into the microphone. The assistant will respond with spoken feedback and display the conversation in the GUI.

**Customization:**

*   You can modify the script to add more commands and functionalities.
*   The voice and speed of the text-to-speech engine can be adjusted.
*   The GUI can be customized to your preferences. 

**Limitations:**

*   The assistant's accuracy depends on the quality of the speech recognition and the clarity of the user's voice.
*   The available commands are limited to those defined in the script.
*   Internet connection is required for some functionalities. 
