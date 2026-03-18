import pytest
from httpx import AsyncClient
from app.models import TaskStatus


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_task_status_valid_status_change(client: AsyncClient) -> None:
    """Test updating a task's status with a valid status value."""
    response = await client.patch(
        "/task/1/status",
        json={"status": TaskStatus.IN_PROGRESS.value}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["task_id"] == 1
    assert data["status"] == TaskStatus.IN_PROGRESS.value


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_task_status_task_not_found(client: AsyncClient) -> None:
    """Test updating a task's status when the task does not exist."""
    response = await client.patch(
        "/task/999/status",
        json={"status": TaskStatus.COMPLETE.value}
    )
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_task_status_invalid_status_value(client: AsyncClient) -> None:
    """Test updating a task's status with an invalid status value."""
    response = await client.patch(
        "/task/1/status",
        json={"status": "invalid_status"}
    )
    assert response.status_code == 422
