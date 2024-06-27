# Task Manager

## Description

Task Manager is a robust tool designed for managing tasks efficiently and effectively. It helps streamline task management, ensuring better organization and productivity.

---

## Demo

https://it-company-task-manager-hvco.onrender.com/
- Login: admin
- Password: 1qazcde3

> ### If the page does not load
> 
> Most likely, you will need to wait about 50 seconds for the service that hosts the project to bring up the environment. Since this is a free plan on render.com, after 5 minutes of inactivity, the project becomes inactive and takes about a minute to turn back on.

---

## Installing / Getting started

To get the Task Manager up and running, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/frontbastard/it-company-task-manager.git
    cd it-company-task-manager/
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables:**
    Rename the `.env.sample` file to `.env` in the root directory and add the necessary environment variables.

4. **Run the Project:**
    ```bash
    python manage.py runserver
    ```

When you execute the above commands, the Task Manager application will start running locally on your machine, ready for use.

---

## Initial Configuration

After setting up the project, ensure the following initial configurations are done:

1. **Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

3. **Load Initial Data:**
    ```bash
    python manage.py loaddata task_manager_db_data.json
    ```

You can also run the command which will create a new `task_manager_db_data.json` and automatically load created data to DB:
```bash
python fixtures/create_demo_data.py
```
---

## Developing

To start developing the project further, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/frontbastard/it-company-task-manager.git
    cd it-company-task-manager/
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a Branch:**
    ```bash
    git checkout -b feature-branch
    ```

4. **Make Changes and Commit:**
    ```bash
    git add .
    git commit -m "Your commit message"
    ```

5. **Push Changes:**
    ```bash
    git push origin feature-branch
    ```

---

**Building**

If your project requires additional steps to build, follow these instructions:

1. **Build Project:**
    ```bash
    ./configure
    make
    make install
    ```

Executing these commands will compile and build the project, making it ready for deployment.

---

## Deploying / Publishing

To deploy the Task Manager project to a server, use the following command:

```bash
packagemanager deploy it-company-task-manager -s server.com -u username -p password
```

This command will deploy your project to the specified server with the provided credentials.

---

**Features**

- **Task Management:** Create, update, and delete tasks efficiently.
- **Priority Setting:** Assign different priority levels to tasks.
- **Tagging:** Organize tasks using tags for better categorization.
- **User Assignment:** Assign tasks to different users or teams.

---

## Contributing

We welcome contributions to the Task Manager project. To contribute, please fork the repository and create a feature branch. Pull requests are warmly welcome.

---

## Links

- **Project Homepage:** [Task Manager](https://it-company-task-manager-hvco.onrender.com/)
- **Repository:** [GitHub Repository](https://github.com/frontbastard/it-company-task-manager.git/)
- **Issue Tracker:** [GitHub Issues](https://github.com/frontbastard/it-company-task-manager.git/issues)

For sensitive bugs like security vulnerabilities, please contact [my@email.com](mailto:my@email.com) directly instead of using the issue tracker. We appreciate your efforts to improve the security and privacy of this project!

---

**Licensing**

The code in this project is licensed under the MIT License.