import unittest
from unittest.mock import patch, mock_open
from task_manager import TaskManager, Task

class TestTaskManagerDelete(unittest.TestCase):
    def setUp(self):
        with patch.object(TaskManager, "load_tasks"), patch.object(TaskManager, "save_tasks"):
            self.tm = TaskManager()

    @patch("builtins.open", new_callable=mock_open)
    def test_add_task(self, mock_file):
            with patch("builtins.print") as mock_print:
                self.tm.add_task("New Task")
                mock_print
            self.assertEqual(len(self.tm._tasks), 1)
            self.assertEqual(self.tm._tasks[0].description, "New Task")

    @patch("builtins.open", new_callable=mock_open)
    def test_delete_existing_task(self, mock_file):
        self.tm.add_task("Task to delete")
        task_id = self.tm._tasks[0].id
        with patch("builtins.print") as mock_print:
            self.tm.delete_task(task_id)
            mock_print.assert_called_with(f"Task deleted: [  #{task_id}: Task to delete]")
        self.assertEqual(len(self.tm._tasks), 0)

    @patch("builtins.open", new_callable=mock_open)
    def test_delete_non_existing_task(self, mock_file):
        with patch("builtins.print") as mock_print:
            self.tm.delete_task(999)
            mock_print.assert_called_with("Task not found: #999")

    @patch("builtins.open", new_callable=mock_open)
    def test_list_tasks(self, mock_file):
        self.tm.add_task("Task 1")
        self.tm.add_task("Task 2")
        self.tm.add_task("Task 3")
        with patch("builtins.print") as mock_print:
            self.tm.list_tasks()
        self.assertEqual(len(self.tm._tasks), 3)

    @patch("builtins.open", new_callable=mock_open)
    def test_complete_tasks(self, mock_file):
        self.tm.add_task("Task to complete")
        task_id = self.tm._tasks[0].id
        with patch("builtins.print") as mock_print:
            self.tm.mark_complete_task(task_id)
            mock_print.assert_called_with(f"Task marked as completed: [✔ #{task_id}: Task to complete]")
        self.assertTrue(self.tm._tasks[0].completed)

    @patch("builtins.open", new_callable=mock_open)
    def test_delete_multiple_tasks(self, mock_file):
        self.tm._tasks = [Task(1, "Task 1", False), Task(2, "Task 2", False), Task(3, "Task 3", False)]
        self.tm.next_id = 4
        with patch("builtins.print") as mock_print:
            self.tm.delete_task(2)
            mock_print.assert_called_with("Task deleted: [  #2: Task 2]")
        self.assertEqual([t.id for t in self.tm._tasks], [1, 3])

if __name__ == "__main__":
    unittest.main()
