from enum import Enum

from pydantic import BaseModel


class TaskStatus(str, Enum):
    """Available statuses for any task."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"


class DeveloperTask(BaseModel):
    """Model for a single task logged by a developer."""
    task_id: int
    title: str
    status: TaskStatus = TaskStatus.PENDING
    hours_spent: float = 0.0


class ProductivityReport(BaseModel):
    """The final calculated report."""
    total_tasks: int
    completed_tasks: int
    total_hours_spent: float
    completion_rate: float


class StatusUpdate(BaseModel):
    """Model for updating a task's status."""
    status: TaskStatus


class TaskCompletionMetrics(BaseModel):
    """Metrics summarizing task completion performance."""
    total_completed: int
    total_pending: int
    total_in_progress: int
    average_hours_per_task: float
    completion_rate: float
