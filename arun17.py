class ProtectedWitness:
    """Represents a witness under protection."""
    def __init__(self, witness_id, name, age, risk_level):
        self.witness_id = witness_id
        self.name = name
        self.age = age
        self.risk_level = risk_level  # Example: low, medium, or high

class ProtectionDetail:
    """Details about the protection provided to a witness."""
    def __init__(self, detail_id, witness_id, location, description):
        self.detail_id = detail_id
        self.witness_id = witness_id
        self.location = location
        self.description = description


class WitnessStore:
    """Manages the operations and storage for witnesses and their protection details."""
    def __init__(self):
        self.witnesses = {}
        self.protection_details = {}

    def add_witness(self, witness):
        """Adds a new witness to the store."""
        self.witnesses[witness.witness_id] = witness

    def remove_witness(self, witness_id):
        """Removes a witness from the store."""
        if witness_id in self.witnesses:
            del self.witnesses[witness_id]

    def add_protection_detail(self, detail):
        """Adds protection details for a witness."""
        self.protection_details[detail.detail_id] = detail

    def remove_protection_detail(self, detail_id):
        """Removes protection detail."""
        if detail_id in self.protection_details:
            del self.protection_details[detail_id]

    def get_witness_by_id(self, witness_id):
        """Fetches a witness by ID."""
        return self.witnesses.get(witness_id)

    def get_protection_detail_by_id(self, detail_id):
        """Fetches protection detail by ID."""
        return self.protection_details.get(detail_id)

    def update_protection_detail(self, detail_id, **kwargs):
        """Updates the protection detail for flexibility."""
        detail = self.protection_details.get(detail_id)
        if not detail:
            return None
        for key, value in kwargs.items():
            setattr(detail, key, value)
        return detail



def manage_protected_witnesses(store, witness_id):
    """Output management details for a witness."""
    witness = store.get_witness_by_id(witness_id)
    detail = store.get_protection_detail_by_id(witness.witness_id)
    return witness, detail

def ensure_witness_safety(store, safety_id):
    """Check and report on the safety of a witness."""
    detail = store.get_protection_detail_by_id(safety_id)
    if detail and detail.location:
        return True, "Witness is secured at location."
    else:
        return False, "Witness location details missing."


import unittest

class TestWitnessProtection(unittest.TestCase):
    def setUp(self):
        self.store = WitnessStore()
        self.witness = ProtectedWitness(1, 'John Doe', 30, 'high')
        self.detail = ProtectionDetail(101, 1, 'Undisclosed Location', 'Under 24/7 surveillance')

    def test_add_witness(self):
        self.store.add_witness(self.witness)
        self.assertIn(self.witness.witness_id, self.store.witnesses)

    def test_add_protection_detail(self):
        self.store.add_protection_detail(self.detail)
        self.assertIn(self.detail.detail_id, self.store.protection_details)

    def test_ensure_witness_safety(self):
        self.store.add_protection_detail(self.detail)
        is_safe, message = ensure_witness_safety(self.store, 101)
        self.assertTrue(is_safe)

if __name__ == '__main__':
    unittest.main()
