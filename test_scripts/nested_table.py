import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class NestedTableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)
        self.table.setRowCount(3)
        self.table.setColumnCount(3)

        # Populate the main table
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QTableWidgetItem(f"({row},{col})")
                self.table.setItem(row, col, item)

        # Create a nested table as a custom widget
        nested_table = QTableWidget(self)
        nested_table.setRowCount(2)
        nested_table.setColumnCount(2)

        for row in range(nested_table.rowCount()):
            for col in range(nested_table.columnCount()):
                item = QTableWidgetItem(f"Nested({row},{col})")
                nested_table.setItem(row, col, item)

        # Set the nested table as a cell widget in the main table
        self.table.setCellWidget(1, 1, nested_table)

        # Adjust table size
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NestedTableWidget()
    window.show()
    sys.exit(app.exec())
