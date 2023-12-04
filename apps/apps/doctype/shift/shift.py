# Copyright (c) 2023, shravan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import format_time

class Shift(Document):
    def before_save(self):
        self.title = {
            format_time(self.start_time,"HH:mm") + "-" +  format_time(self.end_time,"HH:mm")
		}
