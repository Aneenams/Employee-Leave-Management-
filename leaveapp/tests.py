from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from leaveapp.serializers import LeaveSerializer


class LeaveSerializerDateValidationTests(TestCase):
	def leave_data(self, start_date):
		return {
			"employee_name": "Alex",
			"reason": "Annual leave",
			"start_date": start_date,
			"end_date": start_date,
			"leave_type": "Annual",
		}

	def test_rejects_start_date_in_past(self):
		yesterday = timezone.localdate() - timedelta(days=1)
		serializer = LeaveSerializer(data=self.leave_data(yesterday))

		self.assertFalse(serializer.is_valid())
		self.assertIn("start_date", serializer.errors)

	def test_allows_start_date_today(self):
		today = timezone.localdate()
		serializer = LeaveSerializer(data=self.leave_data(today))

		self.assertTrue(serializer.is_valid(), serializer.errors)
