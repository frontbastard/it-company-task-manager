import os
from dotenv import load_dotenv
import sys
import django
from django.contrib.auth import get_user_model
from django.core.management import call_command
from faker import Faker
import random
from datetime import datetime, timedelta

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

django.setup()

from tasks.models import Position, TaskType, Tag, Task

# Clear data before loading new
call_command("flush", "--no-input")

User = get_user_model()
fake = Faker()

# Creating positions
positions = []
for _ in range(5):
    positions.append(Position.objects.create(name=fake.job()))

# Creating workers
users = []
for _ in range(random.randint(15, 20)):
    user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password=os.getenv("SECRET_KEY"),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        position=random.choice(positions) if random.random() > 0.5 else None,
    )
    users.append(user)

# Creating task types
task_types = []
for _ in range(5):
    task_types.append(TaskType.objects.create(name=fake.word()))

# Creating tags
tags = []
for _ in range(5):
    tags.append(Tag.objects.create(name=fake.word()))

# Creating tasks
tasks = []
for _ in range(random.randint(15, 25)):
    task = Task.objects.create(
        name=fake.sentence(),
        description=fake.paragraph(10),
        deadline=datetime.now() + timedelta(days=random.randint(1, 30)),
        is_completed=random.choice([True, False]),
        priority=random.choice([choice[0] for choice in Task.PriorityChoices.choices]),
        task_type=random.choice(task_types),
        created_at=fake.date_time_between(start_date="-1y", end_date="now"),
        updated_at=fake.date_time_between(start_date="-1y", end_date="now"),
    )
    task.assignees.set(random.sample(users, k=random.randint(1, 5)))
    task.tags.set(random.sample(tags, k=random.randint(1, 5)))
    tasks.append(task)

# Save data in JSON file
filename = "fixtures/task_manager_db_data.json"

with open(filename, "w") as f:
    call_command(
        "dumpdata",
        "tasks.position",
        "tasks.tasktype",
        "tasks.tag",
        "tasks.task",
        indent=2,
        stdout=f,
    )

User.objects.create_superuser(
    username="admin",
    email="admin@example.com",
    password=os.getenv("SECRET_KEY"),
    first_name="Admin",
    last_name="User"
)

print(f"Demo data saved to {filename}")
