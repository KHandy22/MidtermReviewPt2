import pytest
import sys
import os
from unittest.mock import patch
from io import StringIO

# Add parent directory to path to import student's code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestPeculiarEmporium:
    
    def test_receipt_with_mock_input(self):
        """Test receipt generation with mocked input - 10 points"""
        # Mock input values
        test_inputs = ["Magic Beans", "25.50", "4"]
        
        # Expected calculations
        # subtotal = 25.50 * 4 = 102.0
        # tax = 102.0 * 0.095 = 9.69
        # total = 102.0 + 9.69 = 111.69 (rounded)
        
        expected_item_line = "Magic Beans x4 @ $25.5"  # Could also be 25.50
        expected_subtotal = "102.0"  # Could appear as 102.0 or 102
        expected_tax = "9.69"
        expected_total = "111.69"
        
        # Capture output with mocked input
        with patch('builtins.input', side_effect=test_inputs):
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            try:
                import task3
                import importlib
                importlib.reload(task3)
                task3.main()
                
                output = sys.stdout.getvalue()
            finally:
                sys.stdout = old_stdout
        
        # Check receipt format and values
        assert "Magic Beans" in output, "Item name missing from receipt"
        assert "x4" in output, "Quantity missing from receipt"
        assert "25.5" in output, "Price missing from receipt"
        assert "--------------------------" in output, "Receipt separator missing"
        assert "Subtotal:" in output or "subtotal:" in output, "Subtotal label missing"
        assert expected_subtotal in output or "102" in output, "Subtotal value incorrect"
        assert "Tax:" in output or "tax:" in output, "Tax label missing"
        assert expected_tax in output, "Tax value incorrect"
        assert "Total:" in output or "total:" in output, "Total label missing"
        assert expected_total in output, "Total value incorrect"
        assert "Thank you" in output, "Thank you message missing"
        assert "Peculiar Emporium" in output, "Shop name missing from thank you"
