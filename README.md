# brighntessControl

Simple python script to change brighntess and batchs script to execute the python script.

## Automatic Brightness Adjustment with Python Script

This document explains how to use the provided Python script, `brightness.py`, to automatically adjust your screen brightness based on the time of day.

**Requirements:**

* Python 3 (tested with Python 3.x)
* `screen_brightness_control` library: This library allows you to control screen brightness on your system. You can install it using `pip install screen_brightness_control`.

**How it Works:**

The script defines two time periods:

* **Daytime:** Brightness is set to a higher level (default: 100%) for better visibility during work hours. 
* **Nighttime:** Brightness is set to a lower level (default: 50%) to reduce eye strain in low-light conditions.

The script checks the current time and adjusts the screen brightness accordingly based on the predefined time intervals.

**Running the Script:**

1. **Install the library:** Open a terminal or command prompt and run:

   ```bash
   pip install screen_brightness_control
   ```

2. **Save the Script:** Save the provided Python script (which you mentioned includes the code) as `brightness.py`.

3. **Run the Script:** Open a terminal or command prompt, navigate to the directory where you saved the script, and run:

   ```bash
   python brightness.py
   ```

This will adjust the brightness based on the current time according to the script's settings.

**Customization:**

* **Brightness Levels:** Modify the `day_brightness` and `night_brightness` variables in the script to adjust the desired brightness levels for day and night.
* **Time Intervals:** Change the `start_hour`, `start_minute`, `stop_hour`, and `stop_minute` variables to define your preferred time periods for day and night brightness.

**Task Scheduler Integration (Optional):**

* The script can be integrated with Task Scheduler (Windows) or a similar tool on your operating system to run automatically at startup or specific times. 

**Additional Notes:**

* This script assumes the `screen_brightness_control` library can adjust your screen brightness. Compatibility might vary depending on your system.
* Make sure the script has the necessary permissions to adjust brightness (might require running it with administrator privileges).

By using this script and potentially integrating it with a task scheduler, you can automate screen brightness adjustments to improve eye comfort and potentially save energy.


## Automatic Brightness Adjustment with Batch Script and Task Scheduler

This guide explains how to configure the `brightness.bat` file and use Task Scheduler to automatically adjust your screen brightness based on the time of day using a Python script.

**Requirements:**

* **brightness.bat:** The provided batch file (which you mentioned includes the code).
* **Python 3 (tested with Python 3.x):** Make sure you have Python 3 installed on your system.
* **`screen_brightness_control` library:** This library allows you to control screen brightness. Install it using `pip install screen_brightness_control` by opening a command prompt or terminal and running the command.

**Configuration:**

1. **Python Script:** Ensure you have the python script ( `brightness.py`) that controls screen brightness based on time. You can find many online resources for such scripts. 
2. **Batch File (`brightness.bat`):**
    * The provided batch file likely includes a line like:
        ```batch
        python C:\Users\Username\Documents\brightness\brightness.py
        ```
    *  **Modify the path:** Replace `C:\Users\Username\Documents\brightness` with the actual location of your Python script (`brightness.py`).

**Task Scheduler Setup:**

1. **Open Task Scheduler:** Search for "Task Scheduler" in the Start Menu or use "taskschd.msc".

2. **Create Tasks:** You'll need to create two separate tasks, one for morning and one for evening.

    **Morning Task:**

    * Click on **"Create Basic Task"** in the Actions pane.
    * Enter a descriptive name like "Set Morning Brightness" and an optional description.
    * Choose the trigger: **"Daily"**. Set the desired time for the morning brightness adjustment.
    * In the **"Action"** section, select **"Start a program"**.
    * Browse to your batch file (`brightness.bat`) and select it.
    * (Optional) In the "Start in (Optional)" field, enter the full path to the folder containing your batch file (without quotes).
    * Review the summary and click **"Finish"** to create the task.

    **Evening Task:**

    * Repeat the steps above to create another **"Basic Task"**.
    * Name it descriptively, like "Set Evening Brightness".
    * Choose the trigger: **"Daily"**. Set the desired time for the evening brightness adjustment.
    * Follow the same steps under **"Action"** to point to your batch file.
    * Review and click **"Finish"** to create the evening task.

**Testing:**

* Right-click on each newly created task and select **"Run"** to test them manually before relying on the schedule.

**Additional Notes:**

* This guide assumes basic familiarity with creating tasks in Task Scheduler. 
* The batch file assumes your Python script can adjust brightness. 
* Make sure your Python script has the necessary permissions (might require administrator privileges).
* You can adjust the brightness levels and time intervals directly in your Python script.

By following these steps, you can automate screen brightness adjustments for improved eye comfort and potentially save energy.